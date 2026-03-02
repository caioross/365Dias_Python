import platform
import subprocess

def check_service_status(service_name):
    """
    Verifica o status de um serviço específico no sistema operacional.

    Args:
        service_name (str): O nome do serviço a ser verificado.

    Returns:
        str: Uma mensagem indicando se o serviço está rodando ou não.
    """
    system = platform.system()
    command = None

    if system == "Windows":
        command = f"sc query {service_name}"
    elif system == "Linux":
        command = f"systemctl is-active --quiet {service_name}"
    else:
        return "Sistema operacional não suportado."

    try:
        result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if system == "Windows":
            if b"RUNNING" in result.stdout:
                return f"O serviço {service_name} está rodando."
            else:
                return f"O serviço {service_name} não está rodando."
        elif system == "Linux":
            return f"O serviço {service_name} está rodando."
    except subprocess.CalledProcessError:
        return f"O serviço {service_name} não está rodando."

def main():
    """
    Função principal que executa o script.
    """
    service_name = input("Digite o nome do serviço a ser verificado: ")
    status = check_service_status(service_name)
    print(status)

if __name__ == '__main__':
    main()