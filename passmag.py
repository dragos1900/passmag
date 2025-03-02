# this is a simple version of the password maanger passmag
import json

PASSWORD_FILE = "passwords.json"

#Load existing passwords or create an empty file
def load_pass ():
    try:
        with open(PASSWORD_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return{}

def save_pass(passwords) -> None:
      with open(PASSWORD_FILE,"w") as file:
            json.dump(passwords, file, indent = 4)

def add_pass(docker, username, password) -> None:
      passwords = load_pass()
      passwords[docker] = {"username": username, "password":password}
      save_pass(passwords)
      print (f"Credentials for container {docker}  was saved!")

def get_pass(docker) -> dict:
      passwords = load_pass()
      if docker in passwords:
            return passwords[docker]
      else:
            return None
      
add_pass("qbitt","ddadmin","oPrefwdf")
add_pass("redis","ddadmin","oPrefwdf432412")
add_pass("grafana","ddadmin","oPr23123efwdf")
add_pass("plex","dragos1900","o312Prefwdf")
add_pass("influxdb","ddadmin","oPrefwfsad3412df")

