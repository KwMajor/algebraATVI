# Programa em Python para calcular o determinante de uma matriz 3x3
# usando o método da triangularização (eliminação de Gauss)

# Importamos a biblioteca numpy, que facilita o trabalho com matrizes
import numpy as np

# Exibimos uma mensagem pedindo ao usuário que digite os números da matriz
print("Digite os elementos da matriz 3x3:")

# Criamos uma lista vazia que vai armazenar as linhas da matriz
matriz = []

# Esse laço "for" vai repetir 3 vezes, uma para cada linha da matriz
for i in range(3):
    # Criamos uma lista para guardar os valores da linha atual
    linha = []
    
    # Esse laço interno repete 3 vezes, uma para cada coluna da matriz
    for j in range(3):
        # Pedimos que o usuário digite o valor do elemento na posição [linha,coluna]
        # Usamos "float" para permitir números decimais ou negativos
        valor = float(input(f"Elemento [{i+1},{j+1}]: "))
        
        # Colocamos o valor dentro da lista "linha"
        linha.append(valor)
    
    # Terminada a linha, adicionamos ela dentro da matriz
    matriz.append(linha)

# Convertendo a lista de listas em uma matriz (array) do numpy
# Isso vai facilitar os cálculos posteriores
A = np.array(matriz, dtype=float)

# Mostramos a matriz digitada na tela
print("\nMatriz inserida:")
print(A)

# Criamos uma variável que vai contar quantas vezes trocamos linhas da matriz
# (Cada troca muda o sinal do determinante)
trocas = 0

# Agora começa o processo de triangularização
# Vamos transformar a matriz em uma matriz triangular superior
for i in range(3):  # percorremos as linhas
    
    # Se o elemento da diagonal for zero, precisamos trocar a linha
    if A[i, i] == 0:
        for k in range(i+1, 3):
            if A[k, i] != 0:   # achamos uma linha abaixo com número diferente de zero
                A[[i, k]] = A[[k, i]]  # trocamos as linhas
                trocas += 1            # registramos a troca
                break  # saímos do laço após a troca
    
    # Agora eliminamos os elementos abaixo do pivô (o número da diagonal)
    for k in range(i+1, 3):
        if A[k, i] != 0:
            fator = A[k, i] / A[i, i]  # calculamos o fator de eliminação
            # Subtraímos a linha de cima multiplicada pelo fator da linha de baixo
            A[k] = A[k] - fator * A[i]

# Quando a matriz estiver triangular (todos os elementos abaixo da diagonal forem zero),
# o determinante é simplesmente o produto dos números da diagonal principal
det = np.prod(np.diag(A))

# Mas precisamos corrigir o sinal caso tenha havido troca de linhas
if trocas % 2 != 0:  # se o número de trocas for ímpar
    det *= -1        # invertemos o sinal

# Mostramos a matriz triangular final
print("\nMatriz triangular superior:")
print(A)

# Mostramos o determinante encontrado
print(f"\nDeterminante = {det}")
