import json
import random

def load_json(name: str):
    with open(f"json/{name}.json") as fh:
        data = json.load(fh)
    
    return data

def cgen():
    return random.choice([
        "is-primary",
        "is-link",
        "is-info",
        "is-warning",
        "is-danger"
    ])
