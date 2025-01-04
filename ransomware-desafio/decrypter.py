from cryptography.fernet import Fernet

def load_key():
    # Load the key from the key file
    with open('key.key', 'rb') as key_file:
        key = key_file.read()
    return key

def decrypt_file(filename):
    # Load the key
    key = load_key()
    
    # Create a Fernet instance with the key
    f = Fernet(key)
    
    # Read the encrypted data
    with open(filename, 'rb') as file:
        encrypted_data = file.read()
    
    # Decrypt the data
    decrypted_data = f.decrypt(encrypted_data)
    
    # Write the decrypted data back to the file
    with open(filename, 'wb') as file:
        file.write(decrypted_data)

if __name__ == "__main__":
    decrypt_file('test.txt')
    print('File has been decrypted')