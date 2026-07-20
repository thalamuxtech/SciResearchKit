/**
 * SciResearchKit VS Code extension.
 *
 * Loads the bundled Markdown corpus (mirrored at build time from the repo
 * root by scripts/sync-content.js into dist/data/) and exposes commands
 * to insert or open it inside the editor.
 *
 * The extension does no network I/O and reads only from its own
 * extension directory.
 */

import * as fs from 'fs';
import * as path from 'path';
import * as vscode from 'vscode';

let extensionRoot = '';

function dataDir(): string {
  return path.join(extensionRoot, 'dist', 'data');
}

function readData(relPath: string): string {
  const target = path.join(dataDir(), relPath);
  if (!fs.existsSync(target)) {
    throw new Error(`SciResearchKit: bundled resource not found: ${relPath}`);
  }
  return fs.readFileSync(target, 'utf8');
}

function listMarkdownSlugs(subdir: string): string[] {
  const dir = path.join(dataDir(), subdir);
  if (!fs.existsSync(dir)) return [];
  return fs
    .readdirSync(dir)
    .filter((name) => name.endsWith('.md'))
    .map((name) => name.slice(0, -3))
    .sort();
}

function systemPrompt(includeEthics: boolean): string {
  const skill = readData('SKILL.md');
  if (!includeEthics) return skill;
  const ethics = readData('ETHICS.md');
  return `${skill}\n\n---\n\n${ethics}`;
}

async function openMarkdownDocument(content: string, hint: string): Promise<void> {
  const doc = await vscode.workspace.openTextDocument({
    language: 'markdown',
    content,
  });
  await vscode.window.showTextDocument(doc, { preview: false });
  vscode.window.setStatusBarMessage(`SciResearchKit: opened ${hint}`, 3000);
}

async function insertAtCursor(content: string): Promise<void> {
  const editor = vscode.window.activeTextEditor;
  if (!editor) {
    await openMarkdownDocument(content, 'system prompt');
    return;
  }
  await editor.edit((edit) => {
    edit.insert(editor.selection.active, content);
  });
}

async function pickAndOpen(subdir: string, kind: string): Promise<void> {
  const slugs = listMarkdownSlugs(subdir);
  if (slugs.length === 0) {
    vscode.window.showErrorMessage(
      `SciResearchKit: no ${kind} files bundled with this extension.`,
    );
    return;
  }
  const picked = await vscode.window.showQuickPick(slugs, {
    placeHolder: `Choose a SciResearchKit ${kind}`,
  });
  if (!picked) return;
  const content = readData(`${subdir}/${picked}.md`);
  await openMarkdownDocument(content, `${kind} ${picked}`);
}

export function activate(context: vscode.ExtensionContext): void {
  extensionRoot = context.extensionPath;

  context.subscriptions.push(
    vscode.commands.registerCommand('sciresearchkit.insertSystemPrompt', async () => {
      try {
        await insertAtCursor(systemPrompt(true));
      } catch (err) {
        vscode.window.showErrorMessage(String(err));
      }
    }),

    vscode.commands.registerCommand('sciresearchkit.copySystemPromptToClipboard', async () => {
      try {
        await vscode.env.clipboard.writeText(systemPrompt(true));
        vscode.window.showInformationMessage(
          'SciResearchKit: system prompt copied to clipboard.',
        );
      } catch (err) {
        vscode.window.showErrorMessage(String(err));
      }
    }),

    vscode.commands.registerCommand('sciresearchkit.openSkill', async () => {
      try {
        await openMarkdownDocument(readData('SKILL.md'), 'SKILL.md');
      } catch (err) {
        vscode.window.showErrorMessage(String(err));
      }
    }),

    vscode.commands.registerCommand('sciresearchkit.openEthics', async () => {
      try {
        await openMarkdownDocument(readData('ETHICS.md'), 'ETHICS.md');
      } catch (err) {
        vscode.window.showErrorMessage(String(err));
      }
    }),

    vscode.commands.registerCommand('sciresearchkit.openReference', async () => {
      await pickAndOpen('references', 'reference');
    }),

    vscode.commands.registerCommand('sciresearchkit.openTemplate', async () => {
      await pickAndOpen('templates', 'template');
    }),
  );
}

export function deactivate(): void {
  /* nothing to clean up */
}
