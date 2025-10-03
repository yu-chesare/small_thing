import json
import os
from xxsubtype import bench

import requests
from dotenv import load_dotenv, find_dotenv


class Bookstore:

    def __init__(self):
        with open("config.json") as env_file:
            ev = json.loads(env_file.read())
            self.base_url = ev["BASE_URL"]
            self.authorizaion_url = f"{self.base_url}/api/Login"
            self.username =ev["USERNAME"]
            self.password =ev["PASSWORD"]
            self._token = None


    def authorize(self, username = None, password = None):
        responce = requests.post(url=self.authorizaion_url, json={
            "username":username if username else self.username,
            "password":password if password else self.password})
        print(responce)
        self._token = responce.json()["token"] if responce.status_code == 200 else None
        return responce.status_code

    @staticmethod
    def ensure_authorized(func: requests.Response):
        def wrapper(*args):
            responce = func(*args)
            if responce.status_code == 401:
                args[0].authorize()
                return func(*args)
            else: return responce
        return wrapper

    @ensure_authorized
    def put_book(self):
        responce = requests.put(url=f"{self.base_url}/api/Book", headers={"Authorization": f"bearer {self._token}"})
        return responce



