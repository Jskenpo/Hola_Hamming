def calculate_parity(bits, positions):
    parity = 0
    for pos in positions:
        parity ^= bits[pos-1]  # XOR operation
    return parity

def correct_and_decode(block):
    # Posiciones de los bits de paridad
    parity_positions = {
        1: [1, 3, 5, 7, 9, 11],
        2: [2, 3, 6, 7, 10, 11],
        3: [4, 5, 6, 7],
        4: [8, 9, 10, 11]
    }
    
    # Convertir el bloque en una lista de enteros
    hamming_code = [int(bit) for bit in block]
    
    # Detectar el error
    syndrome = 0
    for p in parity_positions:
        if calculate_parity(hamming_code, parity_positions[p]) != 0:
            syndrome += p
    
    # Si el síndrome no es cero, hay un error en la posición 'syndrome'
    if syndrome != 0:
        hamming_code[syndrome-1] ^= 1  # Corregir el bit
    
    # Extraer los bits de datos: posiciones 3, 5, 6, 7, 9, 10, 11
    data_positions = [3, 5, 6, 7, 9, 10, 11]
    data_bits = [hamming_code[pos-1] for pos in data_positions]
    
    return data_bits

# Bloques de Hamming (11,7)
blocks = [
    "10110010000",
    "10110011111",
    "10110011100",
    "10100001001",
    "10011000000",
    "01010010101",
    "01100100101",
    "01110010110",
    "01100000100",
    "10110011111"
]

# Decodificar cada bloque
decoded_message_bits = []
for block in blocks:
    decoded_message_bits.extend(correct_and_decode(block))

# Convertir los bits a caracteres ASCII de 7 bits
ascii_chars = []
for i in range(0, len(decoded_message_bits), 7):
    char_bits = decoded_message_bits[i:i+7]
    char_value = int(''.join(map(str, char_bits)), 2)
    ascii_chars.append(chr(char_value))

# Construir el mensaje
decoded_message = ''.join(ascii_chars)
print(f"Mensaje decodificado: {decoded_message}")
