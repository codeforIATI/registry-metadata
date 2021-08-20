import json
from os.path import join
import time

import requests


API_BASE_URL = "https://iatiregistry.org/api/action/"


def fetch(path, *args, **kwargs):
    def _fetch(*args, **kwargs):
        print(args, kwargs)
        r = requests.get(*args, **kwargs)
        time.sleep(0.1)
        r.raise_for_status()
        return r

    attempts = 5
    while True:
        try:
            r = _fetch(API_BASE_URL + path, *args, **kwargs)
            break
        except Exception as e:
            attempts -= 1
            if attempts == 0:
                raise e

    return r.json()["result"]


def fetch_publishers():
    ids = fetch("organization_list")

    output = {
        "help": "https://registry.codeforiati.org",
        "success": True,
        "result": [],
    }
    for id_ in ids:
        data = fetch(
            "organization_show",
            params={"id": id_})
        output["result"].append(data)

    with open(join("out", "publisher_list.json"), "w") as fp:
        json.dump(output, fp)


def fetch_datasets():
    page = 1
    page_size = 1000
    output = {
        "help": "https://registry.codeforiati.org",
        "success": True,
        "result": [],
    }
    while True:
        start = page_size * (page - 1)
        data = fetch(
            "package_search",
            params={"start": start, "rows": page_size})["results"]
        if data == []:
            break
        output["result"] += data
        page += 1

    with open(join("out", "dataset_list.json"), "w") as fp:
        json.dump(output, fp)


fetch_publishers()
fetch_datasets()
