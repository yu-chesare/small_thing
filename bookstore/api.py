import json
import os

import requests
from dotenv import load_dotenv, find_dotenv


class Bookstore:

    def __init__(self):
        with open("config.json") as env_file:
            ev = json.loads(env_file.read())
            self.authorizaion_url = f"{ev["BASE_URL"]}/api/Login"
            self.username =ev["USERNAME"]
            self.password =ev["PASSWORD"]


    def authorize(self, username = None, password = None):
        responce = requests.post(url=self.authorizaion_url, json={
            "username":username if username else self.username,
            "password":password if password else self.password})
        print(responce.status_code)
        print(responce.content)
        self._token = responce.json()["token"] if responce.status_code == 200 else None
        return responce.status_code


