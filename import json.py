import json

file = "demo.json"


def create_new_file(filename):
    try:
        with open(filename,"r") as jfile:
            return json.load(jfile)
    except FileNotFoundError as fnf:
        print (fnf)
        return {}

create_new_file(file)