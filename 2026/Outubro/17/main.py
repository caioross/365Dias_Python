import datetime

class Medicamento:
    """
    Classe que representa um medicamento com nome e data de vencimento.
    """

    def __init__(self, nome, data_vencimento):
        """
        Inicializa um novo medicamento.

        :param nome: Nome do medicamento.
        :param data_vencimento: Data de vencimento do medicamento no formato 'YYYY-MM-DD'.
        """
        self.nome = nome
        self.data_vencimento = datetime.datetime.strptime(data_vencimento, '%Y-%m-%d')

    def esta_proximo_do_vencimento(self):
        """
        Verifica se o medicamento está próximo do vencimento (1 mês ou menos).

        :return: True se estiver próximo do vencimento, False caso contrário.
        """
        hoje = datetime.datetime.now()
        um_mes = datetime.timedelta(days=30)
        return self.data_vencimento <= hoje + um_mes

def main():
    """
    Função principal que cadastra medicamentos e verifica se estão próximos do vencimento.
    """
    medicamentos = [
        Medicamento("Ibuprofeno", "2023-12-01"),
        Medicamento("Paracetamol", "2024-01-15"),
        Medicamento("Amoxicilina", "2023-11-20")
    ]

    for medicamento in medicamentos:
        if medicamento.esta_proximo_do_vencimento():
            print(f"Alerta: O medicamento {medicamento.nome} está próximo do vencimento!")

if __name__ == '__main__':
    main()