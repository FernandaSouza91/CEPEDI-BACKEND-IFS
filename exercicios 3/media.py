#Elaborar um programa que apresente o resultado da soma e da média aritmética dos valores pares situados entre 40 e 70 (inclusive)
soma = 0
cont = 0
for i in range (40,71,1):
    if i%2==0:
        soma += i
        cont += 1
        media = soma/cont        
print (f'O valor da soma é {soma}')
print (f'O valor da media aritimedica é {media}')