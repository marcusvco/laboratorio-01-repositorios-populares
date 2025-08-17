import requests
import csv

# --- Bloco de Configuração  ---
token = ""
api_url = "https://api.github.com"
headers = {"Authorization": f"token {token}"}


# --- Funções de Coleta de Dados da API ---
def get_popular_repos(num_repos):
    url = f"{api_url}/search/repositories?q=stars:>80000&sort=stars&order=desc&per_page={num_repos}"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()["items"]
    else:
        raise Exception(f"Failed to fetch repositories: {response.status_code}")

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


# --- Novas Funções de Processamento ---

def gather_repo_data(repos):
    """
    Função central que itera sobre os repositórios e coleta todos os dados detalhados.
    Isso evita repetir chamadas de API.
    """
    all_repo_data = []
    total = len(repos)
    for i, repo in enumerate(repos):
        print(f"Processando repositório {i + 1}/{total}: {repo['name']}...")
        owner = repo["owner"]["login"]
        repo_name = repo["name"]
        

        pull_requests = get_repo_pull_requests(owner, repo_name)
        releases = get_repo_releases(owner, repo_name)
        closed_issues = get_repo_closed_issues(owner, repo_name)
        
        all_repo_data.append({
            "name": repo['name'],
            "stars": repo['stargazers_count'],
            "created_at": repo['created_at'],
            "open_issues_count": repo['open_issues_count'],
            "pull_requests_count": len(pull_requests),
            "releases_count": len(releases),
            "language": repo['language'],
            "closed_issues_count": len(closed_issues)
        })
    return all_repo_data

def generate_csv_file(repo_data, filename="repositorios_github.csv"):
    """
    Recebe os dados coletados e os salva em um arquivo CSV.
    """
    print(f"\nGerando arquivo '{filename}'...")
    # Define o cabeçalho do CSV
    headers = ["Repository", "Stars", "Created At", "Open Issues", "Total Pull Requests", "Total Releases", "Language", "Closed Issues"]
    
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(headers) # Escreve o cabeçalho
        
        for repo in repo_data:
            writer.writerow([
                repo["name"],
                repo["stars"],
                repo["created_at"],
                repo["open_issues_count"],
                repo["pull_requests_count"],
                repo["releases_count"],
                repo["language"],
                repo["closed_issues_count"]
            ])

# --- Função de Exibição ---
def print_repo_infos(repo_data):
    """
    Recebe os dados já processados e apenas os imprime na tela.
    """
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
    num_repos = 100
    
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