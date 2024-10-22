

peso = float(input("Digite seu peso:(kg) "))
altura = float(input("Digite sua altura:(m) "))

imc = peso/ (altura**2)

if imc < 17:
    print(f'O seu imc é de: {imc:.0f} é você esta Muito abaixo do peso!')
elif imc <18.5:
    print(f'O seu imc é de: {imc:.0f} é você esta Abaixo do Peso!')
elif imc <25:
    print(f'O seu imc é de: {imc:.0f} é você possui o Peso Normal!')
elif imc <30:
    print(f'O seu imc é de: {imc:.0f} é você com Sobrepeso!')
elif imc <35:
    print(f'O seu imc é de: {imc:.0f} é você esta com Obesidade Grau I !')
elif imc <40:
    print(f'O seu imc é de: {imc:.0f} é você esta com Obesidade Grau II !')
elif imc >=40:
    print(f'O seu imc é de: {imc:.0f} é você esta com Obesidade Grau III !')

'''
Errei a questão pois não lembrava o calculo de IMC.
'''