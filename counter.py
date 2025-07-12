
def counter(*args):
    Cleartext_DIT_File = args[0]
    cleartext_passwords = args[1]

    password_counts = {password: 0 for password in cleartext_passwords}
    with open(Cleartext_DIT_File, 'r') as file:
        for line in file:
            for password in cleartext_passwords:
                if password is not "":
                    if password in line:
                        password_counts[password] += 1
    return password_counts
