# GitHub Publishing Guide — OS Lab v3.0

This is a **local Git workflow**. The assistant prepared the files but has not authenticated to the owner's GitHub account or pushed any commits. The exact OS Lab repository URL was not supplied, so commands below use an explicit placeholder. Do not use the separate CodeBreak repository as the target.

## A. Choose repository scope

- Recommended repo name (only if creating a new one): `os-lab`.
- Decide **public or private** when creating the GitHub repository. The docs contain no real secrets, but publication is an owner decision.
- The prepared project contains **no LICENSE** because no license was specified.
- Do not upload private progress JSON, personal browser profiles, `.env`, tokens, or secrets.

## B. Safest path: new empty GitHub repository

1. Sign in to GitHub and select **New repository**.
2. Choose the repository name, e.g. `os-lab`, choose visibility, and click **Create repository**.
3. **Do not initialize** the new repo with README, `.gitignore`, or license; this package already provides a README and `.gitignore`.
4. Copy the repository's HTTPS URL from **Code**.
5. On Ubuntu, first extract the provided GitHub-ready ZIP:

```bash
cd ~/Downloads
mkdir -p ~/Documents/os-lab-release
unzip OS_Lab_v3.0_Final_GitHub_Ready.zip -d ~/Documents/os-lab-release
cd ~/Documents/os-lab-release/os-lab
```

6. Verify files and run the checks:

```bash
ls -la
python3 scripts/verify_release.py
git --version
```

7. Initialize locally and commit:

```bash
git init -b main
git status
git add .
git diff --cached --stat
git commit -m "docs: publish OS Lab v3 user and developer manuals"
```

8. Add the URL copied from GitHub and push:

```bash
git remote add origin <REPOSITORY_URL>
git remote -v
git push -u origin main
```

**Replace `<REPOSITORY_URL>`**, including its angle brackets, with the actual HTTPS URL. Do **not** use a guessed link. GitHub may request browser authorization or a credential manager. Never paste a token into chat or hardcode one in the URL.

9. Open your repository page and verify `README.md`, `docs/USER_MANUAL.md`, `docs/DEVELOPER_MANUAL.md`, scripts and screenshots appear.

10. Optional, after confirming the repository is correct:

```bash
git tag -a v3.0.0-docs -m "OS Lab v3.0 accepted documentation baseline"
git push origin v3.0.0-docs
```

## C. Existing GitHub OS Lab repository

If an OS Lab repo already exists, **do not use `git init` in a random copy and force-push it.** Clone the real repo and add or replace only files you intend to publish:

```bash
cd ~/Documents
git clone <EXISTING_OS_LAB_REPO_URL>
cd <CLONED_OS_LAB_REPO_DIR>
git switch -c docs/v3-manuals
```

Copy the contents of the prepared `os-lab/` release into that cloned repo after examining existing files. You can use your graphical file manager or `cp -a <EXTRACTED_OS_LAB_DIRECTORY>/. .` **only after reviewing potential overwrite conflicts**. If the existing repository's application files differ, investigate and avoid overwriting until versions match.

Then:

```bash
git status
git diff --stat
git add README.md docs scripts
# Add application files only if this repository does not already contain the matching build.
git commit -m "docs: add OS Lab v3 user and developer manuals"
git push -u origin docs/v3-manuals
```

Open a pull request from `docs/v3-manuals` to `main`, review changes, and merge using GitHub. This route protects the previous history and release.

## D. Git commands explained

| Command | Purpose |
| --- | --- |
| `git init -b main` | Create a **new local** repository using `main` |
| `git status` | Show staged and unstaged changes |
| `git add .` | Stage all unignored files within the current project |
| `git diff --cached --stat` | Show a summary of staged changes |
| `git commit -m "..."` | Record a **local** commit |
| `git remote add origin URL` | Configure the GitHub target for a new local repo |
| `git push -u origin main` | Publish `main` and set its upstream |
| `git pull --ff-only` | Integrate compatible upstream changes without an automatic merge commit |
| `git clone URL` | Download a repository with its history |

A local `git commit` alone does not upload anything. A successful `git push` does.

## E. Troubleshooting GitHub publishing

- `Author identity unknown`: configure identity with `git config --global user.name "Your Name"` and `git config --global user.email "you@example.com"` (use your own values).
- `remote origin already exists`: check `git remote -v`, do not blindly add another remote. If wrong, confirm the correct URL before using `git remote set-url origin ...`.
- `Repository not found`: verify URL spelling, privacy/access, GitHub login and repository existence.
- `Permission denied (publickey)`: likely an SSH-key issue. Use the repository HTTPS URL or configure SSH authorization.
- `Authentication failed`: GitHub HTTPS Git operations typically use an approved credential manager or personal access token rather than account password. Follow the current GitHub authentication prompts, and keep credentials private.
- `rejected (non-fast-forward)`: the GitHub branch has commits you don't have. **Do not force push**. Use the existing-repo clone/PR workflow, or reconcile changes with `git fetch` and a review.
- `src refspec main does not match any`: create at least one commit and check your branch name (`git branch --show-current`).
- `nothing to commit`: the intended changes may already be committed; check `git log -1 --oneline` and `git status`.
- `fatal: not a git repository`: change into the actual repo folder containing `.git`.

## F. GitHub download instructions for future readers

Once pushed, the User Manual and root README explain **Code → Download ZIP**, `git clone`, extraction, opening `index.html`, and backups. Copy the real repository URL into your GitHub About/description or repository README after publication if desired. This package intentionally avoids a fabricated link.
