import os
from rich.prompt import Prompt
from richtools import run_command_with_privilege

def crack_handshake(console):
    console.print("[bold red]WPA Handshake Cracker[/bold red]")
    handshake_file = Prompt.ask("Enter WPA handshake file (e.g., handshake-01.cap)")
    wordlist = Prompt.ask("Enter path to wordlist", default="/usr/share/wordlists/rockyou.txt")

    console.print("[bold yellow]Starting cracking process...[/bold yellow]")
    run_command_with_privilege(f"aircrack-ng {handshake_file} -w {wordlist}")

