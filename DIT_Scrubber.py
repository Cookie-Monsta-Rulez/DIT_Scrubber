#!/usr/bin/python3

import sys
import argparse
import fileinput
import re
import shutil
import os
from termcolor import colored
import pyfiglet
from counter import counter
from cleaner import potfile_cleaner_hash, potfile_cleaner_cleartext_and_hash, potfile_cleaner_cleartext_only
from reporter import reporter_docx, reporter_csv
from colorama import Fore, Style

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

def dit_cleaner(*args):
    DIT_File = args[0]
    hashes = args[1]
    cleartext = args[2]
    if (len(args) >= 4):
        Cleartext_DIT_File = args[3]
    else:
        Cleartext_DIT_File = "Cleartext_DIT.ntds"
    # Define the target path
    directory = "Loot" 

    full_path = os.path.join(directory, Cleartext_DIT_File)
    # Create the directory if it doesn't exist
    if not os.path.exists(directory):
        os.makedirs(directory)
    shutil.copy(DIT_File, full_path)
    with open(DIT_File, "r") as file:
        content = file.read()

     # Replace occurrences and update dictionary
    for pattern, replacement in zip(hashes, cleartext):
        content = re.sub(rf"{pattern}:::", replacement, content)  # Replace without counting

# Write the modified content back to the file
    with open(full_path, "w") as file:
        file.write(content)

    print(f"Your freshly scrubbed NTDS.dit is here: {Fore.CYAN}.\{full_path}{Style.RESET_ALL}!")    
    return full_path
    



def main():
    # Establishment of the Arguments for the program
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
    parser.add_argument('-docx', '--docxfile', help='DOCX file to store a report with a count of each password found within the DIT (requires -d/--dit)', required=False)
    parser.add_argument('-csv', '--csvfile', help='CSV file to store a report with a count of each password found within the DIT (requires -d/--dit)', required=False)
    parser.add_argument('-C', '--count', help='Provides a Count of each Password found within the DIT',action="store_true", required=False)
    parser.add_argument('-r', '--reuse', help='Checks to see if any hashes were reused from provided DIT',action="store_true", required=False)
    args = parser.parse_args()
    if len(sys.argv) == 0:
        parser = argparse.ArgumentParser(description='An NTDS.dit file must be specified')
        parser.print_help()
        sys.exit(1)
    # Assignment of the arguments to variables for processing
    DIT_File = args.dit
    if (args.potfile is None and os.geteuid() == 0):
        if os.path.exists("/root/.local/share/hashcat/hashcat.potfile"):
            Pot_File = "/root/.local/share/hashcat/hashcat.potfile"
        else:
            print(colored(f"You are running as Root but no potfile is located in /root/.local/share/hashcat/hashcat.potfile", "red"))
            sys.exit(1)
    elif (args.potfile is None and os.geteuid() != 0):
        if os.path.exists(os.path.expanduser("~/.local/share/hashcat/hashcat.potfile")):
            Pot_File = os.path.expanduser("~/.local/share/hashcat/hashcat.potfile")              
        else:
            print(colored(f"No potfile is located in ~/.local/share/hashcat/hashcat.potfile", "red"))
            sys.exit(1)
    else:
        Pot_File = args.potfile

    previous_DIT = args.reuse
    #if previous_DIT is not None:
    #    password_reuse_checker(DIT_File, previous_DIT)
    print(colored(rf"Using {Pot_File} as the Pot file!", "yellow"))

    # Calling of functions depending on the specified arguments
    hashes = potfile_cleaner_hash(Pot_File)
    cleartext_and_hash = potfile_cleaner_cleartext_and_hash(Pot_File)
    passwords = potfile_cleaner_cleartext_only(Pot_File)
    output_file = args.outfile
    if output_file is not None:
            Cleartext_DIT_File = dit_cleaner(DIT_File, hashes, cleartext_and_hash, output_file)
    else:
        Cleartext_DIT_File = dit_cleaner(DIT_File, hashes, cleartext_and_hash)
        print(Cleartext_DIT_File)
    if args.count:
        password_count = counter(Cleartext_DIT_File, passwords)
    if args.docxfile is not None:
        report_docx_file = args.docxfile
        password_count = counter(Cleartext_DIT_File, passwords)
        reporter_docx(report_docx_file, password_count)
    if args.csvfile is not None:
        report_csv_file = args.csvfile
        password_count = counter(Cleartext_DIT_File, passwords)
        reporter_csv(report_csv_file, password_count)
    return 0;

if __name__ == "__main__":
    main()