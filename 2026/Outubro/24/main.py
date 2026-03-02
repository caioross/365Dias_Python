import os
import time
import statistics

def ping_host(host, count=10):
    """
    Pings a given host and returns a list of latency times.

    :param host: The host to ping.
    :param count: Number of pings to send.
    :return: List of latency times in milliseconds.
    """
    latencies = []
    for _ in range(count):
        response = os.popen(f'ping -c 1 {host}').read()
        latency = extract_latency(response)
        if latency:
            latencies.append(latency)
    return latencies

def extract_latency(response):
    """
    Extracts the latency from the ping response.

    :param response: The response from the ping command.
    :return: Latency in milliseconds or None if not found.
    """
    for line in response.split('\n'):
        if 'time=' in line:
            latency = line.split('time=')[1].split(' ')[0]
            return float(latency)
    return None

def generate_report(latencies):
    """
    Generates a report with minimum, average, and maximum latency.

    :param latencies: List of latency times.
    :return: A dictionary with min, avg, and max latency.
    """
    report = {
        'min': min(latencies),
        'avg': statistics.mean(latencies),
        'max': max(latencies)
    }
    return report

def main():
    """
    Main function to execute the ping monitoring and report generation.
    """
    host = 'google.com'  # Change this to the desired host
    count = 10  # Number of pings to send
    latencies = ping_host(host, count)
    report = generate_report(latencies)
    print(f"Latency Report for {host}:")
    print(f"Minimum: {report['min']} ms")
    print(f"Average: {report['avg']} ms")
    print(f"Maximum: {report['max']} ms")

if __name__ == '__main__':
    main()