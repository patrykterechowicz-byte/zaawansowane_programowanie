from typing import Any
import argparse

import requests


def parse_args():
    parser = argparse.ArgumentParser()
    _ = parser.add_argument("--city", default=None)
    return parser.parse_args()


class Brewery:
    def __init__(self, id: str):
        self.id: str = id

        data = requests.get(
            f"https://api.openbrewerydb.org/v1/breweries/{self.id}"
        ).json()
        self._data: dict[str, Any] = data
        self.name: str = data["name"]
        self.brewery_type: str = data["brewery_type"]
        self.address_1: str = data["address_1"]
        self.address_2: str = data["address_2"]
        self.address_3: str = data["address_3"]
        self.city: str = data["city"]
        self.state_province: str = data["state_province"]
        self.postal_code: str = data["postal_code"]
        self.country: str = data["country"]
        self.longitude: str = data["longitude"]
        self.latitude: str = data["latitude"]
        self.phone: str = data["phone"]
        self.website_url: str = data["website_url"]
        self.state: str = data["state"]
        self.street: str = data["street"]

    def __str__(self):
        s = ""
        for key, value in self._data.items():
            s += f"{key}: {value}\n"
        return s[:-2]


if __name__ == "__main__":
    args = parse_args()

    if hasattr(args, "city") and args.city is not None:
        breweries: list = requests.get(
            f"https://api.openbrewerydb.org/v1/breweries/?by_city={args.city}"
        ).json()
    else:
        breweries: list = requests.get(
            "https://api.openbrewerydb.org/v1/breweries"
        ).json()

    for i in range(20):
        try:
            brewery_id = breweries[i]["id"]
        except IndexError:
            break
        print(f"=== {i} ===")
        brewery = Brewery(brewery_id)
        print(brewery)
