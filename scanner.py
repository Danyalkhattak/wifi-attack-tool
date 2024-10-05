import os

def scan_networks():
    print("Scanning for networks...")
    os.system("sudo airmon-ng start wlan0")
    os.system("sudo airodump-ng wlan0mon")
