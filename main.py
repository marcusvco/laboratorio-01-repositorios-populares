import requests
import csv
import re 

# --- Bloco de Configuração ---
token = ""
api_url = "https://api.github.com"
headers = {"Authorization": f"token {token}"}


# --- Funções de Coleta de Dados da API  ---

def get_popular_repos(num_repos):
    url = f"{api_url}/search/repositories?q=stars:>80000&sort=stars&order=desc&per_page={num_repos}"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()["items"]
    else:
        raise Exception(f"Failed to fetch repositories: {response.status_code}")

def get_repo_pull_requests_count(owner, repo):
    url = f"{api_url}/search/issues?q=is:pr+repo:{owner}/{repo}"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()["total_count"]
    else:
        return 0

def get_repo_releases_count(owner, repo):
    url = f"{api_url}/repos/{owner}/{repo}/releases?per_page=1"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        if 'Link' in response.headers:
            link_header = response.headers['Link']
            last_page_match = re.search(r'page=(\d+)>; rel="last"', link_header)
            if last_page_match:
                return int(last_page_match.group(1))
        return len(response.json())
    return 0
    
def get_repo_closed_issues_count(owner, repo):
    url = f"{api_url}/search/issues?q=is:issue+state:closed+repo:{owner}/{repo}"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()["total_count"]
    else:
        return 0


# --- Funções de Processamento ---

def gather_repo_data(repos):
    all_repo_data = []
    total = len(repos)
    for i, repo in enumerate(repos):
        print(f"Processando repositório {i + 1}/{total}: {repo['name']}...")
        owner = repo["owner"]["login"]
        repo_name = repo["name"]
        
        pull_requests_count = get_repo_pull_requests_count(owner, repo_name)
        closed_issues_count = get_repo_closed_issues_count(owner, repo_name)
        releases_count = get_repo_releases_count(owner, repo_name)
        
        all_repo_data.append({
            "name": repo['name'],
            "stars": repo['stargazers_count'],
            "created_at": repo['created_at'],
            "open_issues_count": repo['open_issues_count'],
            "pull_requests_count": pull_requests_count,
            "releases_count": releases_count,
            "language": repo['language'],
            "closed_issues_count": closed_issues_count
        })
    return all_repo_data

def generate_csv_file(repo_data, filename="repositorios_github.csv"):
    print(f"\nGerando arquivo '{filename}'...")
    headers = ["Repository", "Stars", "Created At", "Open Issues", "Total Pull Requests", "Total Releases", "Language", "Closed Issues"]
    
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        
        for repo in repo_data:
            writer.writerow([
                repo["name"], repo["stars"], repo["created_at"],
                repo["open_issues_count"], repo["pull_requests_count"],
                repo["releases_count"], repo["language"], repo["closed_issues_count"]
            ])

def print_repo_infos(repo_data):
    print("\n--- Lista de Repositórios Populares ---")
    for repo in repo_data:
        print(f"Repository: {repo['name']}")
        print(f"Stars: {repo['stars']}")
        print(f"Created at: {repo['created_at']}")
        print(f"Issues count: {repo['open_issues_count']}")
        print(f"Total pull requests: {repo['pull_requests_count']}")
        print(f"Total releases: {repo['releases_count']}")
        print(f"Language: {repo['language']}")
        print(f"Closed issues: {repo['closed_issues_count']}")
        print("================================")


# --- Bloco Principal de Execução com Menu ---
if __name__ == "__main__":
    num_repos = 5
    
    while True:
        print("\nO que você deseja fazer?")
        print("1 - Listar os repositórios na tela")
        print("2 - Gerar um arquivo CSV com os dados")
        print("3 - Sair")
        choice = input("Digite sua escolha (1, 2 ou 3): ")

        if choice in ['1', '2']:
            try:
                print("Buscando a lista de repositórios populares... Aguarde.")
                popular_repos = get_popular_repos(num_repos=num_repos)
                
                full_data = gather_repo_data(popular_repos)
                
                if choice == '1':
                    print_repo_infos(full_data)
                elif choice == '2':
                    generate_csv_file(full_data)
                    print(f"Arquivo 'repositorios_github.csv' gerado com sucesso!")
                
                break 

            except Exception as e:
                print(f"Ocorreu um erro inesperado: {e}")
                break

        elif choice == '3':
            print("Saindo do programa.")
            break
        
        else:
            print("Opção inválida. Por favor, tente novamente.")