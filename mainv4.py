import binascii

def permutar(bloco, tabela):
    return [bloco[x - 1] for x in tabela]

def xor(t1, t2):
    return [int(x) ^ int(y) for x, y in zip(t1, t2)]

def deslocar_esquerda(bloco, n):
    return bloco[n:] + bloco[:n]

def bits_para_bytes(s):
    return bytes(int(s[i:i+8], 2) for i in range(0, len(s), 8))

def bytes_para_bits(b):
    return ''.join(f'{byte:08b}' for byte in b)

def pad(text):
    pad_len = 8 - len(text) % 8
    return text + chr(pad_len) * pad_len

def unpad(text):
    pad_len = ord(text[-1])
    return text[:-pad_len]

IP = [58, 50, 42, 34, 26, 18, 10, 2,
      60, 52, 44, 36, 28, 20, 12, 4,
      62, 54, 46, 38, 30, 22, 14, 6,
      64, 56, 48, 40, 32, 24, 16, 8,
      57, 49, 41, 33, 25, 17, 9, 1,
      59, 51, 43, 35, 27, 19, 11, 3,
      61, 53, 45, 37, 29, 21, 13, 5,
      63, 55, 47, 39, 31, 23, 15, 7]

FP = [40, 8, 48, 16, 56, 24, 64, 32,
      39, 7, 47, 15, 55, 23, 63, 31,
      38, 6, 46, 14, 54, 22, 62, 30,
      37, 5, 45, 13, 53, 21, 61, 29,
      36, 4, 44, 12, 52, 20, 60, 28,
      35, 3, 43, 11, 51, 19, 59, 27,
      34, 2, 42, 10, 50, 18, 58, 26,
      33, 1, 41, 9, 49, 17, 57, 25]

E = [32, 1, 2, 3, 4, 5,
     4, 5, 6, 7, 8, 9,
     8, 9, 10, 11, 12, 13,
     12, 13, 14, 15, 16, 17,
     16, 17, 18, 19, 20, 21,
     20, 21, 22, 23, 24, 25,
     24, 25, 26, 27, 28, 29,
     28, 29, 30, 31, 32, 1]

S_BOX = [
    [[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
     [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
     [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
     [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]],

    [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
     [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
     [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
     [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]],

    [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
     [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
     [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
     [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]],

    [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
     [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
     [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
     [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]],

    [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
     [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
     [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
     [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]],

    [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
     [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
     [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
     [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]],

    [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
     [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
     [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
     [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]],

    [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
     [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
     [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
     [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]
]

P = [16, 7, 20, 21,
     29, 12, 28, 17,
     1, 15, 23, 26,
     5, 18, 31, 10,
     2, 8, 24, 14,
     32, 27, 3, 9,
     19, 13, 30, 6,
     22, 11, 4, 25]

def funcao_feistel(direita, chave):
    direita_expandida = permutar(direita, E)
    resultado_xor = xor(direita_expandida, chave)
    substituido = []
    for i in range(8):
        bloco = resultado_xor[i*6:(i+1)*6]
        linha = int(f'{bloco[0]}{bloco[5]}', 2)
        coluna = int(''.join(map(str, bloco[1:5])), 2)
        substituido.extend(list(f'{S_BOX[i][linha][coluna]:04b}'))
    return permutar(substituido, P)

def des_criptografar(texto_plano, chave):
    texto_plano = pad(texto_plano)
    bits_texto_plano = bytes_para_bits(texto_plano.encode('utf-8'))
    bits_chave = bytes_para_bits(chave.encode('utf-8'))
    bits_texto_plano = bits_texto_plano.ljust(64, '0')
    bits_chave = bits_chave.ljust(64, '0')
    texto_permutado = permutar(bits_texto_plano, IP)
    esquerda, direita = texto_permutado[:32], texto_permutado[32:]
    
    for i in range(16):
        nova_direita = xor(esquerda, funcao_feistel(direita, bits_chave))
        esquerda = direita
        direita = nova_direita
    
    texto_combinado = direita + esquerda
    texto_criptografado = permutar(texto_combinado, FP)
    return bits_para_bytes(''.join(map(str, texto_criptografado)))

def des_descriptografar(texto_criptografado, chave):
    bits_texto_criptografado = bytes_para_bits(texto_criptografado)
    bits_chave = bytes_para_bits(chave.encode('utf-8'))
    bits_chave = bits_chave.ljust(64, '0')
    texto_permutado = permutar(bits_texto_criptografado, IP)
    esquerda, direita = texto_permutado[:32], texto_permutado[32:]
    
    for i in range(15, -1, -1):
        nova_esquerda = xor(direita, funcao_feistel(esquerda, bits_chave))
        direita = esquerda
        esquerda = nova_esquerda
    
    texto_combinado = direita + esquerda
    texto_descriptografado = permutar(texto_combinado, FP)
    texto_descriptografado_bytes = bits_para_bytes(''.join(map(str, texto_descriptografado)))
    
    try:
        texto_final = unpad(texto_descriptografado_bytes.decode('utf-8', errors='ignore'))
        return texto_final
    except Exception as e:
        return texto_descriptografado_bytes.decode('utf-8', errors='ignore')

# Teste
texto_plano = "testeabc12345"
chave = "chave123"

print("Texto original:", texto_plano)

criptografado = des_criptografar(texto_plano, chave)
print("Texto criptografado:", criptografado.hex())

descriptografado = des_descriptografar(criptografado, chave)
print("Texto descriptografado:", descriptografado)
