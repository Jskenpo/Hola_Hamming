def calculate_parity(bits, positions):
    parity = 0
    for pos in positions:
        parity ^= bits[pos-1]  # XOR operation
    return parity

# Representación de "A"
data_bits = [0, 1, 0, 0, 0, 0, 1]

# Posiciones de los bits de paridad
parity_positions = {
    1: [1, 3, 5, 7, 9, 11],
    2: [2, 3, 6, 7, 10, 11],
    3: [4, 5, 6, 7],
    4: [8, 9, 10, 11]
}

# Insertamos los bits de datos en las posiciones correspondientes
hamming_code = [0] * 11
data_positions = [3, 5, 6, 7, 9, 10, 11]
for i, bit in zip(data_positions, data_bits):
    hamming_code[i-1] = bit

# Calculamos los bits de paridad
for p in parity_positions:
    hamming_code[p-1] = calculate_parity(hamming_code, parity_positions[p])

print(f"Bits de datos: {data_bits}")
print(f"Hamming code (11,7): {''.join(map(str, hamming_code))}")



## Parte 2 
import random

# Introducimos un error en una posición aleatoria
error_position = random.randint(0, 10)
hamming_code[error_position] ^= 1  # Flip the bit

print(f"Error introducido en la posición: {error_position + 1}")
print(f"Codigo con error: {''.join(map(str, hamming_code))}")

# Detectar el error
syndrome = 0
for p in parity_positions:
    if calculate_parity(hamming_code, parity_positions[p]) != 0:
        syndrome += p

print(f"Síndrome: {syndrome}")

# Comprobamos si el síndrome es igual a la posición del error
print(f"El error se encuentra en la posición: {syndrome}")
