#!/usr/bin/env python3
"""Meaningful preview contract and projection tests. No remote writes or LLM calls."""
import copy
from datetime import datetime, timedelta, timezone
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import unittest

ROOT=Path(__file__).resolve().parents[1]
SKILL=ROOT/'skills/substrate/starlight-practice-integration'
spec=importlib.util.spec_from_file_location('bridge',SKILL/'scripts/session_bridge.py')
bridge=importlib.util.module_from_spec(spec);spec.loader.exec_module(bridge)
NOW=datetime(2026,9,9,12,tzinfo=timezone.utc)

class BridgeTests(unittest.TestCase):
    def setUp(self):
        self.s=json.loads((SKILL/'references/session-example.json').read_text())
    def run_preview(self,session=None,**kwargs):
        return bridge.preview(self.s if session is None else session,tenant_id=kwargs.get('tenant','demo'),workspace_id='practice',now=NOW)
    def memory(self):
        self.s['permissions']['memory']=True
        self.s['memory']={'summary':'I want to create a welcoming garden workshop.','approved_summary':'I want to create a welcoming garden workshop.','consent_at':NOW.isoformat(),'retention_days':30,'destination':'sis/local_core'}
    def test_no_implicit_memory(self):
        p=self.run_preview();self.assertIsNone(p['memory_record']);self.assertEqual(p['side_effects'],[])
    def test_draft_is_bounded(self):
        p=self.run_preview()['agent_envelope'];self.assertEqual(p['scope'],'draft_only');self.assertFalse(p['external_actions_allowed']);self.assertEqual(p['max_minutes'],20)
    def test_declining_drafts_still_allows_reflection(self):
        self.s['permissions']['draft']=False;self.assertIsNone(self.run_preview()['agent_envelope'])
    def test_not_returned(self):
        for state in ['practicing','immersed','stopped',None]:
            with self.subTest(state=state),self.assertRaises(bridge.ContractError):
                self.s['state']=state;self.run_preview()
    def test_discomfort_blocks_integration(self):
        self.s['comfortable']=False
        with self.assertRaises(bridge.ContractError): self.run_preview()
    def test_disorientation_blocks_integration(self):
        self.s['oriented']=False
        with self.assertRaises(bridge.ContractError): self.run_preview()
    def test_strings_and_numbers_are_not_consent(self):
        for value in ['true',1,None]:
            with self.subTest(value=value),self.assertRaises(bridge.ContractError):
                self.s['permissions']['memory']=value;self.run_preview()
    def test_unapproved_journal_payload_rejected(self):
        self.s['raw_journal']='private data'
        with self.assertRaises(bridge.ContractError): self.run_preview()
    def test_unconsented_memory_payload_rejected(self):
        self.s['memory']={'summary':'private'}
        with self.assertRaises(bridge.ContractError): self.run_preview()
    def test_request_cannot_set_tenant(self):
        self.s['tenant_id']='another-user'
        with self.assertRaises(bridge.ContractError): self.run_preview()
    def test_reviewed_memory_is_minimal_private_and_expiring(self):
        self.memory();p=self.run_preview();r=p['memory_record']
        self.assertEqual(r['privacy_class'],'private');self.assertEqual(r['memory_type'],'aspirational')
        self.assertNotIn('raw_content',r);self.assertEqual(p['memory_policy'],{'tenant_id':'demo','local_only':True})
        self.assertEqual(r['retention_until'],(NOW+timedelta(days=30)).isoformat())
        self.assertNotIn('memory',p['agent_envelope']);self.assertNotIn(self.s['memory']['summary'],json.dumps(p['agent_envelope']))
    def test_summary_change_requires_new_approval(self):
        self.memory();self.s['memory']['summary']='Another summary'
        with self.assertRaises(bridge.ContractError): self.run_preview()
    def test_stale_or_future_consent_rejected(self):
        self.memory()
        for hours in [-25,1]:
            with self.subTest(hours=hours),self.assertRaises(bridge.ContractError):
                self.s['memory']['consent_at']=(NOW+timedelta(hours=hours)).isoformat();self.run_preview()
    def test_other_destination_rejected(self):
        self.memory();self.s['memory']['destination']='public-github'
        with self.assertRaises(bridge.ContractError): self.run_preview()
    def test_cross_tenant_memory_ids_differ(self):
        self.memory();a=self.run_preview();b=self.run_preview(tenant='second')
        self.assertNotEqual(a['memory_record']['memory_id'],b['memory_record']['memory_id'])
    def test_retry_has_same_id_and_no_input_mutation(self):
        self.memory();before=copy.deepcopy(self.s);a=self.run_preview();b=self.run_preview()
        self.assertEqual(a,b);self.assertEqual(before,self.s)
    def test_invalid_timeboxes(self):
        for value in [True,0,61,'20']:
            with self.subTest(value=value),self.assertRaises(bridge.ContractError):
                self.s['action']['timebox_minutes']=value;self.run_preview()
    def test_action_scope_cannot_escalate(self):
        self.s['action']['publish']=True
        with self.assertRaises(bridge.ContractError): self.run_preview()
    def test_plugin_matches_source(self):
        subprocess.run([sys.executable,str(ROOT/'scripts/build_golden_age_plugin.py'),'--check'],check=True,capture_output=True)
    def test_marketplace_resolves(self):
        m=json.loads((ROOT/'.claude-plugin/marketplace.json').read_text())
        entry=next(x for x in m['plugins'] if x['name']=='starlight-golden-age')
        folder=ROOT/entry['source'];self.assertTrue(folder.is_dir())
        for kind in ['.claude-plugin','.codex-plugin']:
            p=json.loads((folder/kind/'plugin.json').read_text());self.assertEqual(p['name'],folder.name);self.assertEqual(p['version'],'0.1.0')

if __name__=='__main__':unittest.main()
