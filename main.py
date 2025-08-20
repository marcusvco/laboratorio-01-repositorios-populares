import requests
import csv
import re

from models.repository import Repository 

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

def get_repo_pull_requests(owner, repo):
    url = f"{api_url}/search/issues?q=is:pr+repo:{owner}/{repo}"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
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
        
        pull_requests_count = len(get_repo_pull_requests(owner, repo_name))
        closed_issues_count = get_repo_closed_issues_count(owner, repo_name)
        releases_count = get_repo_releases_count(owner, repo_name)
        
        repository = Repository(
            name=repo['name'],
            stars=repo['stargazers_count'],
            created_at=repo['created_at'],
            open_issues_count=repo['open_issues_count'],
            pull_requests_count=pull_requests_count,
            releases_count=releases_count,
            language=repo['language'],
            closed_issues_count=closed_issues_count
        )
        all_repo_data.append(repository)
    return all_repo_data

def generate_csv_file(repo_data: list[Repository], filename="repositorios_github.csv"):
    print(f"\nGerando arquivo '{filename}'...")
    headers = ["Repository", "Stars", "Created At", "Open Issues", "Total Pull Requests", "Total Releases", "Language", "Closed Issues"]
    
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        
        for repo in repo_data:
            writer.writerow([
                repo.name, repo.stars, repo.created_at,
                repo.open_issues_count, repo.pull_requests_count,
                repo.releases_count, repo.language, repo.closed_issues_count
            ])

def print_repo_infos(repo_data: list[Repository]):
    print("\n--- Lista de Repositórios Populares ---")
    for repo in repo_data:
        repo.print()

def get_median_repo_age(repo_data: list[Repository]):
    ages = []
    for repo in repo_data:
        ages.append(repo.getAge())

    if not ages:
        return 0
    
    return sum(ages) / len(ages)

def get_languages(repo_data: list[Repository]):
    languages = {}
    for repo in repo_data:
        lang = repo.language
        if lang:
            languages[lang] = languages.get(lang, 0) + 1
    return languages

def generate_rqs_data(repos):
    median_repo_age = get_median_repo_age(repos)
    languages = get_languages(repos)
    print(f"Média de idade dos repositórios: {median_repo_age} anos")
    print("Distribuição de Linguagens:")
    for lang, count in languages.items():
        print(f" - {lang}: {count}")

# --- Bloco Principal de Execução com Menu ---
if __name__ == "__main__":
    num_repos = 1
    
    while True:
        print("\nO que você deseja fazer?")
        print("1 - Listar os repositórios na tela")
        print("2 - Gerar um arquivo CSV com os dados")
        print("3 - Gerar resultados das RQS")
        print("4 - Sair")
        choice = input("Digite sua escolha (1, 2 ou 3): ")

        if choice in ['1', '2', '3']:
            try:
                print("Buscando a lista de repositórios populares... Aguarde.")
                popular_repos = get_popular_repos(num_repos=num_repos)
                
                full_data = gather_repo_data(popular_repos)
                
                if choice == '1':
                    print_repo_infos(full_data)
                elif choice == '2':
                    generate_csv_file(full_data)
                    print(f"Arquivo 'repositorios_github.csv' gerado com sucesso!")
                elif choice == '3':
                    generate_rqs_data(full_data)

            except Exception as e:
                print(f"Ocorreu um erro inesperado: {e}")
                break

        elif choice == '4':
            print("Saindo do programa.")
            break
        
        else:
            print("Opção inválida. Por favor, tente novamente.")