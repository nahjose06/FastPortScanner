#!/usr/bin/python3

# FastPortScannet, Author: @nahjose06 (José Navarro)

from colorama import Fore, init, Style
import pyfiglet
import socket
from datetime import datetime
from time import sleep
import threading
import concurrent.futures
import sys

init()

banner = pyfiglet.figlet_format("FastPortScanner")

print(Fore.RED + banner + Style.RESET_ALL)
print(Fore.RED + "By José Navarro" + Style.RESET_ALL)
sleep(1)

print_lock = threading.Lock()
ip = input("Set the target's IP: ")
target = socket.gethostbyname(ip)
print("\n")

print("-" * 50)

print(Fore.RED + "Scanning target: " + Fore.GREEN + target + Style.RESET_ALL)
print(Fore.YELLOW + "Scan started at: " + str(datetime.now()))
print("-" * 50)

def scan(target, port):
    scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    scanner.settimeout(1)
    try:
        scanner.connect((target, port))
        scanner.close()
        with print_lock:
            print(Fore.GREEN + f"Port [{port}]: Opened" + Style.RESET_ALL)

    except KeyboardInterrupt:
        print(Fore.RED + "\n Exiting program, CTRL + C detected" + Style.RESET_ALL)
        sys.exit()
    except socket.gaierror:
        print(Fore.RED + "\n Hostname could not be resolved!" + Style.RESET_ALL)                          
        sys.exit()

with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
    for port in range(65535):
        executor.submit(scan, target, port + 1)
