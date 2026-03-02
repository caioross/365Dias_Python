"""
Script para analisar um repositório Git e gerar estatísticas de commits, autores e arquivos alterados.
"""

import subprocess
import json

def get_git_stats():
    """
    Recupera estatísticas do repositório Git atual.
    
    Returns:
        dict: Um dicionário contendo estatísticas de commits, autores e arquivos alterados.
    """
    # Comando para obter estatísticas de commits
    commits_command = "git log --pretty=format:'{\"commit\": \"%H\", \"author\": \"%an\", \"date\": \"%ad\", \"files\": [%f]}'"
    commits_output = subprocess.check_output(commits_command, shell=True, text=True)
    
    # Processa a saída para criar uma lista de commits
    commits = []
    for line in commits_output.strip().split('\n'):
        commit_data = json.loads(line)
        commits.append(commit_data)
    
    # Estatísticas básicas
    total_commits = len(commits)
    authors = set(commit['author'] for commit in commits)
    total_authors = len(authors)
    
    # Conta arquivos alterados
    files_changed = set()
    for commit in commits:
        files_changed.update(commit['files'])
    
    total_files_changed = len(files_changed)
    
    # Retorna as estatísticas
    return {
        'total_commits': total_commits,
        'total_authors': total_authors,
        'total_files_changed': total_files_changed,
        'authors': list(authors),
        'files_changed': list(files_changed)
    }

def main():
    """
    Função principal para executar o script.
    """
    stats = get_git_stats()
    print("Estatísticas do Repositório Git:")
    print(f"Total de Commits: {stats['total_commits']}")
    print(f"Total de Autores: {stats['total_authors']}")
    print(f"Total de Arquivos Alterados: {stats['total_files_changed']}")
    print("\nAutores:")
    for author in stats['authors']:
        print(f"- {author}")
    print("\nArquivos Alterados:")
    for file in stats['files_changed']:
        print(f"- {file}")

if __name__ == '__main__':
    main()