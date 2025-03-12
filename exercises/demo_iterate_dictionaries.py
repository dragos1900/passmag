import json

def load_json()-> dict:
    try:
        with open ("newjson.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}
    
jdict = load_json()
container = "qbitt"
user = "ddadmin"

for docker in jdict:
    if docker == container:
        print (jdict.get(container,{}).get("password"))

