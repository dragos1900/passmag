# this is a simple version of the password maanger passmag
import json
from cryptography.fernet import Fernet

# passwd file name
PASSWORD_FILE = "passwords.json"

def load_key()-> bytes:
     return open("key.key","rb").read()

fernet = Fernet(load_key())

#Load existing passwords or create an empty file
def load_pass ():
    try:
        with open(PASSWORD_FILE, "r") as file:
            encrypted_data = file.read()
            decrypted_data = fernet.decrypt(encrypted_data.encode()).decode()
            return json.load(decrypted_data)
    except (FileNotFoundError, json.JSONDecodeError):
        return{}

def save_pass(passwords) -> None:
      encrypted_data = fernet.encrypt(json.dumps(passwords).encode()).decode()
      with open(PASSWORD_FILE,"w") as file:
            file.write(encrypted_data)

# Add encrypted password
def add_pass(docker, username, password) -> None:
      passwords = load_pass()
      if docker not in passwords:
            passwords[docker] = {"username": username, "password":password}
            save_pass(passwords)
            print (f"Credentials for container {docker}  was saved!")
      else:
           print (f'Credentials for container {docker} already stored. Nothing changed.')

# Retrieve and decrypt passwords
def get_pass(docker) -> dict:
      passwords = load_pass()
      if docker in passwords:
            #print (type(passwords[docker]))
            return passwords[docker]
      else:
            return None
      
add_pass("qbitt","ddadmin","oPrefwdf432vsduy6")
add_pass("redis2","ddadmin","oPrgdfgrtefwdf432412")
add_pass("grafana","ddadmin","oPr23123efwdf")
add_pass("plex","dragos1900","o312Prefwdf")
add_pass("influxdb3","ddadmin","o32312Prefwfsad3412df")
add_pass("grafana2","ddadmin","oPrfsre23123efwdf")
add_pass("plex2","dragos1900","o312Pretrfwdf")
add_pass("influxdb3.1","ddadmin","o32312r534Prefwfsad3412df")

get_pass('qbitt')
get_pass('plex2')
get_pass('influx3.1')
get_pass('redis')
get_pass('redis2')