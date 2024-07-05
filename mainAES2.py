from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes
from Cryptodome.Util.Padding import pad, unpad

key = get_random_bytes(16)  # Chave de 16 bytes para AES-128
cipher = AES.new(key, AES.MODE_CBC)  # Modo CBC para AES
data = b'Hello World 1234'  # Dados de qualquer tamanho

padded_data = pad(data, AES.block_size)  # Adicionando padding aos dados
ciphertext = cipher.encrypt(padded_data)
print("AES ciphertext:", ciphertext.hex())

# Decifrando
decipher = AES.new(key, AES.MODE_CBC, cipher.iv)
decrypted_data = decipher.decrypt(ciphertext)
plaintext = unpad(decrypted_data, AES.block_size)
print("AES plaintext:", plaintext.decode())
