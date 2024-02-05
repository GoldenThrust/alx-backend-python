#!/usr/bin/env python3
""" Client Test Case """
import unittest
from fixtures import TEST_PAYLOAD
from parameterized import parameterized, parameterized_class
from unittest.mock import patch, MagicMock, PropertyMock
from client import GithubOrgClient
from typing import (
    List,
    Dict,
)

class TestGithubOrgClient(unittest.TestCase):
    @parameterized.expand([("google"), ("abc")])
    @patch("client.get_json")
    def test_org(self, name: str, mock: MagicMock):
        github_org = GithubOrgClient(str)
        github_org.org(name)
        mock.called_with_once(github_org.ORG_URL.format(org=name))

    def test_public_repos_url(self):
        with patch("client.GithubOrgClient.org", new_callable=PropertyMock) as mock:
            payload = {
                "repos_url": "https://api.github.com/users/google/repos",
            }
            mock.return_value = payload
            github_org = GithubOrgClient("google")
            result = github_org._public_repos_url
            self.assertEqual(result, payload["repos_url"])

    @patch("client.get_json")
    def test_public_repos(self, mock: MagicMock):
        payload = {
            "url": "https://api.github.com/users/google/repos",
            "repos": [
                {
                    "name": "google",
                },
                {
                    "name": "george",
                },
            ],
        }
        mock.return_value = payload['url']

        with patch(
            "client.GithubOrgClient._public_repos_url", new_callable=PropertyMock
        ) as mock_patch:
            output =  [item['name'] for item in payload['repos']]
            mock.return_value = payload['repos']
            github_org = GithubOrgClient('google')
            result = github_org.public_repos()

            self.assertEqual(output, result)
            mock_patch.assert_called_once()
        mock.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo: Dict[str, Dict], license_key: str, expected: bool):
        result = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(result, expected)

@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def test_public_repos(self):
        pass

    def test_public_repos_with_license(self):
        pass
