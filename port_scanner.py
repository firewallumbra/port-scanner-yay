import socket
from datetime import datetime
import re
import time

def is_valid_ip(ip):
    # Validate IP address format
    pattern = re.compile(r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
    return pattern.match(ip) is not None

def is_valid_port(port):
    # Validate port range
    return 0 <= port <= 65535

def scan_ports(target, start_port, end_port):
    if not is_valid_ip(target):
        print(f"Invalid IP address: {target}")
        return
    if not (is_valid_port(start_port) and is_valid_port(end_port)):
        print("Invalid port range")
        return
    if start_port > end_port:
        print("Start port must be less than or equal to end port")
        return

    print(f'Starting scan on host: {target}')

    # Measure the time it takes to scan
    start_time = datetime.now()

    for port in range(start_port, end_port + 1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)

        # Try to connect to the target port
        result = s.connect_ex((target, port))
        if result == 0:
            print(f'Port {port}: Open')
        s.close()
        time.sleep(0.1)

    end_time = datetime.now()
    total_time = end_time - start_time
    print(f'Scanning completed in: {total_time}')

def main():
    target = input('Enter the target IP address: ')
    start_port = int(input('Enter the start port: '))
    end_port = int(input('Enter the end port: '))

    scan_ports(target, start_port, end_port)

if __name__ == '__main__':
    main()
