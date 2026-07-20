"""Command-line entry point.

Usage
-----
sciresearchkit                    # prints SKILL.md + ETHICS.md (system prompt)
sciresearchkit skill              # prints SKILL.md
sciresearchkit ethics             # prints ETHICS.md
sciresearchkit references         # lists reference slugs
sciresearchkit reference NAME     # prints references/NAME.md
sciresearchkit templates          # lists template slugs
sciresearchkit template NAME      # prints templates/NAME.md
sciresearchkit path               # prints the data directory
sciresearchkit --version          # prints the installed version
"""

from __future__ import annotations

import argparse
import sys

from . import (
    __version__,
    data_dir,
    get_ethics,
    get_reference,
    get_skill,
    get_template,
    list_references,
    list_templates,
    system_prompt,
)


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="sciresearchkit",
        description=(
            "Load and inspect the SciResearchKit Markdown corpus. "
            "Default output is a copy-paste system prompt (SKILL.md + ETHICS.md)."
        ),
    )
    parser.add_argument("--version", action="version", version=f"sciresearchkit {__version__}")

    sub = parser.add_subparsers(dest="cmd")

    sub.add_parser("skill", help="Print SKILL.md")
    sub.add_parser("ethics", help="Print ETHICS.md")
    sub.add_parser("references", help="List reference-file slugs")
    sub.add_parser("templates", help="List template slugs")
    sub.add_parser("path", help="Print the bundled data directory path")

    p_ref = sub.add_parser("reference", help="Print a reference file by slug")
    p_ref.add_argument("name")

    p_tpl = sub.add_parser("template", help="Print a template by slug")
    p_tpl.add_argument("name")

    p_prompt = sub.add_parser(
        "prompt",
        help="Print the copy-paste system prompt (default when no subcommand is given)",
    )
    p_prompt.add_argument(
        "--no-ethics",
        action="store_true",
        help="Emit SKILL.md only, without appending ETHICS.md",
    )

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = _build_parser()
    args = parser.parse_args(argv)

    cmd = args.cmd or "prompt"

    if cmd == "prompt":
        include_ethics = not getattr(args, "no_ethics", False)
        sys.stdout.write(system_prompt(include_ethics=include_ethics))
        return 0
    if cmd == "skill":
        sys.stdout.write(get_skill())
        return 0
    if cmd == "ethics":
        sys.stdout.write(get_ethics())
        return 0
    if cmd == "path":
        sys.stdout.write(str(data_dir()) + "\n")
        return 0
    if cmd == "references":
        sys.stdout.write("\n".join(list_references()) + "\n")
        return 0
    if cmd == "templates":
        sys.stdout.write("\n".join(list_templates()) + "\n")
        return 0
    if cmd == "reference":
        try:
            sys.stdout.write(get_reference(args.name))
        except FileNotFoundError as exc:
            print(str(exc), file=sys.stderr)
            return 2
        return 0
    if cmd == "template":
        try:
            sys.stdout.write(get_template(args.name))
        except FileNotFoundError as exc:
            print(str(exc), file=sys.stderr)
            return 2
        return 0

    parser.error(f"unknown command: {cmd}")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
