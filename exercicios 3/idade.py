#Leia a idade de 20 pessoas e exiba quantas pessoas são maiores de idade.
cont = 0
for i in range (20):
    idade= int(input('Qual a sua idade? '))
    if idade >=18:
        cont+=1
print(f'Existem {cont} pessoas maiores de idade.')