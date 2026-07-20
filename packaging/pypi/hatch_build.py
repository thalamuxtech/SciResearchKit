"""Custom Hatch build hook.

The canonical toolkit content (SKILL.md, ETHICS.md, references/*.md,
templates/*.md) lives at the repository root. To ship it inside the
Python wheel and sdist without maintaining two copies, this hook mirrors
the Markdown files into ``src/sciresearchkit/data/`` before the build
backend collects sources.

Idempotent: running the build twice does not duplicate or drift the
mirror. Deletes stale entries so a removed reference file does not
linger in a later release.
"""

from __future__ import annotations

import shutil
from pathlib import Path

from hatchling.builders.hooks.plugin.interface import BuildHookInterface


REPO_TOOLKIT_FILES = ("SKILL.md", "ETHICS.md", "README.md")
REPO_TOOLKIT_DIRS = ("references", "templates")


class SyncToolkitDataHook(BuildHookInterface):
    """Mirror the toolkit's Markdown corpus into the package tree.

    Two build contexts must both succeed:

    * **Repo build** (``python -m build`` at packaging/pypi, or an editable
      install): the canonical Markdown lives at the repo root, above
      packaging/pypi. This hook copies it into ``src/sciresearchkit/data/``
      so hatchling's wheel step includes it.
    * **sdist-to-wheel build** (what ``python -m build`` runs internally,
      what a downstream ``pip install --no-binary`` triggers, and what
      PyPI does when a wheel is built from a sdist): the sdist already
      contains ``src/sciresearchkit/data/`` because the sdist step ran
      the mirror. In this context there is no repo root to walk up to,
      and the hook must be a no-op.
    """

    PLUGIN_NAME = "custom"

    def initialize(self, version: str, build_data: dict) -> None:  # noqa: D401, ARG002
        pkg_data = Path(self.root) / "src" / "sciresearchkit" / "data"
        repo_root = self._find_repo_root()

        if repo_root is None:
            # sdist-to-wheel path: the sdist already ships data/, do nothing.
            # Guard against a malformed sdist that would silently ship an
            # empty package.
            if not pkg_data.is_dir() or not (pkg_data / "SKILL.md").is_file():
                raise RuntimeError(
                    "Cannot locate SciResearchKit source content. Neither a repo "
                    "root (containing SKILL.md and references/) nor a pre-populated "
                    f"{pkg_data} was found. Run the build from the repo root, "
                    "or use a sdist produced by this package."
                )
            return

        # Repo build path: mirror fresh so a removed file doesn't linger.
        if pkg_data.exists():
            shutil.rmtree(pkg_data)
        pkg_data.mkdir(parents=True)

        for name in REPO_TOOLKIT_FILES:
            source = repo_root / name
            if source.is_file():
                shutil.copy2(source, pkg_data / name)

        for dir_name in REPO_TOOLKIT_DIRS:
            source_dir = repo_root / dir_name
            if not source_dir.is_dir():
                continue
            target_dir = pkg_data / dir_name
            target_dir.mkdir(parents=True, exist_ok=True)
            for md_file in sorted(source_dir.glob("*.md")):
                shutil.copy2(md_file, target_dir / md_file.name)

    def _find_repo_root(self) -> Path | None:
        """Return the repo root, or None if this build is inside an sdist."""
        candidate = Path(self.root).resolve()
        for parent in [candidate, *candidate.parents]:
            if (parent / "SKILL.md").is_file() and (parent / "references").is_dir():
                return parent
        return None
