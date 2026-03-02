"""
monitor_uso_gpu.py

Script para monitorar o uso de memória e carga da placa de vídeo (compatível com NVIDIA/AMD).
"""

import subprocess
import re

def get_gpu_usage_nvidia():
    """
    Obtém o uso de memória e carga da GPU NVIDIA usando nvidia-smi.
    
    Returns:
        tuple: (uso de memória, carga da GPU)
    """
    try:
        result = subprocess.run(['nvidia-smi', '--query-gpu=memory.used,memory.total,utilization.gpu', '--format=csv,noheader,nounits'], capture_output=True, text=True, check=True)
        output = result.stdout.strip()
        memory_used, memory_total, gpu_load = map(int, output.split(','))
        memory_usage = f"{memory_used}/{memory_total} MiB"
        gpu_load = f"{gpu_load}%"
        return memory_usage, gpu_load
    except Exception as e:
        print(f"Erro ao obter informações da GPU NVIDIA: {e}")
        return None, None

def get_gpu_usage_amd():
    """
    Obtém o uso de memória e carga da GPU AMD usando aticonfig.
    
    Returns:
        tuple: (uso de memória, carga da GPU)
    """
    try:
        result = subprocess.run(['aticonfig', '--adapter=all', '--odgc'], capture_output=True, text=True, check=True)
        output = result.stdout.strip()
        memory_usage = re.search(r'Memory Usage\s+:\s+(\d+)MB', output)
        gpu_load = re.search(r'Engine Clock\s+:\s+(\d+)MHz', output)
        if memory_usage and gpu_load:
            memory_usage = f"{memory_usage.group(1)} MiB"
            gpu_load = f"{gpu_load.group(1)} MHz"
            return memory_usage, gpu_load
        else:
            print("Não foi possível extrair informações da GPU AMD.")
            return None, None
    except Exception as e:
        print(f"Erro ao obter informações da GPU AMD: {e}")
        return None, None

def main():
    """
    Função principal para monitorar o uso de memória e carga da GPU.
    """
    nvidia_memory, nvidia_load = get_gpu_usage_nvidia()
    amd_memory, amd_load = get_gpu_usage_amd()
    
    if nvidia_memory and nvidia_load:
        print(f"Uso da GPU NVIDIA: {nvidia_memory}, Carga: {nvidia_load}")
    if amd_memory and amd_load:
        print(f"Uso da GPU AMD: {amd_memory}, Carga: {amd_load}")

if __name__ == '__main__':
    main()