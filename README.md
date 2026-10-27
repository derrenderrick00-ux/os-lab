# OS Lab v3.0 — Offline Operating Systems Academy

**Release status:** User-accepted engineering build, feature-frozen pending future notice.  
**Platforms:** Ubuntu / other desktop Linux distributions / Windows, in a compatible local browser.  
**Runtime:** Offline HTML, CSS, JavaScript. No npm, Node.js, web server, or account required to **run** the application.  
**Safety:** All terminal commands are simulated. They do not invoke real shell commands or change real operating-system settings.

![OS Lab virtual desktop](docs/assets/virtual-desktop.png)

## Start here

- **[User Manual](docs/USER_MANUAL.md):** GitHub download, first launch, lessons, virtual desktop, three simulated shells, troubleshooting, assessments, backup/restore, and FAQs.
- **[Developer Manual](docs/DEVELOPER_MANUAL.md):** source architecture, data flow, saved state, release history, CLI and scenario semantics, limitations, maintenance, verification, and reproducibility.
- **[GitHub Publishing Guide](docs/GITHUB_PUBLISHING.md):** create/clone a repo and commit/push safely.
- **[Release Checklist](docs/RELEASE_CHECKLIST.md):** manual acceptance and static checks.
- **[Engineering Notes](ENGINEERING_NOTES.md):** original limitations statement, kept unchanged.

## Download from GitHub (once this project has been pushed)

1. Open the **OS Lab repository** on GitHub. Its exact URL will be available after the owner creates/publishes the repository.
2. Click **Code → Download ZIP**, then extract the ZIP. Alternatively, use `git clone <REPOSITORY_URL>`.
3. Open the extracted repository's `index.html` in Firefox or another compatible desktop browser.

Ubuntu quick start after cloning:

```bash
git clone <REPOSITORY_URL>
cd <CLONED_REPOSITORY_DIRECTORY>
xdg-open index.html
```

Windows: extract the repository ZIP and **double-click `index.html`**, or in PowerShell run `Start-Process .\index.html` from its folder.

> Placeholder values in angle brackets are **not literal commands**: replace them with the URL/directory of the published repo. No repository URL has been assigned in these documents.

## Features

- 12 learning modules following a nine-step study pattern.
- Virtual desktop, file viewer, process/system monitor, and safe practice terminal.
- 60 selectable legacy troubleshooting scenarios (not all offer unique native-CLI repairs).
- Boot, scheduling, memory, files, devices, networking, virtualization, and mini-OS educational simulators.
- Separate Engineering Lab with Ubuntu Bash-like, Windows CMD-like, and PowerShell-like **simulated** command subsets.
- Guided, independent, and examination assessments; local scores/attempt history.
- Learning progress export/import, and separate assessment-history export.

## Release qualification

The supplied v3.0 engineering build was exercised by the project owner on Ubuntu and reported passing user tests. This repository documentation does **not** claim Windows browser validation, full test coverage, or true OS/kernel virtualization. Original v2.0.1 behavior is retained; the Engineering Lab is an additional isolated simulator, not a single state shared with every older pane. The 60 Engineering Lab selections largely use category-based fault templates.

## Development checks (optional)

```bash
python3 scripts/verify_release.py
```

Node.js is optional for users but recommended for development (`node --check` validates JavaScript syntax). The script performs structural checks and syntax checks when Node.js is present; it is **not** a full automated browser test suite.

## Data handling

Learning progress is stored in browser `localStorage` under `oslab-stage1-v1`; Engineering Lab attempt history under `oslab-v3-engineering-v1`. Export both datasets **separately** before clearing browser data or moving computers. Virtual machine state resets when a scenario is restarted or the page reloads. See the User Manual.

## Licensing

No open-source license has been chosen or granted by these documentation changes. The repository owner should select and add a license only if they intend to grant reuse rights.
