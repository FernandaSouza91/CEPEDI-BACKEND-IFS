# Carregue uma lista com 20 números inteiros e armazene em outra lista apenas os números pares e outra os ímpares.
Lista_par=[]
lista_impar=[]
lista=[]
for i in range (20):
    numero=int(input('Digite um numero '))
    lista.append(numero)

for i in lista:
    if i % 2 == 0:
        Lista_par.append(i)
    else:
        lista_impar.append(i)
print(f'Numeros ímpares {lista_impar}')
print(f'Numeros pares {Lista_par}')
