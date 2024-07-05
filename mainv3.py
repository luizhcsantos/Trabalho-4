# Permutação Inicial (IP)
def initial_permutation(block):
    ip = [58, 50, 42, 34, 26, 18, 10, 2,
          60, 52, 44, 36, 28, 20, 12, 4,
          62, 54, 46, 38, 30, 22, 14, 6,
          64, 56, 48, 40, 32, 24, 16, 8,
          57, 49, 41, 33, 25, 17, 9, 1,
          59, 51, 43, 35, 27, 19, 11, 3,
          61, 53, 45, 37, 29, 21, 13, 5,
          63, 55, 47, 39, 31, 23, 15, 7]
    return [block[i-1] for i in ip]

# Permutação Final (FP)
def final_permutation(block):
    fp = [40, 8, 48, 16, 56, 24, 64, 32,
          39, 7, 47, 15, 55, 23, 63, 31,
          38, 6, 46, 14, 54, 22, 62, 30,
          37, 5, 45, 13, 53, 21, 61, 29,
          36, 4, 44, 12, 52, 20, 60, 28,
          35, 3, 43, 11, 51, 19, 59, 27,
          34, 2, 42, 10, 50, 18, 58, 26,
          33, 1, 41, 9, 49, 17, 57, 25]
    return [block[i-1] for i in fp]

# Expansão E
def expansion_function(block):
    e = [32, 1, 2, 3, 4, 5,
         4, 5, 6, 7, 8, 9,
         8, 9, 10, 11, 12, 13,
         12, 13, 14, 15, 16, 17,
         16, 17, 18, 19, 20, 21,
         20, 21, 22, 23, 24, 25,
         24, 25, 26, 27, 28, 29,
         28, 29, 30, 31, 32, 1]
    return [block[i-1] for i in e]

# Substituição S-box
def s_box_substitution(block):
    s_boxes = [
        # S1
        [[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
         [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
         [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
         [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]],
        # S2
        [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
         [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
         [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
         [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]],
        # S3
        [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
         [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
         [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
         [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]],
        # S4
        [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
         [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
         [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
         [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]],
        # S5
        [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
         [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
         [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
         [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]],
        # S6
        [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
         [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
         [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
         [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]],
        # S7
        [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
         [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
         [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
         [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]],
        # S8
        [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
         [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
         [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
         [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]
    ]

    blocks = [block[i:i + 6] for i in range(0, len(block), 6)]
    result = []

    for i, b in enumerate(blocks):
        row = (b[0] << 1) | b[5]
        col = (b[1] << 3) | (b[2] << 2) | (b[3] << 1) | b[4]
        result.extend([int(x) for x in format(s_boxes[i][row][col], '04b')])

    return result

# Permutação P
def permutation_p(block):
    p = [16, 7, 20, 21, 29, 12, 28, 17,
         1, 15, 23, 26, 5, 18, 31, 10,
         2, 8, 24, 14, 32, 27, 3, 9,
         19, 13, 30, 6, 22, 11, 4, 25]
    return [block[i-1] for i in p]

# Função F
def function_f(r, k):
    expanded_r = expansion_function(r)
    xor_rk = [er ^ kr for er, kr in zip(expanded_r, k)]
    s_box_output = s_box_substitution(xor_rk)
    return permutation_p(s_box_output)

# Gerar subchaves (simplificado para este exemplo)
def generate_subkeys(key):
    subkeys = []
    for i in range(16):
        subkeys.append(key[i:i + 48])
    return subkeys

# Função para cifrar um bloco de 64 bits
def des_encrypt_block(block, key):
    block = initial_permutation(block)
    left, right = block[:32], block[32:]
    subkeys = generate_subkeys(key)

    for k in subkeys:
        new_right = [l ^ r for l, r in zip(left, function_f(right, k))]
        left, right = right, new_right

    return final_permutation(right + left)

# Função para decifrar um bloco de 64 bits
def des_decrypt_block(block, key):
    block = initial_permutation(block)
    left, right = block[:32], block[32:]
    subkeys = generate_subkeys(key)[::-1]

    for k in subkeys:
        new_right = [l ^ r for l, r in zip(left, function_f(right, k))]
        left, right = right, new_right

    return final_permutation(right + left)

# Função de utilidade para converter texto em uma lista de bits
def string_to_bit_list(data):
    return [int(bit) for bit in ''.join(format(byte, '08b') for byte in data.encode())]

# Função de utilidade para converter uma lista de bits em texto
def bit_list_to_string(data):
    return ''.join(chr(int(''.join(map(str, data[i:i + 8])), 2)) for i in range(0, len(data), 8))

# Teste de cifragem e decifragem
key = string_to_bit_list('test_key_')[:56]  # Deve ser ajustado para 56 bits
plaintext = 'HelloDES'

# Converter o texto em bits e adicionar padding se necessário
plaintext_bits = string_to_bit_list(plaintext)
while len(plaintext_bits) % 64 != 0:
    plaintext_bits.append(0)

# Certificar-se de que os blocos estejam corretos
plaintext_blocks = [plaintext_bits[i:i + 64] for i in range(0, len(plaintext_bits), 64)]
ciphertext_blocks = []

for block in plaintext_blocks:
    ciphertext_blocks.extend(des_encrypt_block(block, key))

ciphertext = bit_list_to_string(ciphertext_blocks)
print("Texto cifrado (simplificado DES):", ciphertext)

# Descriptografar
decrypted_blocks = []
for block in [ciphertext_blocks[i:i + 64] for i in range(0, len(ciphertext_blocks), 64)]:
    decrypted_blocks.extend(des_decrypt_block(block, key))

decrypted_text = bit_list_to_string(decrypted_blocks).strip('\x00')
print("Texto decifrado (simplificado DES):", decrypted_text)
