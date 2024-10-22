alpha = float(input('Informe alpha: '))
x = float(input('Informe X: '))
if alpha > 0.1:
    print('Valor inválido para alpha')
else:
    if x < 0:
        print(alpha * x)
    else:
        print(x)

def mostrar_tabela():
    print("| {:^25} | {:^25} |".format("Teste de mesa", "Resultado "))
    print("|" + "-"*27 + "|" + "-"*27 + "|")
    print("| {:<25} | {:<25} |".format("Alpha > 0.1", "Print de valor inválido"))
    print("| {:<25} | {:<25} |".format("Alpha < 0.1 e X < 0", "Print de alpha * X"))
    print("| {:<25} | {:<25} |".format("Alpha < 0.1 e X >= 0", "Print de X"))

mostrar_tabela()

'''
Não informei todas as saidas possiveis, e não fiz a tabela que mostre o teste de mesa.
'''
