from cryptography.fernet import Fernet

# Generate kunci baru
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Enkripsi pesan
text = "Halo, ini adalah pesan rahasia!"
cipher_text = cipher_suite.encrypt(text.encode())
print(f"Encrypted: {cipher_text}")

# Dekripsi pesan
decrypted_text = cipher_suite.decrypt(cipher_text).decode()
print(f"Decrypted: {decrypted_text}")
