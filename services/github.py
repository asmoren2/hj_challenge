import logging
import os

import requests


def fork_repo(owner, repo):
    headers = {
        'Authorization': f'Bearer {os.getenv("GITHUB_TOKEN")}',
        'Accept': 'application/vnd.github+json'
    }
    url = f'https://api.github.com/repos/{owner}/{repo}/forks'
    response = requests.post(url, headers=headers)
    if response.status_code == 202:
        logging.error(f'Repo was forked')
        return response.json()
    logging.error(f'Failed to fork repo')
    return None

