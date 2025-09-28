import requests

def get_user_repo_commit_counts(user: str):
    """
    Returns a list of (repo_name, commit_count) for the given GitHub user.
    - Counts ONLY the first page of commits per repo (simple version).
    - Private/unreachable repos -> commit_count = 0.
    - Unknown user -> returns [].
    """
    repos_url = f"https://api.github.com/users/{user}/repos"
    try:
        r = requests.get(repos_url, timeout=10)
    except requests.RequestException:
        return []
    if r.status_code != 200:
        return []

    results = []
    for repo in r.json():
        name = repo.get("name")
        if not name:
            continue
        commits_url = f"https://api.github.com/repos/{user}/{name}/commits"
        try:
            cr = requests.get(commits_url, timeout=10)
            if cr.status_code != 200:
                count = 0
            else:
                data = cr.json()
                count = len(data) if isinstance(data, list) else 0
        except requests.RequestException:
            count = 0
        results.append((name, count))
    return results


def format_repo_commits(pairs):
    """Return strings in the assignment's example format."""
    return [f"Repo: {name} Number of commits: {count}" for name, count in pairs]


if __name__ == "__main__":
    import sys
    user = sys.argv[1] if len(sys.argv) > 1 else "richkempinski"
    for line in format_repo_commits(get_user_repo_commit_counts(user)):
        print(line)

