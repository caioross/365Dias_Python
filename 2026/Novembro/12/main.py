"""
buscador_clima_cidade_gui.py

Interface gráfica para buscar e mostrar o clima atual de uma cidade.
Utiliza a API OpenWeatherMap para obter os dados de clima.
"""

import tkinter as tk
from tkinter import messagebox
import requests

API_KEY = 'SUA_API_KEY_AQUI'  # Substitua pela sua chave de API do OpenWeatherMap
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"

class ClimaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Buscador de Clima")
        
        self.create_widgets()
    
    def create_widgets(self):
        # Criação dos widgets
        self.label_cidade = tk.Label(self.root, text="Digite a cidade:")
        self.label_cidade.pack(pady=5)
        
        self.entry_cidade = tk.Entry(self.root, width=30)
        self.entry_cidade.pack(pady=5)
        
        self.botao_buscar = tk.Button(self.root, text="Buscar", command=self.buscar_clima)
        self.botao_buscar.pack(pady=10)
        
        self.label_resultado = tk.Label(self.root, text="", font=("Helvetica", 16))
        self.label_resultado.pack(pady=20)
        
        self.label_icon = tk.Label(self.root, image="")
        self.label_icon.pack(pady=10)
    
    def buscar_clima(self):
        cidade = self.entry_cidade.get()
        if not cidade:
            messagebox.showwarning("Aviso", "Por favor, digite o nome de uma cidade.")
            return
        
        completo_url = BASE_URL + "appid=" + API_KEY + "&q=" + cidade + "&units=metric"
        resposta = requests.get(completo_url)
        
        if resposta.status_code == 200:
            dados = resposta.json()
            main = dados['main']
            temperatura = main['temp']
            icon_code = dados['weather'][0]['icon']
            icon_url = f"http://openweathermap.org/img/wn/{icon_code}.png"
            
            self.label_resultado.config(text=f"Temperatura em {cidade}: {temperatura}°C")
            self.label_icon.config(image=tk.PhotoImage(file=icon_url))
            self.label_icon.image = tk.PhotoImage(file=icon_url)
        else:
            messagebox.showerror("Erro", "Cidade não encontrada. Por favor, verifique o nome.")

def main():
    root = tk.Tk()
    app = ClimaApp(root)
    root.mainloop()

if __name__ == '__main__':
    main()