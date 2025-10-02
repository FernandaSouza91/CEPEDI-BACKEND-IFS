#Escreva uma função chamada somar_tudo que possa receber um número variável de argumentos numéricos e retorne a soma de todos eles.

def somar_tudo(*num):
    soma=sum(num)
    return soma



#princiapl
lista=[]
n1=int(input('Digite a quantidade de numeros'))
for i in range(n1):
    num=int(input('Digite um numero: '))
    lista.append(num)

somar_tudo(*lista)
print(somar_tudo(*lista))