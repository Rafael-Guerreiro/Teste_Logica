def completar_intervalo(arr):
    max_num = max(arr)  # Encontra o maior número no array
    intervalo_completo = set(range(max_num + 1))  # Cria um conjunto com números de 0 a max_num
    
    numeros_faltantes = intervalo_completo - set(arr)  # Encontra os números ausentes
    arr.extend(numeros_faltantes)  # Adiciona os números faltantes ao array original
    
    return sorted(arr)  # Retorna o array ordenado

# Testando a função
array = [9, 2, 3, 1, 4]
resultado = completar_intervalo(array)
print(resultado)
