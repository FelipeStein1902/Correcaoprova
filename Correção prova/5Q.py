from random import randint
import time
#Solução 1
def tem_duplicados(lista):
    start = time.time()
    for i in range(len(lista)):
        for j in range(i+1,(len(lista))):
            if lista[i] == lista[j]:
                end = time.time()
                tempo = end - start
                print(f'O Processamento demorou: {tempo:.7f}')
                return True
    end = time.time()
    tempo = end - start
    print(f'O Processamento demorou: {tempo:.7f}')
    return False

#Solução 2
def tem_duplicados2(lista):
    start = time.time()
    lista_ordenada = sorted(lista)
    for i in range(len(lista_ordenada)-1):
        if lista_ordenada[i] == lista_ordenada[i+1]:
            end = time.time()
            tempo = end - start
            print(f'O Processamento demorou: {tempo:.7f}')
            return True
    end = time.time()
    tempo = end - start
    print(f'O Processamento demorou: {tempo:.7f}')
    return False

#Solução 3
def tem_duplicados3(lista):
    start = time.time()
    elementos_vistos=set()
    for elemento in lista:
        if elemento in elementos_vistos:
            end = time.time()
            tempo = end - start
            print(f'O Processamento demorou: {tempo:.7f}')
            return True
        elementos_vistos.add(elemento)
    end = time.time()
    tempo = end - start
    print(f'O Processamento demorou: {tempo:.7f}')
    return False

lista = []
for i in range(1000000):
    lista.append(randint(1,10000000))

print("Solução 1: ")
print(tem_duplicados(lista))
print('-~-'*20)
print("Solução 2: ")
print(tem_duplicados2(lista))
print('-~-'*20)
print("Solução 3: ")
print(tem_duplicados3(lista))

'''
Respostas certas = C e D
Marquei = B
Só chutei mesmo, não sabia como resolver.
'''