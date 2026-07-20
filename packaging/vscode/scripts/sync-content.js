/**
 * Mirror the canonical toolkit Markdown into the extension's dist tree.
 *
 * Runs at compile time (npm run compile) and again at package/publish time
 * so the VSIX ships an offline, versioned copy of SKILL.md, ETHICS.md, the
 * reference files, and the templates. Idempotent.
 */

const fs = require('fs');
const path = require('path');

const REPO_FILES = ['SKILL.md', 'ETHICS.md'];
const REPO_DIRS = ['references', 'templates'];

function findRepoRoot(startDir) {
  let dir = path.resolve(startDir);
  while (true) {
    const skill = path.join(dir, 'SKILL.md');
    const refs = path.join(dir, 'references');
    if (fs.existsSync(skill) && fs.existsSync(refs) && fs.statSync(refs).isDirectory()) {
      return dir;
    }
    const parent = path.dirname(dir);
    if (parent === dir) return null;
    dir = parent;
  }
}

function copyMarkdown(sourceDir, targetDir) {
  if (!fs.existsSync(targetDir)) fs.mkdirSync(targetDir, { recursive: true });
  for (const name of fs.readdirSync(sourceDir).sort()) {
    if (!name.endsWith('.md')) continue;
    fs.copyFileSync(path.join(sourceDir, name), path.join(targetDir, name));
  }
}

function main() {
  const extensionDir = path.resolve(__dirname, '..');
  const repoRoot = findRepoRoot(extensionDir);
  if (!repoRoot) {
    console.error(
      'sync-content: could not find repo root (containing SKILL.md and references/) ' +
        `above ${extensionDir}. Run the build from a checkout of SciResearchKit.`,
    );
    process.exit(1);
  }

  const dataDir = path.join(extensionDir, 'dist', 'data');
  if (fs.existsSync(dataDir)) {
    fs.rmSync(dataDir, { recursive: true, force: true });
  }
  fs.mkdirSync(dataDir, { recursive: true });

  for (const name of REPO_FILES) {
    const source = path.join(repoRoot, name);
    if (fs.existsSync(source)) {
      fs.copyFileSync(source, path.join(dataDir, name));
    }
  }

  for (const dir of REPO_DIRS) {
    const source = path.join(repoRoot, dir);
    if (fs.existsSync(source) && fs.statSync(source).isDirectory()) {
      copyMarkdown(source, path.join(dataDir, dir));
    }
  }

  console.log(`sync-content: mirrored toolkit content from ${repoRoot} -> ${dataDir}`);
}

main();
