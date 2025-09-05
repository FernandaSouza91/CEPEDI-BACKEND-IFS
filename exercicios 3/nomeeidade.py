# Leia o nome e a idade de 10 pessoas e exiba o nome da pessoa mais nova.
menorid = None
nomemaisnovo = None
for i in range(1,11):
    print(f'---{i}° PESSOA---')
    nome=str(input('Qual o seu nome? '))
    idade = int(input('Qual a sua idade? '))
    if menorid is None or idade < menorid:
        nomemaisnovo = nome
        menorid = idade
print(f' A pessoas mais nova tem {menorid} ano(s) e seu nome  é {nomemaisnovo}.')