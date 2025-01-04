import os
from cryptography.fernet import Fernet

def generate_key():
    # Generate the key and save it to a file
    key = Fernet.generate_key()
    with open('key.key', 'wb') as key_file:
        key_file.write(key)

def load_key():
    # Load the key from the key file
    with open('key.key', 'rb') as key_file:
        key = key_file.read()
    return key

def encrypt_file(filename):
    # Generate and save the key
    generate_key()
    # Load the key
    key = load_key()
    
    # Create a Fernet instance with the key
    f = Fernet(key)
    
    # Read the file content
    with open(filename, 'rb') as file:
        file_data = file.read()
    
    # Encrypt the data
    encrypted_data = f.encrypt(file_data)
    
    # Write the encrypted data back to the file
    with open(filename, 'wb') as file:
        file.write(encrypted_data)

if __name__ == "__main__":
    encrypt_file('test.txt')
    print('File has been encrypted')