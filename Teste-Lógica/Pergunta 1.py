numeros = [2, 1, 5, 2, 5, 2, 1, 1, 1, 7, 9, 13, 127, 21]

# Filtra todos os números 1
numeros_um = [num for num in numeros if num == 1]

# Filtra todos os outros números
outros_numeros = [num for num in numeros if num != 1]

# Junta todos os números 1 à esquerda, seguidos dos outros números
numeros = numeros_um + outros_numeros

print(numeros)


