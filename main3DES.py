from Cryptodome.Cipher import DES3
from Cryptodome.Random import get_random_bytes

# Criptografar com 3DES
data = b'Texto para cifrar'
key = DES3.adjust_key_parity(get_random_bytes(24))  # 3DES usa chaves de 24 bytes
cipher = DES3.new(key, DES3.MODE_EAX)
nonce = cipher.nonce
ciphertext, tag = cipher.encrypt_and_digest(data)

print("Texto cifrado (3DES):", ciphertext)

# Descriptografar com 3DES
decipher = DES3.new(key, DES3.MODE_EAX, nonce=nonce)
plaintext = decipher.decrypt(ciphertext)
try:
    decipher.verify(tag)
    print("Texto decifrado (3DES):", plaintext)
except ValueError:
    print("A chave ou a mensagem estão corrompidas!")
