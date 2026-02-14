import os
import sys

def run_command_with_privilege(command):
    """
    Runs a command with appropriate privileges.
    - If root (uid 0), runs directly.
    - If not root, checks usage of sudo (Kali) vs warning (Termux).
    """
    if os.name == 'nt':
        # On Windows, just run it (likely will fail if tool not found, but avoids sudo error)
        os.system(command)
        return

    if os.geteuid() == 0:
        # Already root
        os.system(command)
    else:
        # Not root
        # Check if 'sudo' is available (simplistic check)
        is_termux = "com.termux" in os.environ.get("PREFIX", "")
        
        if is_termux:
             # Termux usually doesn't have sudo by default unless installed, usually use 'tsu' before starting script
             print(f"[Warning] Not running as root. Command '{command}' might fail.")
             print("Please run the script with 'tsu' or ensure you have privileges.")
             os.system(command) # Try anyway? or fail?
             # Better to assume user ran with tsu if they are in menu.
             # However, if they didn't, we can try prepending 'sudo' if installed, but 'tsu' is shell wrapper.
        else:
            # Assume standard Linux (Kali)
            os.system(f"sudo {command}")
