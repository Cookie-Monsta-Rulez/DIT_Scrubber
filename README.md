# DIT_Scrubber
A python program to efficiently see what hashes in a DIT have been cracked by Hashcat. 

![image](https://github.com/user-attachments/assets/abd6c8f5-9cab-494e-ac27-643a0cad37a2)

This program takes an NTDS.dit file (or any files that have hashes in them that are compatible with Hashcat) and uses the Hashcat potfile (either specified or default path) and will append the cleartext credentials to the hashes in the target file. It can also provide a count of password occurences and an overall total of cracked passwords in an NTDS.dit file!

## Installation

Windows:
```
git clone --recursive https://github.com/Cookie-Monsta-Rulez/DIT_Scrubber.git 
cd DIT_Scrubber
python3 -m virtualenv venv
venv\scripts\activate.bat
pip install -r requirements.txt
python DIT_Scrubber.py -h
```

Linux: 
```
git clone --recursive https://github.com/Cookie-Monsta-Rulez/DIT_Scrubber.git 
cd DIT_Scrubber
python3 -m virtualenv venv
source venv\scripts\activate
python3 DIT_Scrubber.py -h
```

## Usage

```
python3 DIT_Scruuber.py -d <path to ntds.dit file> -p <path to potfile (or uses default path> -o <path to outputted ntds.dit file with cleartext passwords appended> 
```

## Help

The help menu is as follows: 

```
 _____ _          
|_   _| |__   ___ 
  | | | '_ \ / _ \
  | | | | | |  __/
  |_| |_| |_|\___|
                  
      ____ ___ _____ 
     |  _ \_ _|_   _|
     | | | | |  | |  
     | |_| | |  | |  
     |____/___| |_|  
                     
         ____                  _     _               
        / ___|  ___ _ __ _   _| |__ | |__   ___ _ __ 
        \___ \ / __| '__| | | | '_ \| '_ \ / _ \ '__|
         ___) | (__| |  | |_| | |_) | |_) |  __/ |   
        |____/ \___|_|   \__,_|_.__/|_.__/ \___|_|   
                                                     


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
⠀⠀⠀⠀⠀⠀⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
usage: DIT Scrubber -d DIT [-p POTFILE] [-h] [-o OUTFILE] [-C]

Created by Cookie-Monsta-Rulez - This program takes an NTDS.dit file (or any files that have hashes in them that are compatible with Hashcat) and uses the Hashcat potfile (either specified or default path) and will append the
cleartext credentials to the hashes in the target file. It can also provide a count of password occurences and an overall total of cracked passwords in an NTDS.dit file!

options:
  -d DIT, --dit DIT     DIT File
  -p POTFILE, --potfile POTFILE
                        Hashcat potfile
  -h, --help            You're looking at it baby!
  -o OUTFILE, --outfile OUTFILE
                        Output file to store the NTDS.dit file appended with cleartext passwords
  -C, --count           Provides a Count of each Password found within the DIT

Have improvements? Want a feature implemented? Please feel free to submit a pull request!

```

## Support
If you have any suggestions or improvements please feel free to submit a pull request!

## Roadmap
Some features to be implemented: 
- Checking for JohnTheRipper potfiles
- Error handling for non-NTDS.dit hash files (such as Cisco hashes)

## Authors and acknowledgment
This project was made by Cookie-Monsta-Rulez

## Contributions

## Acknowledgements: 




