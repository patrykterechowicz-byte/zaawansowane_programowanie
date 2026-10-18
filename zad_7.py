from typing import Any

import requests


class Brewery:
    def __init__(self, id: str):
        self.id = id
        self.data: dict[str, Any] | None = None

    def __str__(self):
        data = requests.get(f"https://api.openbrewerydb.org/v1/breweries/{self.id}")
        s = ""
        for key, value in data.json().items():
            s += f"{key}: {value}\n"
        return s[:-2]


if __name__ == "__main__":
    data = requests.get("https://api.openbrewerydb.org/v1/breweries").json()
    for i in range(20):
        print(f"=== {i} ===")
        brewery_id = data[i]["id"]
        brewery = Brewery(brewery_id)
        print(brewery)
