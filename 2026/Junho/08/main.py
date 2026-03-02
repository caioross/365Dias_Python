import psutil
import platform
from datetime import datetime

def get_system_info():
    """Retrieve system information including CPU, RAM, and disk usage."""
    info = {}
    info['platform'] = platform.system()
    info['platform-release'] = platform.release()
    info['platform-version'] = platform.version()
    info['architecture'] = platform.machine()
    info['processor'] = platform.processor()
    info['ram'] = f"{round(psutil.virtual_memory().total / (1024 ** 3), 2)} GB"
    info['disk'] = f"{round(psutil.disk_usage('/').total / (1024 ** 3), 2)} GB"
    return info

def generate_report(info):
    """Generate a formatted report from the system information."""
    report = f"System Report\n{'='*20}\n"
    report += f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
    for key, value in info.items():
        report += f"{key.replace('_', ' ').capitalize()}: {value}\n"
    return report

def main():
    """Main function to execute the script."""
    system_info = get_system_info()
    report = generate_report(system_info)
    print(report)
    # Optionally, save the report to a file
    with open("system_report.txt", "w") as file:
        file.write(report)

if __name__ == '__main__':
    main()