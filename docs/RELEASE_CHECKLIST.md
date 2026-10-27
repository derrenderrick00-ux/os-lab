# OS Lab v3.0 — Release Verification Checklist

## A. Static/source verification

- [ ] `python3 scripts/verify_release.py` passes.
- [ ] All 4 runtime JS files pass `node --check` (when Node installed).
- [ ] Script tags stay in order: app, stages2-6, stages7-8, engineering.
- [ ] Baseline hashes match `docs/BASELINE_SHA256.txt` (documentation-only release).
- [ ] No external runtime dependencies added.
- [ ] `git status` shows only intended files before commit.

## B. Ubuntu functional acceptance

- [ ] Open `index.html` from local file URL (not solely a development server).
- [ ] No blocking Console exceptions.
- [ ] All 12 lesson buttons navigate to actual content.
- [ ] Module 11 shows virtualization and kernel architecture components.
- [ ] Module 12 mini-OS workbench completes health check.
- [ ] Virtual Desktop Terminal, Files, System Monitor and Settings work.
- [ ] Original Troubleshooting case17 can be inspected, repaired, verified and reset.
- [ ] Original Troubleshooting scenario count shows 60.
- [ ] Engineering Lab button and scenario/mode/shell selectors work.
- [ ] Engineering Lab DNS scenario repairs and verifies through separate commands.
- [ ] CMD and PowerShell simulated commands return output.
- [ ] At least one guided and one exam assessment can be submitted.
- [ ] Engineering Lab scores survive browser refresh.
- [ ] Course completion data survives refresh.
- [ ] Course JSON export/import functions; Engineering Lab assessment JSON exports.
- [ ] Browser stays functional with no Internet connection.

## C. Windows acceptance (not claimed by documentation pack)

- [ ] ZIP extracted and `index.html` opened from Explorer.
- [ ] Same core/advanced/engineering flows pass on a Windows desktop browser.
- [ ] Progress import tested on a different browser/device.

## D. Release integrity

- [ ] GitHub repo owner and URL confirmed.
- [ ] Repository visibility chosen deliberately.
- [ ] No private backups, passwords, tokens or API keys included.
- [ ] `README.md`, both manuals, publishing guide and images display correctly in GitHub.
- [ ] Branch merged or pushed without force; tag created only if desired.

## Known limitations not to misrepresent

- Simulated CLI command subsets are not full Bash, CMD or PowerShell.
- Legacy and Engineering Lab machines are not one globally shared state.
- Most Engineering Lab cases reuse a category-level fault mechanism.
- Diagnosis scoring is simplified and not valid as official certification.
- Engineering Lab assessment export currently lacks in-app import.
- This pack does not independently certify Windows performance or comprehensive browser automation.
