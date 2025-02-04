def tem_soma(array, x):
    numeros_vistos = set()
    
    for num in array:
        complemento = x - num
        if complemento in numeros_vistos:
            return True
        numeros_vistos.add(num)
    
    return False

array = [1, 15, 2, 7, 2, 5, 7, 1, 4]

while True:
    entrada = input("Digite um número (ou 'stop' para sair): ")
    if entrada.lower() == 'stop':
        print("Encerrando o programa...")
        break
    
    try:
        x = int(entrada)
        resultado = tem_soma(array, x)
        print(resultado)
    except ValueError:
        print("Entrada inválida! Digite um número inteiro ou 'stop' para sair.")