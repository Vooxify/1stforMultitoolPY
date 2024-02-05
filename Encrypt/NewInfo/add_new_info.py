import getpass

from cryptography.fernet import Fernet

from Encrypt.NewInfo.GenerateKeys.generate_keys import generate_key


def z(var):
    f = Fernet(var)
    return f
def dictionnary_file_encryption():

    var = generate_key()
    keys = {}
    temp_var_keys = b""
    for items in var:

        if isinstance(items, int):
            items = bytes([items])

        if items == b"\n":

            if temp_var_keys:
                keys[len(keys) + 1] = temp_var_keys.decode()

            temp_var_keys = b""

        else:
            temp_var_keys += items

    if temp_var_keys:
        keys[len(keys) + 1] = temp_var_keys.decode()

    for key in keys:
        keys[key] = keys[key].replace("\n", "")

    return keys


def encrypt():
    print("ATTENTION ! PLEASE DONT PRESS CTRL + C OR THE PROGRAM CRASHING !!")
    input_domain = input("For who website you want to register ? : ").encode()
    input_username = input("Username : ").encode()
    input_password = getpass.getpass("Password : ").encode()
    dico = dictionnary_file_encryption()
    last_key_dico = str(list(dico.values())[-1])
    f = z(last_key_dico)

    encrypted_domain = f.encrypt(input_domain)
    encrypted_username = f.encrypt(input_username)
    encrypted_password = f.encrypt(input_password)

    return encrypted_username.decode(), encrypted_password.decode(), encrypted_domain.decode()


