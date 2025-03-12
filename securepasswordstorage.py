from cryptography.fernet import Fernet
import json

#generate the enc/dec key and store it in a file - this is one time 
"""
key = Fernet.generate_key()
fernet = Fernet(key)

with open ("enckey.key","wb") as kfile:
    kfile.write(key)
"""
keyfilesore:str = "enckey.key"

# Load encryption/decryption key
def load_key(keyfile: str)-> classmethod:
    return open(keyfile,"r").read()

token = Fernet(load_key(keyfilesore))
print (type(token))


PASSSTORE = "secretstorage.json" ## here is the secrets storage

# encrypt passwords function
def pass_encryption(password:bytes) -> str:
    return token.encrypt(password).decode()

# decrypt passwords function
def pass_decrypt(passwd:str) -> str:
    return token.decrypt(passwd.encode()).decode()

def load_passwordstore () -> object:
    try:
        with open (PASSSTORE,"rb") as storage:
            return json.load(storage)
    except FileNotFoundError as fnf:
        print(f'>>>>> {fnf} <<<<<')
        return {}

def save_secrets(secrets_dictionary:dict):
    with open(PASSSTORE,"w") as secrets_file:
        json.dump(secrets_dictionary,secrets_file)
    print ("## >>Information safetly saved!<< ###")


def create_pass() -> None:
    secretsfile = load_passwordstore()
    docker = input(f"Please enter the docker name: ")
    user = input(f"Please enter the username: ")
    passwd = input(f"Please enter the password: ")
    
    if docker not in (secretsfile) or user not in secretsfile[docker]:
        enc_pass = pass_encryption(passwd.encode()) # password needs to be uin bytes to be encrypted
        secretsfile[docker] = {"username": user,"password":enc_pass}
        #print (secretsfile)
    else:
        credentials =  input(f'Credentials for user {user} for container {docker} already exists. Update it (Yes/No): ')
        if credentials.upper  == 'YES' or credentials.upper == "Y":
            enc_pass = pass_encryption(passwd.encode()) # password needs to be uin bytes to be encrypted
            secretsfile[docker] = {"username": user,"password":enc_pass}
        
        else:
            print (f'Nothing changed for container {docker}.')
    save_secrets(secretsfile)

def get_pass(docker: str, user: str):
    pass_store: dict = load_passwordstore()
    for container in pass_store:
        if docker == container and pass_store.get(container,{}).get("username") == user:
            secret: str = pass_store.get(container, {}).get("password")
            decrypted_message = pass_decrypt(secret)
            print (f'Password requested for user {user} in containter {docker} is: {decrypted_message}' )
        else:
            print (f'There are no credentials stored for user: {user} of container {docker}:')

create_pass()
get_pass ("qbitt","ddadmin")
get_pass ("docksrv01","ddadmin")