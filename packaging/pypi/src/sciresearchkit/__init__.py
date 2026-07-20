"""SciResearchKit: model-agnostic scientific-research skill.

Programmatic access to the Markdown skill files bundled with the
package. The Markdown itself is the product; this module is a thin
loader so any Python-hosted LLM harness can pull the router
(``SKILL.md``), the ethical-use notice (``ETHICS.md``), a specific
reference file, or a template without shelling out to the filesystem
layout.

Example
-------
>>> import sciresearchkit as srk
>>> prompt = srk.system_prompt()
>>> writing = srk.get_reference("writing-style")
>>> imrad = srk.get_template("imrad-paper")

The bundled corpus is versioned with the package and is available at
``sciresearchkit.data_dir()`` for callers that need a directory handle
rather than string content.

See ``ETHICS.md`` (also available via ``srk.get_ethics()``) for the
conditions that govern use of this toolkit.
"""

from __future__ import annotations

from importlib import resources
from importlib.metadata import PackageNotFoundError, version
from pathlib import Path
from typing import Iterator

__all__ = [
    "__version__",
    "data_dir",
    "get_ethics",
    "get_reference",
    "get_skill",
    "get_template",
    "list_references",
    "list_templates",
    "system_prompt",
]

try:
    __version__ = version("sciresearchkit")
except PackageNotFoundError:  # pragma: no cover - editable install pre-metadata
    __version__ = "0.0.0+local"


def data_dir() -> Path:
    """Return the directory containing the bundled Markdown corpus."""
    return Path(str(resources.files(__name__).joinpath("data")))


def _read(relpath: str) -> str:
    root = resources.files(__name__).joinpath("data")
    target = root.joinpath(relpath)
    if not target.is_file():
        raise FileNotFoundError(
            f"SciResearchKit resource not found: {relpath!r} "
            f"(looked under {root!s})"
        )
    return target.read_text(encoding="utf-8")


def get_skill() -> str:
    """Return the contents of ``SKILL.md`` (the top-level router)."""
    return _read("SKILL.md")


def get_ethics() -> str:
    """Return the contents of ``ETHICS.md``."""
    return _read("ETHICS.md")


def get_reference(name: str) -> str:
    """Return a reference file by name (with or without ``.md`` suffix)."""
    if not name.endswith(".md"):
        name = f"{name}.md"
    return _read(f"references/{name}")


def get_template(name: str) -> str:
    """Return a template file by name (with or without ``.md`` suffix)."""
    if not name.endswith(".md"):
        name = f"{name}.md"
    return _read(f"templates/{name}")


def _iter_bundle(subdir: str) -> Iterator[str]:
    root = resources.files(__name__).joinpath("data").joinpath(subdir)
    for entry in sorted(root.iterdir()):
        name = entry.name
        if name.endswith(".md"):
            yield name[:-3]


def list_references() -> list[str]:
    """Return the sorted list of available reference-file slugs."""
    return list(_iter_bundle("references"))


def list_templates() -> list[str]:
    """Return the sorted list of available template slugs."""
    return list(_iter_bundle("templates"))


def system_prompt(*, include_ethics: bool = True) -> str:
    """Return a copy-paste system prompt for an LLM.

    Concatenates SKILL.md with (optionally) ETHICS.md. This is the
    recommended minimum payload for loading the toolkit into a hosted
    LLM system-prompt slot.
    """
    parts = [get_skill()]
    if include_ethics:
        parts.append("\n\n---\n\n")
        parts.append(get_ethics())
    return "".join(parts)
