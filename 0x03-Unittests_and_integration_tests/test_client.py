#!/usr/bin/env python3
""" Client Test Case """
import unittest
from fixtures import TEST_PAYLOAD
from parameterized import parameterized, parameterized_class
from unittest.mock import patch, MagicMock, PropertyMock
from client import GithubOrgClient
from typing import Dict


class TestGithubOrgClient(unittest.TestCase):
    """Test GithubOrgClient"""

    @parameterized.expand([("google"), ("abc")])
    @patch("client.get_json")
    def test_org(self, name: str, mock: MagicMock) -> None:
        """test organization method"""
        github_org = GithubOrgClient(str)
        github_org.org(name)
        mock.called_with_once(github_org.ORG_URL.format(org=name))

    def test_public_repos_url(self) -> None:
        """test public repositories url"""
        with patch("client.GithubOrgClient.org",
                   new_callable=PropertyMock) as mock:
            payload = {
                "repos_url": "https://api.github.com/users/google/repos",
            }
            mock.return_value = payload
            github_org = GithubOrgClient("google")
            result = github_org._public_repos_url
            self.assertEqual(result, payload["repos_url"])

    @patch("client.get_json")
    def test_public_repos(self, mock: MagicMock) -> None:
        """test public repositories method"""
        payload = {
            'repos_url': "https://api.github.com/users/google/repos",
            'repos': [
                {
                    "id": 1,
                    "name": "google",
                },
                {
                    "id": 2,
                    "name": "george",
                },
            ],
        }
        mock.return_value = payload["repos"]

        with patch(
            "client.GithubOrgClient."
            "_public_repos_url", new_callable=PropertyMock
        ) as mock_url:
            mock_url.return_value = payload["repos_url"]
            result = GithubOrgClient("google").public_repos()
            expected = [item["name"] for item in payload["repos"]]
            self.assertEqual(result, expected)
            mock_url.assert_called_once()
        mock.assert_called_once()

    @parameterized.expand(
        [
            ({"license": {"key": "my_license"}}, "my_license", True),
            ({"license": {"key": "other_license"}}, "my_license", False),
        ]
    )
    def test_has_license(
        self, repo: Dict[str, Dict], license_key: str, expected: bool
    ) -> None:
        """test has license"""
        result = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(result, expected)


@parameterized_class(
    ("org_payload", "repos_payload",
     "expected_repos", "apache2_repos"), TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        """Set up the integration Test"""
        config = {
            "return_value.json.side_effect": [
                cls.org_payload,
                cls.repos_payload,
                cls.org_payload,
                cls.repos_payload,
            ]
        }
        cls.get_patcher = patch("requests.get", **config)
        cls.mock = cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls) -> None:
        """Tear down the Test"""
        cls.get_patcher.stop()

    def test_public_repos(self) -> None:
        """test public repositories"""
        result = GithubOrgClient("google").public_repos()
        self.assertEqual(
            result,
            self.expected_repos,
        )
        self.mock.assert_called()

    def test_public_repos_with_license(self) -> None:
        """test public repositories with license"""
        result = GithubOrgClient("google").public_repos(license="apache-2.0")
        self.assertEqual(
            result,
            self.apache2_repos,
        )
        self.mock.assert_called()
