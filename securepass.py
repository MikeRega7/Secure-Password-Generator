#!/usr/bin/python3
import pyfiglet
import string
import random
import signal
import sys
import time
from pwn import *
from colorama import Style, Fore, Back

def print_banner():
    banner = pyfiglet.figlet_format("By Miguelrega7")
    print(banner)

def def_handler(sig, frame):
    print(Fore.BLUE +"\n\n[!] Exit...")
    sys.exit(1)

def generate_password():
    while True:
        try:
            print(Fore.RED + Style.BRIGHT + "\nRemember to use a password longer than 12 characters\n")
            l = int(input(Fore.YELLOW + Style.BRIGHT + "\nHow many characters would you like your password to be? "))
            caracteres = string.ascii_letters + string.digits + string.punctuation
            p1 = log.progress("Creating a secure password")
            time.sleep(3)
            password = ''.join(random.choice(caracteres) for i in range(l))
            p1.status("Completed")
            print(Fore.GREEN + Style.BRIGHT + f"\nGenerated Password: {password}")
        except KeyboardInterrupt:
            print(Fore.RED + Style.BRIGHT + "\n\n[!] Exit...")
            break

def main():
    print_banner()
    print("\n[-] Use: python3 " + sys.argv[0])
    signal.signal(signal.SIGINT, def_handler)
    generate_password()

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(f"Error: {e}")
