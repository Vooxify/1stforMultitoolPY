from Encrypt.NewInfo.add_new_info import *
from requiered_usb import requiered_usb

usb_letter, usb_label = requiered_usb()
def add_encrypted_datas():
        encrypted_username, encrypted_password, encrypted_domain = encrypt()
        with open(f"C:\\Pass\\encrypted_datas.key", "a") as encrypted_file_data:
            encrypted_file_data.write(
                f"{encrypted_domain}\n{encrypted_username}\n{encrypted_password}\n")
        encrypted_file_data.close()
