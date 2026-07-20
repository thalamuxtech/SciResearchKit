# Publishing SciResearchKit

Step-by-step release instructions for the two distributions. Do the one-time setup once per registry; after that, releases are one `git tag && git push --tags`.

Both flows use GitHub Actions workflows already in the repo:

- `.github/workflows/publish-pypi.yml` — Trusted Publishing to PyPI (no token stored anywhere)
- `.github/workflows/publish-vscode.yml` — VS Code Marketplace publish via `vsce`

---

## 1. Push the packaging changes to GitHub

The repo is already initialised with `origin` pointing at
https://github.com/thalamuxtech/SciResearchKit and has one commit on
`main`. Ship the packaging + logo work as a second commit:

```bash
cd C:/Users/ismailukman/Downloads/ResearchPapers/SciResearchKit

# Sanity check first — expect only the files listed in "Files touched"
# at the bottom of the last chat reply. If you see anything unexpected
# (build outputs, node_modules, __pycache__), fix .gitignore before
# staging.
git status

git add .
git commit -m "Add PyPI + VS Code packages, ethics notice, clean-traced SVG logo"
git push
```

Confirm the two workflows show up under the repo's **Actions** tab after
the push completes.

---

## 2. PyPI: one-time setup, then release on tag

### 2a. Create the PyPI project via Trusted Publishing

You do NOT create the project first on the PyPI website. You configure a **pending publisher**, and PyPI creates the project on the first successful upload.

1. Sign in to <https://pypi.org>.
2. Go to <https://pypi.org/manage/account/publishing/>.
3. Under **Add a new pending publisher**, choose **GitHub** and enter:
   - **PyPI project name**: `sciresearchkit`
   - **Owner**: `thalamuxtech`
   - **Repository name**: `SciResearchKit`
   - **Workflow name**: `publish-pypi.yml`
   - **Environment name**: `pypi`
4. Save.

### 2b. Create the `pypi` environment on GitHub

The workflow file requires an environment named `pypi` (so you get a review gate before every publish).

1. GitHub → repo → **Settings** → **Environments** → **New environment** → name it `pypi`.
2. Under **Deployment protection rules**, tick **Required reviewers** and add your own GitHub account (so a real person clicks Approve before publish).
3. Save.

### 2c. Release

```bash
cd C:/Users/ismailukman/Downloads/ResearchPapers/SciResearchKit

# Bump the version in packaging/pypi/pyproject.toml (already 0.1.0 for first release)
# Then:
git tag pypi-v0.1.0
git push --tags
```

That triggers `publish-pypi.yml`:

1. Tests run on Python 3.9 / 3.11 / 3.13.
2. Wheel + sdist build; `twine check` runs.
3. Waits at the `pypi` environment gate → you click **Approve** on GitHub.
4. Publish job assumes the OIDC identity that PyPI trusts (no token) and uploads to <https://pypi.org/project/sciresearchkit/>.

After it finishes, verify:

```bash
pip install sciresearchkit
sciresearchkit --version
sciresearchkit ethics | head -20
```

### 2d. Subsequent releases

Bump `version` in `packaging/pypi/pyproject.toml`, commit, then:

```bash
git tag pypi-v0.2.0
git push --tags
```

---

## 3. VS Code Marketplace: one-time setup, then release on tag

Docs: <https://code.visualstudio.com/api/working-with-extensions/publishing-extension>.

### 3a. Create an Azure DevOps organisation (if you don't have one)

The Marketplace uses Azure DevOps for auth.

1. Go to <https://dev.azure.com>.
2. Sign in with a Microsoft account (personal or work).
3. Create an organisation (the name doesn't matter; it's just where the token lives). You can name it anything, e.g. `ismailukman-vsce`.

### 3b. Generate a Personal Access Token (PAT)

1. In your Azure DevOps org → top-right avatar → **Personal Access Tokens**.
2. **New Token** with:
   - **Name**: `vsce-publish`
   - **Organization**: **All accessible organizations**
   - **Expiration**: 1 year (or your policy's max)
   - **Scopes** → **Custom defined** → check **Marketplace: Manage** (only).
3. Copy the token — you cannot see it again.

### 3c. Create the Marketplace publisher

1. Go to <https://marketplace.visualstudio.com/manage/createpublisher>.
2. **Publisher ID**: `ismailukman` (this matches `publisher` in `packaging/vscode/package.json`).
3. **Publisher name**: whatever the marketplace page should display (e.g. `Lukman E. Ismaila`).
4. Save.

### 3d. Add the PAT as a GitHub secret

1. GitHub → repo → **Settings** → **Secrets and variables** → **Actions** → **New repository secret**.
2. **Name**: `VSCE_PAT`.
3. **Secret**: paste the PAT from step 3b.
4. Save.

### 3e. Release

```bash
cd C:/Users/ismailukman/Downloads/ResearchPapers/SciResearchKit

# Bump version in packaging/vscode/package.json (already 0.1.0 for first release)
git tag vscode-v0.1.0
git push --tags
```

That triggers `publish-vscode.yml`:

1. `npm ci` + TypeScript compile + `sync-content` mirrors the Markdown corpus into `dist/data/`.
2. `vsce package` builds the VSIX.
3. `vsce publish` uploads to the Marketplace using `VSCE_PAT`.

After it finishes, verify:

- Extension page: `https://marketplace.visualstudio.com/items?itemName=ismailukman.sciresearchkit`
- Install in VS Code: press `Ctrl+P`, then `ext install ismailukman.sciresearchkit`
- Confirm the six commands appear in the palette under "SciResearchKit:".

### 3f. Subsequent releases

Bump `version` in `packaging/vscode/package.json`, commit, then:

```bash
git tag vscode-v0.2.0
git push --tags
```

---

## 4. Manual release (fallback, if a workflow is broken)

### PyPI (manual)

```bash
cd C:/Users/ismailukman/Downloads/ResearchPapers/SciResearchKit/packaging/pypi

python -m build                         # rebuild dist/
python -m twine check dist/*            # sanity check

# One-time: create a PyPI API token at https://pypi.org/manage/account/token/
# Save it in ~/.pypirc or as $TWINE_PASSWORD (username = __token__).
python -m twine upload dist/*
```

### VS Code Marketplace (manual)

```bash
cd C:/Users/ismailukman/Downloads/ResearchPapers/SciResearchKit/packaging/vscode

npm ci
npm run compile
npx @vscode/vsce package --out sciresearchkit.vsix

# One-time: `vsce login ismailukman` (paste the PAT once, it caches).
npx @vscode/vsce publish --packagePath sciresearchkit.vsix
```

---

## 5. Version-bump cheatsheet

| Change | File(s) to bump | Then |
|---|---|---|
| Only Markdown content (SKILL.md, references/, templates/) | `packaging/pypi/pyproject.toml` and `packaging/vscode/package.json` | Release both packages so they ship the same content |
| Only Python API changes | `packaging/pypi/pyproject.toml` | Release PyPI |
| Only extension code changes | `packaging/vscode/package.json` | Release VS Code |

Semver reminder: **patch** for bug fixes, **minor** for new backwards-compatible features, **major** for breaking changes to the Python API or the extension commands.

---

## 6. Common pitfalls

- **PyPI Trusted Publishing configured before first upload**: you don't create the project manually first. Add the pending publisher and let the first workflow run create it.
- **VS Code publisher ID vs display name**: the `publisher` field in `package.json` is the **ID** (used in the extension URL). The display name is set in the Marketplace publisher profile and can be different.
- **VSIX shipped without the Markdown corpus**: the `sync-content` script runs as part of `npm run compile`. If you package with `vsce package` without running `compile` first, `dist/data/` will be empty. The GitHub workflow runs both in the right order.
- **SVG in a marketplace README**: PyPI and the VS Code Marketplace both strip SVG images from README content (security policy). Use `srk_logo_hero.png` for those READMEs; the master `README.md` on GitHub can use `srk_logo_animated.svg`.
