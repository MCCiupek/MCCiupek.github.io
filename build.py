#!/usr/bin/env python3
"""Build index.html from resume.yaml + template.html."""

import re
from pathlib import Path

import yaml
from jinja2 import Environment, FileSystemLoader

ROOT = Path(__file__).parent


def linkify(text: str) -> str:
    """Convert markdown-style [label](url) links to HTML anchors."""
    return re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', text)


def build() -> None:
    data = yaml.safe_load((ROOT / "resume.yaml").read_text())

    env = Environment(
        loader=FileSystemLoader(ROOT),
        autoescape=False,
        keep_trailing_newline=True,
    )
    env.filters["linkify"] = linkify

    template = env.get_template("template.html")

    for proj in data.get("side_projects", []):
        proj["title"] = linkify(proj["title"])
        if proj.get("extra"):
            proj["extra"] = linkify(proj["extra"])

    html = template.render(**data)
    (ROOT / "index.html").write_text(html)
    print("Built index.html")


if __name__ == "__main__":
    build()
