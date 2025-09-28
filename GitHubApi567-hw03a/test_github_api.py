import unittest
from unittest.mock import patch, MagicMock
import github_api
import requests

class TestGithubApi(unittest.TestCase):

    @patch("github_api.requests.get")
    def test_happy_path_two_repos(self, mock_get):
        # Fake repos response
        repos_resp = MagicMock(status_code=200)
        repos_resp.json.return_value = [
            {"name": "Triangle567"},
            {"name": "Square567"},
        ]
        # Fake commits responses
        commits1 = MagicMock(status_code=200)
        commits1.json.return_value = [1, 2]
        commits2 = MagicMock(status_code=200)
        commits2.json.return_value = [1, 2, 3]
        mock_get.side_effect = [repos_resp, commits1, commits2]

        out = github_api.get_user_repo_commit_counts("John567")
        self.assertEqual(out, [("Triangle567", 2), ("Square567", 3)])

    @patch("github_api.requests.get")
    def test_user_not_found_returns_empty(self, mock_get):
        resp = MagicMock(status_code=404)
        mock_get.return_value = resp
        self.assertEqual(github_api.get_user_repo_commit_counts("nope"), [])

    def test_formatter(self):
        pairs = [("Triangle567", 10), ("Square567", 27)]
        lines = github_api.format_repo_commits(pairs)
        self.assertEqual(
            lines,
            ["Repo: Triangle567 Number of commits: 10",
             "Repo: Square567 Number of commits: 27"]
        )

if __name__ == "__main__":
    unittest.main()
