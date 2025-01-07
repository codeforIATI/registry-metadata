import csv
import json
from os.path import join
import time

import requests


API_BASE_URL = "https://iatiregistry.org/api/action/"

REQUEST_HEADERS = {
    "User-Agent": "CodeForIATI registry metadata https://github.com/codeforIATI/registry-metadata"
}

def fetch(path, *args, **kwargs):
    def _fetch(*args, **kwargs):
        print(args, kwargs)
        r = requests.get(headers=REQUEST_HEADERS, *args, **kwargs)
        time.sleep(0.1)
        r.raise_for_status()
        return r

    attempts = 5
    while True:
        try:
            r = _fetch(API_BASE_URL + path, *args, **kwargs)
            break
        except Exception as e:
            print("Retrying in 5 seconds")
            time.sleep(5)
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
            params={
                "id": id_,
                "show_historical_publisher_names": "true",
            })
        output["result"].append(data)

    with open(join("out", "publisher_list.json"), "w") as fp:
        json.dump(output, fp)

    return output["result"]


def generate_mappings(publishers):
    mappings = {
        x["name"]: list(set([y["old_name"] for y in x["historical_publisher_names"]]))
        for x in publishers
        if x["historical_publisher_names"]
    }

    with open(join("out", "registry_id_relationships.csv"), "w") as fh:
        writer = csv.DictWriter(fh, fieldnames=["current_registry_id", "previous_registry_id"])
        writer.writeheader()
        for current_name, old_names in mappings.items():
            for old_name in old_names:
                _ = writer.writerow({
                    "current_registry_id": current_name,
                    "previous_registry_id": old_name,
                })

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


publishers = fetch_publishers()
generate_mappings(publishers)
fetch_datasets()
