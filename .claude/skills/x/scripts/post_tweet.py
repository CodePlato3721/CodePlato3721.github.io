#!/usr/bin/env python3
"""Post a tweet to X (Twitter) via API v2, using OAuth1.0a user context."""

import argparse
import os
import sys
from pathlib import Path

import requests
from dotenv import load_dotenv
from requests_oauthlib import OAuth1

load_dotenv(Path(__file__).parent.parent / ".env")

TWEET_API = "https://api.twitter.com/2/tweets"
MEDIA_UPLOAD_API = "https://upload.twitter.com/1.1/media/upload.json"
MAX_LEN = 280


def load_credentials() -> OAuth1:
    api_key = os.getenv("X_API_KEY")
    api_secret = os.getenv("X_API_SECRET")
    access_token = os.getenv("X_ACCESS_TOKEN")
    access_token_secret = os.getenv("X_ACCESS_TOKEN_SECRET")

    missing = [
        name
        for name, val in [
            ("X_API_KEY", api_key),
            ("X_API_SECRET", api_secret),
            ("X_ACCESS_TOKEN", access_token),
            ("X_ACCESS_TOKEN_SECRET", access_token_secret),
        ]
        if not val
    ]
    if missing:
        sys.exit(f"Error: missing in .claude/skills/x/.env: {', '.join(missing)}")

    return OAuth1(api_key, api_secret, access_token, access_token_secret)


def upload_media(auth: OAuth1, image_path: Path) -> str:
    if not image_path.exists():
        sys.exit(f"Error: image not found: {image_path}")

    with image_path.open("rb") as f:
        resp = requests.post(MEDIA_UPLOAD_API, auth=auth, files={"media": f}, timeout=60)

    if resp.status_code not in (200, 201):
        sys.exit(f"X media upload error {resp.status_code}:\n{resp.text}")

    return resp.json()["media_id_string"]


def post(filepath: str, image_path: str | None = None) -> None:
    path = Path(filepath)
    if not path.exists():
        sys.exit(f"Error: file not found: {filepath}")

    text = path.read_text(encoding="utf-8").strip()
    if not text:
        sys.exit("Error: tweet text is empty")
    if len(text) > MAX_LEN:
        sys.exit(f"Error: tweet is {len(text)} chars, exceeds {MAX_LEN}-char limit")

    auth = load_credentials()

    payload = {"text": text}
    if image_path:
        media_id = upload_media(auth, Path(image_path))
        payload["media"] = {"media_ids": [media_id]}

    resp = requests.post(TWEET_API, auth=auth, json=payload, timeout=30)

    if resp.status_code in (200, 201):
        data = resp.json()["data"]
        handle = os.getenv("X_HANDLE", "codeplato2026")
        print(f"published: https://x.com/{handle}/status/{data['id']}")
    else:
        sys.exit(f"X API error {resp.status_code}:\n{resp.text}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Post a tweet to X")
    parser.add_argument("filepath", help="Path to a plain-text file containing the tweet")
    parser.add_argument("--image", help="Path to an image file to attach", default=None)
    args = parser.parse_args()
    post(args.filepath, args.image)


if __name__ == "__main__":
    main()
