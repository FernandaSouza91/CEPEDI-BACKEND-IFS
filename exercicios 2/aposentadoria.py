#Desenvolva um programa que leia a idade e o tempo de serviço de um trabalhador e escreva se ele pode ou não se aposentar. As condições para aposentadoria são:  ter pelo menos 65 anos, ou ter trabalhado pelo menos 30 anos, ou ter pelo menos 60 anos e ter trabalhado pelo menos 25 anos.

idade=int(input('Digite a sua idade: '))
tempo=int(input('Digite o tempo de serviço: '))
if idade >= 60 and tempo >= 25:
    print('Pode se aposentar.')
elif idade >= 65 :
    print('Pode se aposentar. ')
elif tempo >= 30:
    print('Pode se aposentar.')
else:
    print('Aposentadoria não permitida')