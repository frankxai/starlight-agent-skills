import copy
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('brain', ROOT/'scripts/brain.py')
brain = importlib.util.module_from_spec(spec)
spec.loader.exec_module(brain)

class ProjectionTests(unittest.TestCase):
    def setUp(self):
        self.p = json.loads((ROOT/'examples/packet.synthetic.json').read_text())
    def test_valid_packet(self):
        self.assertEqual(brain.validate(self.p), self.p)
    def test_scope_mix_rejected(self):
        self.p['claims'][0]['scope']={'tenant':'other-client','project':'demo'}
        with self.assertRaisesRegex(ValueError,'scope mismatch'): brain.validate(self.p)
    def test_source_scope_mix_rejected(self):
        self.p['sources'][0]['scope']={'tenant':'other-client','project':'demo'}
        with self.assertRaisesRegex(ValueError,'scope mismatch'): brain.validate(self.p)
    def test_missing_source_rejected(self):
        self.p['claims'][0]['citations'][0]['source_id']='missing'
        with self.assertRaisesRegex(ValueError,'missing source'): brain.validate(self.p)
    def test_no_citation_rejected(self):
        self.p['claims'][0]['citations']=[]
        with self.assertRaisesRegex(ValueError,'citations required'): brain.validate(self.p)
    def test_acceptance_not_inferred(self):
        self.p['claims'][0]['status']='accepted'
        self.p['claims'][0]['citations'][0]['evidence_type']='source_claim'
        with self.assertRaisesRegex(ValueError,'acceptance evidence'): brain.validate(self.p)
    def test_acceptance_from_projection_rejected(self):
        self.p['sources'][0]['role']='projection'
        with self.assertRaisesRegex(ValueError,'acceptance evidence'): brain.validate(self.p)
    def test_raw_private_rejected(self):
        self.p['claims'][0]['privacy']='raw_private'
        with self.assertRaisesRegex(ValueError,'only reviewed'): brain.validate(self.p)
    def test_extra_raw_payload_rejected(self):
        self.p['raw_transcript']='should not travel'
        with self.assertRaisesRegex(ValueError,'unknown fields'): brain.validate(self.p)
    def test_duplicate_claim_rejected(self):
        self.p['claims'].append(copy.deepcopy(self.p['claims'][0]))
        with self.assertRaisesRegex(ValueError,'duplicate claim'): brain.validate(self.p)
    def test_malformed_date_rejected(self):
        self.p['generated_at']='2026-13-59'
        with self.assertRaisesRegex(ValueError,'timestamp'): brain.validate(self.p)
    def test_naive_time_rejected(self):
        self.p['generated_at']='2026-10-29T12:00:00'
        with self.assertRaisesRegex(ValueError,'timezone'): brain.validate(self.p)
    def test_dangerous_links_rejected(self):
        for uri in ['javascript:alert(1)','data:text/html,test','file:///private/secret.md','https://user:pass@example.org/x','https://example.org/x?token=secret','https://example.org/private/raw.md']:
            with self.subTest(uri=uri):
                self.p['sources'][0]['uri']=uri
                with self.assertRaises(ValueError): brain.validate(self.p)
    def test_dangling_edge_rejected(self):
        self.p['edges'][0]['to']='missing'
        with self.assertRaisesRegex(ValueError,'endpoints'): brain.validate(self.p)
    def test_evidenced_edge_requires_source(self):
        self.p['edges'][0]['citations']=[]
        with self.assertRaisesRegex(ValueError,'needs citations'): brain.validate(self.p)
    def test_inferred_edge_allowed(self):
        self.p['edges'][0]['status']='inferred';self.p['edges'][0]['citations']=[]
        brain.validate(self.p)
    def test_history_not_active(self):
        self.p['claims'][0]['status']='superseded'
        result=brain.context(self.p)
        self.assertNotIn('## c1 [superseded]',result)
        self.assertIn('Historical claims excluded from active context: 2',result)
        self.assertIn('[disputed]',result)
    def test_output_deterministic(self):
        self.assertEqual(brain.render(self.p),brain.render(copy.deepcopy(self.p)))
    def test_script_termination_escaped(self):
        self.p['claims'][0]['text']='</script><script>alert(1)</script>'
        html=brain.render(self.p)
        self.assertNotIn('</script><script>alert(1)',html)
        self.assertIn('\\u003c/script',html)
    def test_no_network_or_dynamic_html(self):
        html=brain.render(self.p)
        self.assertNotIn('fetch(',html);self.assertNotIn('innerHTML',html)
        self.assertIn("connect-src 'none'",html)
        self.assertNotIn('localStorage',html)
    def test_existing_output_refused(self):
        with tempfile.TemporaryDirectory() as d:
            with self.assertRaisesRegex(ValueError,'already exists'): brain.emit(self.p,d,'render')
    def test_receipt_and_roundtrip(self):
        with tempfile.TemporaryDirectory() as d:
            out=Path(d)/'version-one';r=brain.emit(self.p,out,'render')
            self.assertFalse(r['canonical_write']);self.assertFalse(r['deployed'])
            self.assertEqual(brain.read_packet(out/'packet.json'),self.p)
            self.assertTrue((out/'index.html').is_file())
    def test_duplicate_json_key_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/'bad.json';p.write_text('{"schema":1,"schema":2}')
            with self.assertRaisesRegex(ValueError,'duplicate JSON key'): brain.read_packet(p)
    def test_graph_bound_enforced(self):
        self.p['claims'] = [copy.deepcopy(self.p['claims'][0]) for _ in range(201)]
        with self.assertRaisesRegex(ValueError,'limit 200'): brain.validate(self.p)
    def test_unknown_times_remain_unknown(self):
        self.p['claims'][0]['event_at']=None;self.p['sources'][0]['revision']=None
        text=brain.context(self.p)
        self.assertIn('Event: unknown',text);self.assertIn('revision: unknown',text)
    def test_context_preserves_coverage(self):
        self.p['coverage']['omitted_count']=123
        self.p['coverage']['access_gaps']=['Local vault was not available.']
        text=brain.context(self.p)
        self.assertIn('123',text);self.assertIn('Local vault was not available.',text)

    def test_unknown_source_locator_preserved(self):
        self.p['sources'][0].update(uri=None, observed_at=None, owner=None, access_state='provided')
        text=brain.context(self.p)
        self.assertIn('locator: unknown',text)
        self.assertIn('Synthetic owner decisions',text)
        brain.render(self.p)
    def test_unavailable_source_inventory_preserved(self):
        self.p['sources'][2].update(uri=None, observed_at=None, access_state='unavailable')
        text=brain.context(self.p)
        self.assertIn('unavailable',text)
    def test_inspected_requires_locator(self):
        self.p['sources'][0].update(uri=None, access_state='inspected')
        with self.assertRaisesRegex(ValueError,'inspected source needs'): brain.validate(self.p)
    def test_relation_evidence_and_historical_identity_preserved(self):
        text=brain.context(self.p)
        self.assertIn('## c2 [accepted]',text)
        self.assertIn('c5 (Old dashboard direction; superseded)',text)
        self.assertIn('Relation evidence: Synthetic owner decisions',text)
        self.assertIn('Synthetic relation supersedes',text)

if __name__=='__main__': unittest.main()
