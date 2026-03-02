import tkinter as tk
from tkinter import messagebox

def calcular_imc(peso, altura):
    """
    Calcula o Índice de Massa Corporal (IMC).

    Args:
        peso (float): Peso do indivíduo em quilogramas.
        altura (float): Altura do indivíduo em metros.

    Returns:
        float: O valor do IMC.
    """
    if altura <= 0:
        raise ValueError("Altura deve ser maior que zero.")
    return peso / (altura ** 2)

def classificar_imc(imc):
    """
    Classifica o IMC em uma categoria.

    Args:
        imc (float): O valor do IMC.

    Returns:
        str: A categoria correspondente ao IMC.
    """
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 24.9:
        return "Normal"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    else:
        return "Obesidade"

def main():
    """
    Função principal que cria a interface gráfica e lida com os eventos.
    """
    def calcular():
        try:
            peso = float(entry_peso.get())
            altura = float(entry_altura.get())
            imc = calcular_imc(peso, altura)
            classificacao = classificar_imc(imc)
            resultado = f"IMC: {imc:.2f}\nClassificação: {classificacao}"
            messagebox.showinfo("Resultado", resultado)
        except ValueError as e:
            messagebox.showerror("Erro", str(e))

    # Configuração da janela principal
    root = tk.Tk()
    root.title("Calculadora de IMC")

    # Labels e Entries
    label_peso = tk.Label(root, text="Peso (kg):")
    label_peso.grid(row=0, column=0, padx=10, pady=10)
    entry_peso = tk.Entry(root)
    entry_peso.grid(row=0, column=1, padx=10, pady=10)

    label_altura = tk.Label(root, text="Altura (m):")
    label_altura.grid(row=1, column=0, padx=10, pady=10)
    entry_altura = tk.Entry(root)
    entry_altura.grid(row=1, column=1, padx=10, pady=10)

    # Botão de cálculo
    botao_calcular = tk.Button(root, text="Calcular IMC", command=calcular)
    botao_calcular.grid(row=2, column=0, columnspan=2, pady=20)

    # Inicia o loop principal da interface gráfica
    root.mainloop()

if __name__ == '__main__':
    main()