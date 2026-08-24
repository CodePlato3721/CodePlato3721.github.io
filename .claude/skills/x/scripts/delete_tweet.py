#!/usr/bin/env python3
"""Delete a tweet from X (Twitter) via API v2, using OAuth1.0a user context."""

import argparse
import os
import sys
from pathlib import Path

import requests
from dotenv import load_dotenv
from requests_oauthlib import OAuth1

load_dotenv(Path(__file__).parent.parent / ".env")

TWEET_API = "https://api.twitter.com/2/tweets"


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


def delete(tweet_id: str) -> None:
    auth = load_credentials()
    resp = requests.delete(f"{TWEET_API}/{tweet_id}", auth=auth, timeout=30)

    if resp.status_code == 200 and resp.json().get("data", {}).get("deleted"):
        print(f"deleted: {tweet_id}")
    else:
        sys.exit(f"X API error {resp.status_code}:\n{resp.text}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Delete a tweet from X")
    parser.add_argument("tweet_id", help="ID of the tweet to delete")
    args = parser.parse_args()
    delete(args.tweet_id)


if __name__ == "__main__":
    main()
