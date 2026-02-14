from rich.panel import Panel

def display_defense_tips(console):
    tips = """
    [bold green]1. Use WPA3 encryption whenever possible.[/bold green]
    [white]WPA3 is the latest security standard and is much harder to crack than WPA2.[/white]

    [bold green]2. Enable 802.11w (Management Frame Protection).[/bold green]
    [white]This prevents deauthentication attacks by encrypting management frames.[/white]

    [bold green]3. Use a strong and complex Wi-Fi password.[/bold green]
    [white]Avoid common words. Use a mix of uppercase, lowercase, numbers, and symbols.[/white]

    [bold green]4. Disable WPS (Wi-Fi Protected Setup).[/bold green]
    [white]WPS has known vulnerabilities that allow attackers to brute-force the PIN.[/white]

    [bold green]5. Regularly monitor your Wi-Fi for unknown devices.[/bold green]
    [white]Check your router's admin panel for unfamiliar MAC addresses.[/white]
    """
    console.print(Panel(tips, title="[bold cyan]Wi-Fi Defense Tips[/bold cyan]", border_style="cyan"))

