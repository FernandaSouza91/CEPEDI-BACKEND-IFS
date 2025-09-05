#Taboada utilizando o for.
n1=int(input('Digite um numero '))
soma = 1
for i in range (1,11):
    soma = i*n1 
    print(f'{i} x {n1} = {soma}')

#somar os numero positivos ate chegar um negativo, mostrando a soma dos numeros digitados.
n1 = 0
lista = []
while n1 >=0:
    n1 = int(input('Digite um numero '))
    lista.append(n1)
print(f'Soma é {sum(lista)}')
#somando os numeros positivos até chegar um negativo utilizando o break
n1 = 0
soma = 0
while n1 >= 0:
    n1 = int(input('Digite um numero '))
    if n1 < 0: break
    soma = soma + n1
print(f'A soma dos numeros digitados foi {soma}')
# perguntar a idade e perguntar se a pessoa quer continuar e depois tirar a media das idades.
n1 = 0
n2 = 'S'
soma = 0
cont = 0
while n2 == 'S':
    n1=int(input('Qual a idade '))
    n2= str(input('Deseja continuar ? S/N')).upper()
    if n2 == 'N': break
    soma = soma+n1
    cont=cont+1
media= soma/cont
print(f'A media das idades é {media}')

#Verificando se um numero é par ou impar e digitando 0 para encerrar. 
num = int(input("Digite um número (0 para sair): "))
while num!=0:
    if num%2==0:
        print(f'Numero {num} é par.')
    else:
        print (f'Numero {num} é impar')
    num=int(input('digite um numero (Digite 0 para sair)'))
print("Programa encerrado.")
#Verificando se um numero é primo
n = int(input('Digite n: '))
cont = 0
i = 2
while i < n:
    r = n % i
    if r == 0:
        cont += 1
    i += 1
if cont == 0:
    print(f'{n} é primo')  
else: 
    print(f'{n} não é primo')      
    












 


    