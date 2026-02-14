import sys
import os
from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel
from rich import print as rprint
import time

# Importing local modules
import scanner
import attacks
import cracker
import defense_tips

console = Console()

def check_root():
    """Checks if the script is running as root."""
    if os.name == 'nt':
        return True # Windows doesn't use sudo the same way, assuming user knows what they are doing or it's a test.
    
    if os.geteuid() != 0:
        console.print(Panel("[bold red]Run this tool as root![/bold red]\n[yellow]Use 'sudo python3 main.py' (Kali) or 'tsu' then 'python3 main.py' (Termux)[/yellow]", title="Permission Error", expand=False))
        return False
    return True

def banner():
    console.print(Panel.fit("[bold cyan]Wi-Fi Attack Automation Tool[/bold cyan]\n[green]Optimized for Kali Linux & Termux[/green]", border_style="bold blue"))

def menu():
    banner()
    console.print("[bold yellow]1.[/bold yellow] Scan for networks")
    console.print("[bold yellow]2.[/bold yellow] Deauthentication Attack")
    console.print("[bold yellow]3.[/bold yellow] Evil Twin Attack")
    console.print("[bold yellow]4.[/bold yellow] WPA Handshake Capture")
    console.print("[bold yellow]5.[/bold yellow] Crack WPA Handshake")
    console.print("[bold yellow]6.[/bold yellow] Defense Tips")
    console.print("[bold yellow]7.[/bold yellow] Exit")
    
    choice = Prompt.ask("[bold cyan]Select an option[/bold cyan]", choices=["1", "2", "3", "4", "5", "6", "7"])
    return choice

def main():
    if not check_root():
        if os.name != 'nt': # Only exit if not on windows (for testing purposes on windows)
            sys.exit(1)
            
    while True:
        try:
            console.clear()
            choice = menu()

            if choice == '1':
                console.clear()
                scanner.scan_networks(console)
            elif choice == '2':
                console.clear()
                attacks.deauth_attack(console)
            elif choice == '3':
                console.clear()
                attacks.evil_twin_attack(console)
            elif choice == '4':
                console.clear()
                attacks.wpa_handshake_capture(console)
            elif choice == '5':
                console.clear()
                cracker.crack_handshake(console)
            elif choice == '6':
                console.clear()
                defense_tips.display_defense_tips(console)
            elif choice == '7':
                console.print("[bold green]Exiting...[/bold green]")
                break
            
            input("\nPress Enter to return to menu...")
            
        except KeyboardInterrupt:
            console.print("\n[bold red]Interrupted by user. Exiting...[/bold red]")
            break
        except Exception as e:
            console.print(f"\n[bold red]An error occurred: {e}[/bold red]")
            input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
