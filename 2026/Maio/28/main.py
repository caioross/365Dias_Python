import tkinter as tk
from tkinter import messagebox
import requests

class BuscadorCEP:
    """
    Classe para criar uma interface gráfica simples para buscar endereços por CEP.
    Utiliza a API ViaCEP para obter os dados do endereço.
    """
    
    def __init__(self, root):
        """
        Inicializa a interface gráfica.
        
        :param root: A janela principal da aplicação.
        """
        self.root = root
        self.root.title("Buscador de CEP")
        
        # Componentes da interface
        self.cep_label = tk.Label(root, text="CEP:")
        self.cep_label.grid(row=0, column=0, padx=10, pady=10)
        
        self.cep_entry = tk.Entry(root)
        self.cep_entry.grid(row=0, column=1, padx=10, pady=10)
        
        self.buscar_button = tk.Button(root, text="Buscar", command=self.buscar_cep)
        self.buscar_button.grid(row=0, column=2, padx=10, pady=10)
        
        self.resultado_label = tk.Label(root, text="")
        self.resultado_label.grid(row=1, column=0, columnspan=3, padx=10, pady=10)
    
    def buscar_cep(self):
        """
        Método para buscar o endereço com base no CEP inserido.
        """
        cep = self.cep_entry.get().replace('-', '')
        if len(cep) != 8 or not cep.isdigit():
            messagebox.showerror("Erro", "CEP inválido. Insira um CEP válido.")
            return
        
        url = f"https://viacep.com.br/ws/{cep}/json/"
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            
            if 'erro' in data:
                messagebox.showerror("Erro", "CEP não encontrado.")
            else:
                self.exibir_resultado(data)
        except requests.RequestException as e:
            messagebox.showerror("Erro", f"Erro ao buscar CEP: {e}")
    
    def exibir_resultado(self, data):
        """
        Exibe o resultado da busca do CEP na interface.
        
        :param data: Dados do endereço obtidos da API.
        """
        resultado = (
            f"Logradouro: {data.get('logradouro', 'N/A')}\n"
            f"Bairro: {data.get('bairro', 'N/A')}\n"
            f"Cidade: {data.get('localidade', 'N/A')}\n"
            f"UF: {data.get('uf', 'N/A')}"
        )
        self.resultado_label.config(text=resultado)

def main():
    """
    Função principal para iniciar a aplicação.
    """
    root = tk.Tk()
    app = BuscadorCEP(root)
    root.mainloop()

if __name__ == '__main__':
    main()