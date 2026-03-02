import os
import time
import psutil
import numpy as np

def get_cpu_usage():
    """Returns the current CPU usage percentage."""
    return psutil.cpu_percent(interval=1)

def draw_ascii_graph(data, max_height=10):
    """Draws an ASCII graph of the CPU usage data."""
    if not data:
        return
    
    max_usage = max(data)
    scale = max_height / max_usage if max_usage > 0 else 1
    
    for value in data:
        height = int(value * scale)
        bar = '#' * height
        print(f"{bar:>{max_height}} {value}%")

def main():
    """Main function to monitor CPU usage and display it graphically."""
    history_length = 20
    cpu_usage_history = []
    
    try:
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            current_usage = get_cpu_usage()
            cpu_usage_history.append(current_usage)
            
            if len(cpu_usage_history) > history_length:
                cpu_usage_history.pop(0)
            
            draw_ascii_graph(cpu_usage_history)
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nMonitoring stopped.")

if __name__ == '__main__':
    main()