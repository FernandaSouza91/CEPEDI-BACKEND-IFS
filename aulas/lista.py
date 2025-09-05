#Operação com lista:
minha_lista = [4,5,3,1,6]
for i in range(len(minha_lista)):
    minha_lista[i] = minha_lista[i]**2
print(minha_lista)
minha_lista.append(10)
print(minha_lista)
minha_lista.append([0,1])
print(minha_lista)
minha_lista += [1,2,3]
print(minha_lista)
minha_lista = [1,2]
minha_lista.insert(0,'fernanda')
minha_lista.insert(1,'joao')
print(minha_lista)

#Removendo elemento da lista
minha_lista=[8,22,1,2]
minha_lista.remove(22)
print(minha_lista)

#Usando pop e index
lista=[2,4,5,8,21]
lista.pop(3)
print(lista)
print(lista.index(5))

#Fatias (slicing) em listas
lista = [2,4,5,8,21]
print(lista[1:4])
print(lista[:2])
print(lista[3:])
print(lista[::2])

#Funções úteis em listas
Lista = [1,2,3,1,5,12,14,16]
print(len(Lista))
print(sum(Lista))
print(max(Lista))
print(min(Lista))
print(Lista.count(1))

#Ordenando lista em ordem alfabética
lista = ['Banana','Kiwi','Caju', 'Laranja', 'Uva']
lista.sort()
for fruta in lista:
    print(fruta)

#pergunte quantos numeros a pessoas quer digitar , depois digita os numeros na lista e imprima ao contrario
lista= []
numero = int(input('Quantos numeros voce quer digitar '))
for i in range (numero):
    n1 = int(input('(Qual o numero? '))
    lista.append(n1)
print(lista)
for elemento in reversed(lista):
    print (elemento)
    
