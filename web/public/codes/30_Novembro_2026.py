"""
gerenciador_gastos_pessoais_gui.py

Este script cria uma interface gráfica simples para registrar entradas e saídas financeiras.
Ele permite ao usuário adicionar transações e visualizar gráficos de suas finanças.
"""

import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd

class GerenciadorGastos:
    def __init__(self, root):
        self.root = root
        self.root.title("Gerenciador de Gastos Pessoais")
        
        self.transactions = pd.DataFrame(columns=['Tipo', 'Valor'])
        
        self.create_widgets()
    
    def create_widgets(self):
        # Labels and Entries
        tk.Label(self.root, text="Tipo (Entrada/Saída):").grid(row=0, column=0, padx=10, pady=5)
        self.type_entry = tk.Entry(self.root)
        self.type_entry.grid(row=0, column=1, padx=10, pady=5)
        
        tk.Label(self.root, text="Valor:").grid(row=1, column=0, padx=10, pady=5)
        self.value_entry = tk.Entry(self.root)
        self.value_entry.grid(row=1, column=1, padx=10, pady=5)
        
        # Add Transaction Button
        self.add_button = tk.Button(self.root, text="Adicionar Transação", command=self.add_transaction)
        self.add_button.grid(row=2, column=0, columnspan=2, pady=10)
        
        # Plot Button
        self.plot_button = tk.Button(self.root, text="Visualizar Gráficos", command=self.plot_transactions)
        self.plot_button.grid(row=3, column=0, columnspan=2, pady=10)
    
    def add_transaction(self):
        tipo = self.type_entry.get().strip()
        valor = self.value_entry.get().strip()
        
        if not tipo or not valor:
            messagebox.showerror("Erro", "Por favor, preencha todos os campos.")
            return
        
        try:
            valor = float(valor)
        except ValueError:
            messagebox.showerror("Erro", "O valor deve ser um número.")
            return
        
        self.transactions = self.transactions.append({'Tipo': tipo, 'Valor': valor}, ignore_index=True)
        messagebox.showinfo("Sucesso", "Transação adicionada com sucesso!")
        
        self.type_entry.delete(0, tk.END)
        self.value_entry.delete(0, tk.END)
    
    def plot_transactions(self):
        if self.transactions.empty:
            messagebox.showwarning("Aviso", "Não há transações para plotar.")
            return
        
        fig, ax = plt.subplots(figsize=(10, 5))
        self.transactions.groupby('Tipo')['Valor'].sum().plot(kind='bar', ax=ax)
        ax.set_title('Total por Tipo de Transação')
        ax.set_ylabel('Valor')
        
        canvas = FigureCanvasTkAgg(fig, master=self.root)
        canvas.draw()
        canvas.get_tk_widget().grid(row=4, column=0, columnspan=2, pady=10)

def main():
    root = tk.Tk()
    app = GerenciadorGastos(root)
    root.mainloop()

if __name__ == '__main__':
    main()