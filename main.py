import psutil
import os
import time

def get_usb_drive_info():
    drives = psutil.disk_partitions()
    for drive in drives:
        if 'removable' in drive.opts or 'cdrom' in drive.opts:
            drive_info = {
                'letter': os.path.splitdrive(drive.device)[0],
                'label': drive.mountpoint
            }
            return drive_info

    return None

if __name__ == "__main__":
    while True:
        usb_info = get_usb_drive_info()
        if usb_info:
            print(f"Clé USB détectée sur le lecteur {usb_info['letter']} avec le nom {usb_info['label']}. Arrêt de la boucle infinie.")
            break
        time.sleep(1)  # Attendre pendant 1 seconde avant de vérifier à nouveau
