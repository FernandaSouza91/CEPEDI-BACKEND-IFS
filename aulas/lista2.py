#Separando números positivos e negativos
list= []
listneg= []
for n1 in range(8):
    n1=int(input('Digite um numero'))
    if n1 >= 0:
        list.append(n1)
    if n1 <0:
        listneg.append(n1)
print(list) 
print(listneg) 

#Encontrando temperatura máxima e mínima
list =[]
temp = []
for i in range(12):
    temp=float(input('Digite uma temperatura '))
    list.append(temp)
print(f' Esse é o valor maximo', max(list))
print(f' Esse é o valor minimo', min(list))


#Usando namedtuple para coordenadas
from collections import namedtuple
coordenadas = namedtuple('coordenadas',['latitude','longitude'])
casa_coordenadas=coordenadas(1,8)
print(casa_coordenadas)
print(casa_coordenadas.latitude)
print(casa_coordenadas.longitude)

