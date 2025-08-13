import requests

token = ""
api_url = "https://api.github.com"

headers = {"Authorization": f"token {token}"}

def get_popular_repos(keyword, num_repos):
    url = f"{api_url}/search/repositories?q={keyword}&sort=stars&order=desc&per_page={num_repos}"
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

def collect_and_print_repo_info(repos):
    for repo in repos:
        owner = repo["owner"]["login"]
        repo_name = repo["name"]
        repo_details = get_repo_details(owner, repo_name)

        print(f"Repository: {repo_name}")
        print(f"Stars: {repo_details['stargazers_count']}")
        print("================================")

def print_repo_infos(repos):
    for repo in repos:
        print(f"Repository: {repo['name']}")
        print(f"Stars: {repo['stargazers_count']}")
        print("================================")

if __name__ == "__main__":
    keyword = "microservices"
    num_repos = 10

    try:
        popular_repos = get_popular_repos(keyword=keyword, num_repos=num_repos)
        print_repo_infos(popular_repos)
    except Exception as e:
        print(e)
