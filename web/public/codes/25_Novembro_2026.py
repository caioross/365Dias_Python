import os
import shutil
import re

class OrganizadorDownloads:
    """
    Classe para organizar arquivos em pastas com base em palavras-chave no nome do arquivo.
    """

    def __init__(self, diretorio_download, diretorios_destino):
        """
        Inicializa o organizador com o diretório de downloads e os diretórios de destino.

        :param diretorio_download: Caminho para o diretório de downloads.
        :param diretorios_destino: Dicionário com palavras-chave como chaves e caminhos de destino como valores.
        """
        self.diretorio_download = diretorio_download
        self.diretorios_destino = diretorios_destino

    def organizar(self):
        """
        Organiza os arquivos no diretório de downloads movendo-os para as pastas de destino.
        """
        for arquivo in os.listdir(self.diretorio_download):
            if os.path.isfile(os.path.join(self.diretorio_download, arquivo)):
                for palavra_chave, destino in self.diretorios_destino.items():
                    if re.search(palavra_chave, arquivo, re.IGNORECASE):
                        self.mover_arquivo(arquivo, destino)
                        break

    def mover_arquivo(self, arquivo, destino):
        """
        Move um arquivo para o diretório de destino.

        :param arquivo: Nome do arquivo a ser movido.
        :param destino: Caminho do diretório de destino.
        """
        origem = os.path.join(self.diretorio_download, arquivo)
        destino_completo = os.path.join(destino, arquivo)
        os.makedirs(destino, exist_ok=True)
        shutil.move(origem, destino_completo)
        print(f'Movido: {arquivo} para {destino}')

def main():
    """
    Função principal para executar o organizador de downloads.
    """
    diretorio_download = '/caminho/para/downloads'
    diretorios_destino = {
        'fatura': '/caminho/para/pastas/faturas',
        'relatorio': '/caminho/para/pastas/relatorios',
        'imagem': '/caminho/para/pastas/imagens',
        'video': '/caminho/para/pastas/videos'
    }

    organizador = OrganizadorDownloads(diretorio_download, diretorios_destino)
    organizador.organizar()

if __name__ == '__main__':
    main()