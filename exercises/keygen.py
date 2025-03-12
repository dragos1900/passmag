from cryptography.fernet import Fernet

# generate the enc/dec key -this should only run once.

key = Fernet.generate_key()
with open("demokey.key","wb") as keyfile:
      keyfile.write(key)