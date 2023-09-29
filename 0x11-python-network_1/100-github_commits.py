#!/usr/bin/python3

import requests
import sys

def get_recent_commits(owner, repo):
    url = f'https://api.github.com/repos/{owner}/{repo}/commits'
    params = {'per_page': 10}

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()

        commits = response.json()
        for commit in commits:
            sha = commit['sha']
            author_name = commit['commit']['author']['name']
            print(f"{sha}: {author_name}")
    except requests.exceptions.HTTPError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit("Usage: ./100-github_commits.py <owner> <repo>")

    owner = sys.argv[1]
    repo = sys.argv[2]
    get_recent_commits(owner, repo)

