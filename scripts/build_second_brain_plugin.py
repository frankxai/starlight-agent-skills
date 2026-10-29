#!/usr/bin/env python3
"""Compile the six canonical Second Brain skills; --check detects byte drift."""
import argparse, pathlib, shutil, sys
R=pathlib.Path(__file__).resolve().parents[1]
NAMES=['run-second-brain', 'distill-brain-sources', 'reconcile-brain-decisions', 'reflect-on-knowledge', 'visualize-knowledge', 'compile-brain-context']
a=argparse.ArgumentParser();a.add_argument('--check',action='store_true');args=a.parse_args()
target=R/'plugins/starlight-second-brain/skills'
expected={}
for name in NAMES:
 for p in (R/'skills/substrate'/name).rglob('*'):
  if p.is_file() and '__pycache__' not in p.parts and p.suffix!='.pyc':
   expected[str(pathlib.Path(name)/p.relative_to(R/'skills/substrate'/name))]=p.read_bytes()
actual={str(p.relative_to(target)):p.read_bytes() for p in target.rglob('*') if p.is_file() and '__pycache__' not in p.parts and p.suffix!='.pyc'} if target.exists() else {}
if args.check:
 if actual!=expected: sys.exit('Second Brain projection is stale')
else:
 if target.exists(): shutil.rmtree(target)
 for rel,data in expected.items():
  p=target/rel;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(data)
print('Second Brain projection current: '+str(len(expected))+' files, six skills')
