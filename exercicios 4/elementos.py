# Fazer um programa para ler uma lista de 5 elementos, e, em seguida, mostrar a posição(não o índice) onde se encontram o maior e o menor valor e seus respectivos valores.
numeros = []
maior=0
menor=0
for i in range(5):
    elemento=int(input('Digite um numero '))
    numeros.append(elemento)
maior = max(numeros)
menor = min(numeros)
index_maior = numeros.index(maior)+1
index_menor = numeros.index(menor)+1

print(f'O maior número está na {index_maior}° posição e seu valor é {maior}')
print(f'O menor número está na {index_menor}° posição e seu valor é {menor}')
