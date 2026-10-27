#!/usr/bin/env python3
"""OS Lab documentation-release verifier: stdlib-only static/source checks.

This does NOT replace browser functional tests. It never evaluates app JS.
"""
from pathlib import Path
import hashlib, shutil, subprocess, re, sys
root=Path(__file__).resolve().parents[1]
errors=[]
def check(condition, message):
    print(('PASS' if condition else 'FAIL')+'  '+message)
    if not condition: errors.append(message)
files=['index.html','style.css','app.js','stages2-6.js','stages7-8.js','engineering.js']
for f in files: check((root/f).is_file(), 'required runtime file: '+f)
for f in ['docs/USER_MANUAL.md','docs/DEVELOPER_MANUAL.md','docs/GITHUB_PUBLISHING.md','docs/RELEASE_CHECKLIST.md','README.md']:
    check((root/f).is_file(), 'required manual/release file: '+f)
html=(root/'index.html').read_text(encoding='utf-8')
order=re.findall(r'<script\s+src="([^"]+)"',html)
check(order==['app.js','stages2-6.js','stages7-8.js','engineering.js'], 'ordered scripts match v3 baseline')
for ref in re.findall(r'(?:src|href)="([^"]+)"',html):
    if ref.startswith(('http:','https:','#','data:')): errors.append('unexpected external/local reference: '+ref)
    else: check((root/ref).is_file(),'entry HTML dependency: '+ref)
if (root/'stages7-8.js').exists():
    cases=set(re.findall(r'"slug":\s*"case(\d+)"',(root/'stages7-8.js').read_text(encoding='utf-8')))
    check(cases=={str(i) for i in range(17,61)},'44 numbered Stage 8 cases (case17-case60) present')
if (root/'engineering.js').exists():
    e=(root/'engineering.js').read_text(encoding='utf-8')
    check('oslab-v3-engineering-v1' in e and 'OSLabEngineeringTest' in e,'v3 history key and test hook present')
if (root/'app.js').exists():
    check("oslab-stage1-v1" in (root/'app.js').read_text(encoding='utf-8'),'legacy course progress key preserved')
manifest=root/'docs'/'BASELINE_SHA256.txt'
if manifest.is_file():
    for line in manifest.read_text(encoding='utf-8').splitlines():
        if not line or line.startswith('#'): continue
        parts=line.split('  ',1)
        if len(parts)!=2: errors.append('malformed hash line: '+line);continue
        digest,filename=parts
        target=root/filename
        check(target.is_file() and hashlib.sha256(target.read_bytes()).hexdigest()==digest,'baseline SHA-256: '+filename)
else: errors.append('baseline hash manifest missing')
node=shutil.which('node')
if node:
    for f in ['app.js','stages2-6.js','stages7-8.js','engineering.js']:
        if not (root/f).is_file():continue
        proc=subprocess.run([node,'--check',str(root/f)],capture_output=True,text=True)
        check(proc.returncode==0, 'node syntax: '+f)
        if proc.returncode: print(proc.stderr)
else: print('SKIP  Node.js not installed; optional syntax checks skipped')
print('\n'+('FAILED' if errors else 'PASS')+': '+str(len(errors))+' issue(s). Reminder: static checks do not confirm browser behavior.')
sys.exit(bool(errors))
