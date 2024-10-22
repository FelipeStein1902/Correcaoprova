def some_diagonal_principal(matriz):
    soma = 0
    for i in range(len(matriz)):
        soma += matriz[i][i]
    return soma

def some_diagonal_principal2(matriz):
    soma = 0
    for i in range(len(matriz)):
        soma += matriz[i][-i]
    return soma

def some_diagonal_principal3(matriz):
    soma = 0
    for linha in matriz:
        for elemento in linha:
            soma += elemento
    return soma
def some_diagonal_principal4(matriz):
    soma = 0
    for i in range(len(matriz)):
        soma += matriz[i][len(matriz)-i-1]
    return soma

def some_diagonal_principal5(matriz):
    soma = 0
    for i in range(len(matriz)):
        soma +=matriz[len(matriz)-i-1][i]
    return soma

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(f'Soma solução 1: {some_diagonal_principal(matriz)}')
print('-~-'*10)
print(f'Soma solução 2: {some_diagonal_principal2(matriz)}')
print('-~-'*10)
print(f'Soma solução 3: {some_diagonal_principal3(matriz)}')
print('-~-'*10)
print(f'Soma solução 4: {some_diagonal_principal4(matriz)}')
print('-~-'*10)
print(f'Soma solução 5: {some_diagonal_principal5(matriz)}')
print('-~-'*10)

'''
Resposta certa = A
Marquei = B
Errei pois não vi a o menos do lado do (i), isso que dar querer fazer a prova rapido...
'''