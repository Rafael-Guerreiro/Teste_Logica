class No:
    def __init__(self, palavra):
        self.palavra = palavra
        self.esquerdo = None
        self.direito = None

def buscar_palavra(no, palavra, caminho=None):
    # Se o no for None, a palavra não foi encontrada
    if no is None:
        return None
    
    # Se o no atual for a palavra que estamos buscando
    if no.palavra == palavra:
        if caminho is None:
            caminho = []
        caminho.append(no.palavra)
        return caminho
    
    # Caso contrário, procurar na árvore
    if caminho is None:
        caminho = []
    caminho.append(no.palavra)
    
    # Recursão para a esquerda e para a direita
    caminho_esquerda = buscar_palavra(no.esquerdo, palavra, caminho.copy())
    if caminho_esquerda:
        return caminho_esquerda

    caminho_direita = buscar_palavra(no.direito, palavra, caminho.copy())
    return caminho_direita

# Construindo a árvore binária:
raiz = No('Maçã')
raiz.esquerdo = No('Pera')
raiz.direito = No('Morango')

# Subárvore à esquerda de "Pera"
raiz.esquerdo.esquerdo = No('Abacaxi')
raiz.esquerdo.esquerdo.esquerdo = No('Laranja')
raiz.esquerdo.esquerdo.esquerdo.esquerdo = No('Banana')
raiz.esquerdo.esquerdo.esquerdo.direito = No('Cebola')

# Subárvore à direita de "Pera"
raiz.esquerdo.direito = None

# Subárvore à esquerda de "Morango"
raiz.direito.esquerdo = No('Goiaba')

# Subárvore à direita de "Morango"
raiz.direito.direito = No('Limão')

# Loop para permitir múltiplas buscas
while True:
    # Entrada do usuário para a palavra que deseja procurar
    palavra_procurada = input("Digite o nome da fruta que você deseja procurar (ou 'sair' para encerrar): ")

    if palavra_procurada.lower() == 'sair':
        print("Saindo do programa.")
        break

    # Buscando a palavra na árvore
    caminho = buscar_palavra(raiz, palavra_procurada)

    if caminho:
        print(f'Caminho até {palavra_procurada}: {" -> ".join(caminho)}')
    else:
        print(f'Palavra {palavra_procurada} não encontrada.')