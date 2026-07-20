"""Smoke tests that the wheel actually ships the toolkit content."""

from __future__ import annotations

import sciresearchkit as srk


def test_skill_loads_and_starts_with_frontmatter() -> None:
    text = srk.get_skill()
    assert text.startswith("---\n"), "SKILL.md must open with YAML frontmatter"
    assert "name: SciResearchKit" in text


def test_ethics_loads() -> None:
    text = srk.get_ethics()
    assert "Ethical Use" in text or "ethical use" in text.lower()


def test_reference_lookup_by_slug_and_filename() -> None:
    a = srk.get_reference("writing-style")
    b = srk.get_reference("writing-style.md")
    assert a == b
    assert len(a) > 200


def test_template_lookup() -> None:
    imrad = srk.get_template("imrad-paper")
    assert "IMRaD" in imrad or "Introduction" in imrad


def test_reference_and_template_listings_are_non_empty() -> None:
    assert len(srk.list_references()) >= 10
    assert len(srk.list_templates()) >= 3


def test_system_prompt_default_includes_ethics() -> None:
    prompt = srk.system_prompt()
    assert srk.get_skill().strip() in prompt
    assert srk.get_ethics().strip() in prompt


def test_system_prompt_no_ethics_option() -> None:
    prompt = srk.system_prompt(include_ethics=False)
    assert srk.get_ethics().strip() not in prompt
