import os
from richtools import run_command_with_privilege

def scan_networks(console):
    console.print("[bold green]Scanning for networks... (Press CTRL+C to stop)[/bold green]")
    try:
        run_command_with_privilege("airmon-ng start wlan0")
        run_command_with_privilege("airodump-ng wlan0mon")
    except KeyboardInterrupt:
        console.print("\n[bold yellow]Stopping scan...[/bold yellow]")
        run_command_with_privilege("airmon-ng stop wlan0mon")

