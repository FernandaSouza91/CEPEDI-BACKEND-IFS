#Crie um programa que peça um número de 1 a 7 e imprima o dia da semana correspondente (1 para Domingo, 2 para Segunda, etc.). Se o número estiver fora do intervalo, exiba "Número inválido".
numero=int(input('Digite um numero '))
if numero == 1:
    print('Domingo')
elif numero == 2:
    print('Segunda')
elif numero == 3:
    print('Terça')
elif numero == 4:
    print('Quarta')
elif numero == 5:
    print('Quinta')
elif numero == 6:
    print('Sexta')
elif numero == 7:
    print('Sábado')
else:
    print('Número inválido')