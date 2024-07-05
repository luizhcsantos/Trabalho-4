from Cryptodome.Cipher import Blowfish
from Cryptodome.Random import get_random_bytes
from Cryptodome.Util.Padding import pad, unpad

# Criptografar com Blowfish
data = b'Texto para cifrar'
key = get_random_bytes(16)  # Blowfish usa chaves de 4 a 56 bytes
cipher = Blowfish.new(key, Blowfish.MODE_EAX)
nonce = cipher.nonce
ciphertext, tag = cipher.encrypt_and_digest(pad(data, Blowfish.block_size))

print("Texto cifrado (Blowfish):", ciphertext)

# Descriptografar com Blowfish
decipher = Blowfish.new(key, Blowfish.MODE_EAX, nonce=nonce)
plaintext = unpad(decipher.decrypt(ciphertext), Blowfish.block_size)
try:
    decipher.verify(tag)
    print("Texto decifrado (Blowfish):", plaintext)
except ValueError:
    print("A chave ou a mensagem estão corrompidas!")
