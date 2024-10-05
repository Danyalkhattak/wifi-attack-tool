import scanner
import attacks
import cracker
import defense_tips

def menu():
    print("""
    === Wi-Fi Attack Automation Tool ===
    1. Scan for networks
    2. Deauthentication Attack
    3. Evil Twin Attack
    4. WPA Handshake Capture
    5. Crack WPA Handshake
    6. Defense Tips
    7. Exit
    """)

    choice = input("Select an option: ")
    return choice

def main():
    while True:
        choice = menu()

        if choice == '1':
            scanner.scan_networks()
        elif choice == '2':
            attacks.deauth_attack()
        elif choice == '3':
            attacks.evil_twin_attack()
        elif choice == '4':
            attacks.wpa_handshake_capture()
        elif choice == '5':
            cracker.crack_handshake()
        elif choice == '6':
            defense_tips.display_defense_tips()
        elif choice == '7':
            print("Exiting...")
            break
        else:
            print("Invalid option, try again.")

if __name__ == "__main__":
    main()
