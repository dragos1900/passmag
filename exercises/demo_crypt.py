from cryptography.fernet import Fernet
import json


key = open("demokey.key","r").read()
print (key)
f=Fernet(key)


def load_json()-> dict:
    try:
        with open ("passwords.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}
    
def save_json(secret_item):
    with open ("passwords.json", "w") as jfile:
        json.dump(secret_item,jfile)

# string encryption
message = "This is the message"

def encrypt_secret(secret) -> str:
    secret = secret.encode()
    return f.encrypt(secret).decode()

#enc_message = f.encrypt(message.encode())
#print (f'This is an ecrypted mesasge: {enc_message}')

def dectrypt_secret (secret)->str:
    return f.decrypt(secret).encode()
    #print (f'This is the same message, decrypted: >>>> {dec_message.decode()}')

def create_secret(docker:str, user: str, passwd:str):
    passwordfile = load_json()
    passwd  = encrypt_secret(passwd)
    if docker not in passwordfile:
        passwordfile[docker] = {"username": user, "password": passwd}
        print (passwordfile[docker])
    save_json(passwordfile)


create_secret ("docsrv04", "ddadmin", "parola123")
create_secret ("docsrv05", "ddadmin", "9238402938")
create_secret ("docsrv06", "ddadmin", "parolofidwsno8374019a123")





