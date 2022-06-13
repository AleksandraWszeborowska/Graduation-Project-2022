import requests
import pytest
from branches.settings.credentials_branches import GITHUB_TOKEN
from branches.settings.githubconfig import GITHUB_REST_URL_REF


def test_create_new_branch(branch_sha, delete_branch):
    """create a new branch in repository"""
    sha = branch_sha
    headers = {
        "Authorization": "token " + GITHUB_TOKEN
    }
    data = {
        "ref": "refs/heads/test-branch",
        "sha": sha
    }
    response = requests.post(GITHUB_REST_URL_REF, headers=headers,
                             json=data)
    assert response.status_code == 201
    response_body = response.json()
    assert response_body["object"]["type"] == "commit"
