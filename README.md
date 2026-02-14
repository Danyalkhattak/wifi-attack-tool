<p align="center">
  <img src="./image.jpg" alt="Thumbnail" />
</p>

# 🔥 Wi-Fi Attack Automation Tool (Kali Linux & Termux) 🔥


This tool automates Wi-Fi attacks such as Deauthentication, Evil Twin, and WPA Handshake Capture. It is optimized for **Kali Linux** and **Termux** (Root Required), providing a user-friendly TUI (Text User Interface).

🚨 **Disclaimer**: This tool is for educational purposes only. Always get permission from network owners before conducting any attacks.

## 📜 Features

- 🕵️ **Network Scanning**: Identify nearby Wi-Fi networks.
- 🚫 **Deauthentication Attack**: Disconnect all clients from a target network.
- 💀 **Evil Twin Attack**: Set up a rogue Wi-Fi access point (Requires external adapter supporting AP mode).
- 📡 **WPA Handshake Capture**: Capture handshakes for offline cracking.
- 🛡️ **Defense Tips**: Learn how to defend your network against attacks.
- 🎨 **Rich TUI**: Beautiful and easier to use command-line interface.

## 🎯 How to Use

### Kali Linux

#### 1. Install Dependencies
Ensure you have all necessary tools installed:
```bash
sudo apt-get update && sudo apt-get install aircrack-ng hostapd dnsmasq python3-pip
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

### Termux (Android)

**Note:** You need a rooted device and an external Wi-Fi adapter that supports monitor mode connected via OTG.

#### 1. Install Dependencies
Open Termux and install the required packages:
```bash
pkg update
pkg install root-repo
pkg install aircrack-ng python3 tsu
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
You must run as root using `tsu`:
```bash
tsu
python3 main.py
```

---

## 📡 Wi-Fi Scanning

- Run the network scanning module to view nearby Wi-Fi networks:
```bash
# The tool automates these commands:
airmon-ng start wlan0
airodump-ng wlan0mon
```

---

## 🚀 Attacks

1. **Deauthentication Attack**:
   - Disconnect clients from a target network.
   
2. **Evil Twin Attack**:
   - Create a fake access point (requires `hostapd` and `dnsmasq`).

3. **WPA Handshake Capture**:
   - Capture a WPA handshake for cracking.

4. **Crack WPA Handshake**:
   - Crack the captured WPA handshake using a wordlist.

---

## 🛡️ Defense Measures

After simulating attacks, learn how to protect your network:
- Use **WPA3** encryption for enhanced security.
- Disable **WPS** (Wi-Fi Protected Setup).
- Enable **802.11w** to protect management frames.
- Set a strong and unique Wi-Fi password.
- Regularly monitor your network for suspicious devices.

---

## 🌐 Connect with Me

Follow me on Instagram or support my work by buying me a coffee!

[![Instagram](https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://instagram.com/dannyk_739)


---

## ⚠️ Disclaimer

This tool is for **ethical hacking** and **educational purposes only**. Do not use it on networks you do not own or have permission to test.

