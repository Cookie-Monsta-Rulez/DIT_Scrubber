def potfile_cleaner_hash(Pot_File):
    hashes = []
    Hash_Pot_File = Pot_File
    with open(Hash_Pot_File, 'r') as file:
        for line in file:
            hash = line.split(":")[0].strip()
            hashes.append(hash)
    return hashes

def potfile_cleaner_cleartext_and_hash(Pot_File):
    cleartext_and_hash = []
    Cleartext_Pot_File = Pot_File
    with open(Cleartext_Pot_File, 'r') as file:
        for line in file:
            cleartext_and_hash.append(line.strip())
    return cleartext_and_hash

def potfile_cleaner_cleartext_only(Pot_File):
    Cleartext_Pot_File = Pot_File
    Cleartext_Passwords = []
    with open(Cleartext_Pot_File, 'r') as file:
        for line in file:
            if "31d6cfe0d16ae931b73c59d7e0c089c0" in line: # NT Hash for a blank password
                password = line.strip()
                Cleartext_Passwords.append(password)
            else:
                password = line.split(":")[1].strip()
            Cleartext_Passwords.append(password)
    return Cleartext_Passwords