# import sys
# print(sys.path)
import requests


class APICall:
    def call(self, method, api_url):
        if method.lower() == "get":
            r = requests.get(api_url)

        match r.status_code:
            case 200 | 201 | 202:
                return r.json()["value"]
            case _:
                raise TypeError("API error")


class TZKUAConcepts(APICall):
    url = "https://wordpress.com/home/tzkuaconcepts.wordpress.com"
    categories = ["software", "dev"]

    def __init__(self, category):
        self.category = category
        if self.category not in self.categories:
            raise TypeError("category options ['software', 'dev']")

    def get(self):
        api_url = f'{self.url}{self.category}'
        return self.call("GET", api_url)
