from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes

# Exemplo com AES no modo EAX
data = b'Texto para cifrar'
key = get_random_bytes(16)  # Gera uma chave aleatória de 128 bits
cipher = AES.new(key, AES.MODE_EAX)
nonce = cipher.nonce
ciphertext, tag = cipher.encrypt_and_digest(data)

print("Texto cifrado:", ciphertext)

# Para decifrar
decipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
plaintext = decipher.decrypt(ciphertext)

try:
    decipher.verify(tag)
    print("Texto decifrado:", plaintext)
except ValueError:
    print("A chave ou a mensagem estão corrompidas!")
