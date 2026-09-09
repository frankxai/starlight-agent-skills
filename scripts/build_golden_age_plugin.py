#!/usr/bin/env python3
"""Build or check the three-skill Golden Age package from canonical repo sources."""
from pathlib import Path
import argparse
import shutil

ROOT=Path(__file__).resolve().parents[1]
PLUGIN=ROOT/'plugins/starlight-golden-age'
SOURCES=('education/starlight-practice-preparation','education/starlight-golden-age','substrate/starlight-practice-integration')

def expected():
    result={}
    for source in SOURCES:
        folder=ROOT/'skills'/source
        for p in folder.rglob('*'):
            if p.is_file() and '__pycache__' not in p.parts and p.suffix != '.pyc':
                result[Path(folder.name)/p.relative_to(folder)]=p.read_bytes()
    return result

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--check',action='store_true');args=parser.parse_args()
    files=expected();target=PLUGIN/'skills'
    if args.check:
        actual={p.relative_to(target):p.read_bytes() for p in target.rglob('*') if p.is_file() and '__pycache__' not in p.parts and p.suffix != '.pyc'}
        if actual != files:
            raise SystemExit('Golden Age plugin differs from canonical sources; rebuild it.')
        print(f'Golden Age projection matches: {len(files)} files, 3 skills.')
    else:
        if target.is_symlink() or target.resolve().parent != PLUGIN.resolve():
            raise SystemExit('Unexpected plugin target')
        if target.exists(): shutil.rmtree(target)
        for path,data in files.items():
            p=target/path;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(data)
        print(f'Built Golden Age plugin: {len(files)} files.')
if __name__=='__main__': main()
