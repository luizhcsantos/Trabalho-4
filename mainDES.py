from Cryptodome.Cipher import DES
from Cryptodome.Random import get_random_bytes

# Criptografar com DES
data = b'Texto para cifrar'
key = get_random_bytes(8)  # DES usa chaves de 8 bytes
cipher = DES.new(key, DES.MODE_EAX)
nonce = cipher.nonce
ciphertext, tag = cipher.encrypt_and_digest(data)

print("Texto cifrado (DES):", ciphertext)

# Descriptografar com DES
decipher = DES.new(key, DES.MODE_EAX, nonce=nonce)
plaintext = decipher.decrypt(ciphertext)
try:
    decipher.verify(tag)
    print("Texto decifrado (DES):", plaintext)
except ValueError:
    print("A chave ou a mensagem estão corrompidas!")
