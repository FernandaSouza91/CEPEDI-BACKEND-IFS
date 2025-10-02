# Crie uma função chamada calcular_imc que receba dois argumentos: peso (em
# kg) e altura (em metros). A função deve calcular e retornar o valor do IMC. A
# fórmula é: IMC = peso / (altura * altura). Crie uma segunda função para realizar a
# classificação do IMC segundo a tabela:

def calcular_imc (p,a):
    imc = p/(a*a)
    return imc


def classificação(imc):
    if imc < 18.5:
        print('Abaixo do peso normal') 
    if imc > 18.5 and imc <24.9:
        print('Peso Normal')
    if imc > 25 and imc < 29.9:
        print('Excesso de peso')
    if imc >30 and imc < 34.9:
        print('Obesidade classe I')
    if imc >35 and imc <39.9:
        print('Obesidade classe II')
    if imc >=40:
        print('Obesidade classe III')


#programa principal
peso=int(input('Digite o peso: '))
altura=float(input('Digite sua altura: '))
imc=calcular_imc(peso,altura)
print(imc)

classificação(imc)
