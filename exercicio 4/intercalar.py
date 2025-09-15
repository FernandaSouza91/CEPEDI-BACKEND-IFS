#Faça um programa que leia duas listas com 10 elementos cada. Gere uma terceira lista, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.
lista1=[]
lista2=[]
lista3=[]
for i in range(10):
    n1=int(input('\nDigite um numero para a primeira lista '))
    lista1.append(n1)

for i in range(10):
    n2=int(input('Digite um numero para a segunda lista '))
    lista2.append(n2)
for i in range(10):
    lista3.append(lista1[i])
    lista3.append(lista2[i])

print(lista3)
