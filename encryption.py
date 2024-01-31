from cryptography.fernet import Fernet

# Generating a key
key = Fernet.generate_key()

# Fernet cipher using the key
cipher = Fernet(key)

def encrypt_text(text, key):
    cipher_suite = Fernet(key)
    encrypted_text = cipher_suite.encrypt(text.encode())
    return encrypted_text

def decrypt_text(encrypted_text, key):
    cipher_suite = Fernet(key)
    decrypted_text = cipher_suite.decrypt(encrypted_text).decode()
    return decrypted_text

# Example 
if __name__ == "__main__":
    text = input(str("Enter the text to be encrypted \n"))
    
    # Encrypting
    encrypted_text = encrypt_text(text, key)
    print("Encrypted text:", encrypted_text)

    # Decrypting
    decrypted_text = decrypt_text(encrypted_text, key)
    print("Decrypted text:", decrypted_text)
