#!/usr/bin/python3

import sys
import argparse
import fileinput
import re
import shutil
import os
from termcolor import colored
import pyfiglet

ascii_art = """
⠀⠀⠀⠀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢀⣾⣿⣿⣿⠷⣆⠀⠀⠀⠀⠀⠀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢸⡿⠿⠿⠏⠀⣿⡇⠀⣠⣶⣿⣿⣿⣯⡙⠻⣦⡀⠀⣀⣤⣤⣄⡀⠀⠀⠀⠀
⠀⠈⢿⣄⣀⣀⣴⠟⠀⣰⣿⣿⣿⣿⣿⣿⣷⠀⠈⣿⣿⣿⣿⣿⣯⠛⢦⡀⠀⠀
⠀⠀⠀⠈⠉⠉⠁⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⢻⣿⣿⣿⣿⣿⠀⢸⣧⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡙⠿⢿⣿⠿⠟⠁⠀⠀⠀⠙⠛⠛⠛⠁⠀⢸⡏⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢷⣀⠀⠀⢀⣠⣴⣶⣶⣦⣄⠀⠀⠀⠀⢴⡟⠀⠀⠀
⠀⠀⠀⣠⣶⣿⡿⠶⣦⣄⠀⠛⠷⣶⣿⣿⣿⣿⣿⣿⣿⣷⡄⠀⠀⠀⢻⣆⠀⠀
⠀⢀⣾⣿⣿⣿⣿⣆⠈⠻⣧⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⢻⡆⠀
⠀⢸⣿⣿⣿⣿⣿⠏⠀⠀⣿⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀⠀⠀⠀⢸⡇⠀
⠀⠈⢿⡉⠛⠋⠁⠀⠀⣴⡟⠀⠸⣿⠻⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀⣼⠇⠀
⠀⠀⠈⠙⣶⣶⣶⣄⠉⠻⣦⠀⠀⠹⣧⡈⠉⠛⠛⠉⠀⠀⠀⠀⠀⠀⣼⠏⠀⠀
⠀⠀⠀⠀⣿⣿⣿⡿⠀⠀⣽⠀⠀⠀⠘⠿⣦⣀⠀⠀⠀⠀⠀⢀⣴⠾⠋⠀⠀⠀
⠀⠀⠀⠀⠻⣯⣄⣀⣠⣴⠟⠀⠀⠀⠀⠀⠈⠉⠛⠛⠒⠚⠛⠉⠁⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀"""

banner = pyfiglet.figlet_format("The\n     DIT\n        Scrubber\n")
print(colored(banner, "red"))
print(ascii_art)
def main_func():
    parser = argparse.ArgumentParser(
                    prog='DIT Scrubber',
                    description='Created by Cookie-Monsta-Rulez - \nThis program takes an NTDS.dit file (or any files that have hashes in them that are compatible with Hashcat) and uses the Hashcat potfile (either specified or default path) and will append the cleartext credentials to the hashes in the target file. It can also provide a count of password occurences and an overall total of cracked passwords in an NTDS.dit file!',
                    epilog='Have improvements? Want a feature implemented? Please feel free to submit a pull request!',
                    add_help=False)
    parser.add_argument('-d', '--dit', help='DIT File', required=True)
    parser.add_argument('-p', '--potfile', help='Hashcat potfile', required=False)
    parser.add_argument('-h', '--help', action='help', default=argparse.SUPPRESS,
                    help='You\'re looking at it baby!')
    parser.add_argument('-o', '--outfile', help='Output file to store the NTDS.dit file appended with cleartext passwords', required=False)
    parser.add_argument('-C', '--count', help='Provides a Count of each Password found within the DIT',action="store_true", required=False)
    args = parser.parse_args()
    if len(sys.argv) == 0:
        parser = argparse.ArgumentParser(description='An NTDS.dit file must be specified')
        parser.print_help()
        sys.exit(1)
    DIT_File = args.dit
    Pot_File = args.potfile
    if (args.potfile is None and os.geteuid() == 0):
        if os.path.exists("/root/.local/share/hashcat/hashcat.potfile"):
            Pot_File = "/root/.local/share/hashcat/hashcat.potfile"
        else:
            print(colored("You are running as Root but no potfile is located in /root/.local/share/hashcat/hashcat.potfile", "red"))
            sys.exit(1)
    else:
        if os.path.exists(os.path.expanduser("~/.local/share/hashcat/hashcat.potfile")):
            Pot_File = os.path.expanduser("~/.local/share/hashcat/hashcat.potfile")              
        else:
            print(colored("No potfile is located in ~/.local/share/hashcat/hashcat.potfile", "red"))
            sys.exit(1)
    print(colored(rf"Using {Pot_File} as the Pot file!", "yellow"))
    hashes = potfile_cleaner_hash(Pot_File)
    cleartext = potfile_cleaner_cleartext(Pot_File)
    output_file = args.outfile
    if output_file is not None:
        if args.count:  # Directly check for True (no need for `== True`)
            dit_cleaner(DIT_File, hashes, cleartext, output_file, args.count)
        else:
            dit_cleaner(DIT_File, hashes, cleartext, output_file)
    else:
        dit_cleaner(DIT_File, hashes, cleartext)

    return 0;

def potfile_cleaner_hash(Pot_File):
    hashes = []
    Hash_Pot_File = Pot_File
    with open(Hash_Pot_File, 'r') as file:
        for line in file:
    	    hash = line.split(":")[0].strip()
    	    hashes.append(hash)
    return hashes

def potfile_cleaner_cleartext(Pot_File):
    cleartext = []
    Cleartext_Pot_File = Pot_File
    with open(Cleartext_Pot_File, 'r') as file:
        for line in file:
            cleartext.append(line.strip())
    return cleartext

def dit_cleaner(*args):
    DIT_File = args[0]
    hashes = args[1]
    cleartext = args[2]
    if (len(args) >= 4):
        Cleartext_DIT_File = args[3]
    else:
        Cleartext_DIT_File = "./Cleartext_DIT.ntds"
    shutil.copy(DIT_File, Cleartext_DIT_File)
    with open(DIT_File, "r") as file:
        content = file.read()

# Replace occurrences

    pattern_counts = {}  # Dictionary to store counts and replaced values

    # Initialize count tracking only if args.count is True
    count_enabled = args.count if hasattr(args, "count") else False
    total_count = 0  # Track total replacements

    # Replace occurrences and update dictionary
    for pattern, replacement in zip(hashes, cleartext):
        if count_enabled:
            content, count = re.subn(rf"{pattern}:::", replacement, content)  # Replace while counting
            total_count += count  # Accumulate total count
        else:
            content = re.sub(rf"{pattern}:::", replacement, content)  # Replace without counting

        pattern_counts[pattern] = {"replacement": replacement, "count": count if count_enabled else "N/A"}

    # Print summary
    for pattern, data in pattern_counts.items():
        print(colored(f"Replaced '{pattern}:::' with '{data['replacement']}' {data['count']} times.", "green"))

    if count_enabled:
        print(colored(f"\nTotal replacements made: {total_count}", "green"))

# Write the modified content back to the file
    with open(Cleartext_DIT_File, "w") as file:
        file.write(content)

    print(f"Your freshly scrubbed NTDS.dit is here: {colored(os.path.abspath(Cleartext_DIT_File), 'red')}!")    
    #print(colored(rf"Your freshly scrubbed NTDS.dit is here: {Cleartext_DIT_File}", "green"))
main_func()
