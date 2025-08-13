import requests

token = ""
api_url = "https://api.github.com"

headers = {"Authorization": f"token {token}"}

def get_popular_repos(num_repos):
    url = f"{api_url}/search/repositories?q=stars:>80000&sort=stars&order=desc&per_page={num_repos}"
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return response.json()["items"]
    else:
        raise Exception(f"Failed to fetch repositories: {response.status_code}")

def get_repo_details(owner, repo):
    url = f"{api_url}/repos/{owner}/{repo}"
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to fetch repository details: {response.status_code}")

def get_repo_pull_requests(owner, repo):
    url = f"{api_url}/repos/{owner}/{repo}/pulls"
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to fetch repository pull requests: {response.status_code}")

def get_repo_releases(owner, repo):
    url = f"{api_url}/repos/{owner}/{repo}/releases"
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to fetch repository releases: {response.status_code}")

def get_repo_closed_issues(owner, repo):
    url = f"{api_url}/repos/{owner}/{repo}/issues?state=closed"
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to fetch repository closed issues: {response.status_code}")

def print_repo_infos(repos):
    for repo in repos:
        owner = repo["owner"]["login"]
        repo_name = repo["name"]
        repo_pull_requests = get_repo_pull_requests(owner, repo_name)
        repo_releases = get_repo_releases(owner, repo_name)
        closed_issues = get_repo_closed_issues(owner, repo_name)

        print(f"Repository: {repo['name']}")
        print(f"Stars: {repo['stargazers_count']}")
        print(f"Created at: {repo['created_at']}")
        print(f"Issues count: {repo['open_issues_count']}")
        print(f"Total pull requests: {len(repo_pull_requests)}")
        print(f"Total releases: {len(repo_releases)}")
        print(f"Language: {repo['language']}")
        print(f"Closed issues: {len(closed_issues)}")
        print("================================")

if __name__ == "__main__":
    num_repos = 100

    try:
        popular_repos = get_popular_repos(num_repos=num_repos)
        print_repo_infos(popular_repos)
    except Exception as e:
        print(e)
