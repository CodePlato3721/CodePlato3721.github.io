#!/usr/bin/env python3
"""Publish a Hugo blog post to Dev.to via API."""

import argparse
import os
import re
import sys
from pathlib import Path

import frontmatter
import requests
from dotenv import load_dotenv

load_dotenv(Path(__file__).parent.parent.parent / ".env")

BASE_URL = "https://CodePlato3721.github.io/"
DEVTO_API = "https://dev.to/api/articles"
DEFAULT_LANG = "en"


def canonical_url(filepath: Path) -> str:
    parts = filepath.resolve().parts
    try:
        idx = [p.lower() for p in parts].index("content")
    except ValueError:
        return ""

    lang = parts[idx + 1]
    slug_parts = list(parts[idx + 2:])

    if slug_parts and slug_parts[-1] in ("index.md", "_index.md"):
        slug_parts.pop()

    slug = "/".join(slug_parts)
    if lang == DEFAULT_LANG:
        return f"{BASE_URL}{slug}/"
    return f"{BASE_URL}{lang}/{slug}/"


def clean_body(body: str, title: str) -> str:
    """Remove leading H1 if it duplicates the frontmatter title."""
    lines = body.lstrip("\n").split("\n")
    if lines and lines[0].strip() == f"# {title}":
        lines = lines[1:]
        if lines and lines[0].strip() == "":
            lines = lines[1:]
    return "\n".join(lines)


def sanitize_tag(tag: str) -> str:
    return re.sub(r"[^a-z0-9_]", "", tag.lower())


def publish(filepath: str) -> None:
    api_key = os.getenv("DEVTO_API_KEY")
    if not api_key:
        sys.exit("Error: DEVTO_API_KEY not set in publish/.env")

    path = Path(filepath)
    if not path.exists():
        sys.exit(f"Error: file not found: {filepath}")

    post = frontmatter.load(path)

    title = post.get("title", path.stem)
    if re.match(r'^[a-z0-9]+(-[a-z0-9]+)+$', title):
        sys.exit(f"Error: title '{title}' looks like a slug. Set a proper human-readable title in the frontmatter.")
    tags = [sanitize_tag(t) for t in post.get("tags", [])[:4] if sanitize_tag(t)]
    image = post.get("image", "")
    body = clean_body(post.content, title)
    url = canonical_url(path)

    article: dict = {
        "title": title,
        "body_markdown": body,
        "published": True,
        "tags": tags,
    }
    if url:
        article["canonical_url"] = url
    if image:
        article["main_image"] = image

    resp = requests.post(
        DEVTO_API,
        headers={"api-key": api_key, "Content-Type": "application/json"},
        json={"article": article},
        timeout=30,
    )

    if resp.status_code in (200, 201):
        data = resp.json()
        print(f"published: {data['url']}")
    else:
        sys.exit(f"Dev.to API error {resp.status_code}:\n{resp.text}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Publish Hugo post to Dev.to")
    parser.add_argument("filepath", help="Path to Hugo markdown file")
    args = parser.parse_args()
    publish(args.filepath)


if __name__ == "__main__":
    main()
