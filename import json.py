from cryptography.fernet import Fernet

# Generate a key
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Encrypt a message
message = b"Hello, this is a secret message."
cipher_text = cipher_suite.encrypt(message)
print(f"Encrypted: {cipher_text}")

# Decrypt the message
plain_text = cipher_suite.decrypt(cipher_text)
print(f"Decrypted: {plain_text.decode()}")