#Contando de 0 a 4:
for contador in range(5):
    print(contador)

#Contando de 1 a 4:
for contador in range(1,5):
    print (contador)

#Contagem regressiva de 5 até 2:
for contador in range(5,1,-1):
    print(contador)

#Repetindo mensagem várias vezes
for i in range(10,1,-1):
    print('Tenho que estudar!')

#Números pares de 2 até 10
for contador in range (2,11,2):
    print(contador, 'é um número par.')

#Checando pares com if
for contador in range(2,11):
    if contador%2==0:
        print(contador,'é um número par.')

#Somatório de frações (usando 1/i)
soma=0
for i in range(1,7):
    termo=1/i
    soma=soma+termo
    print('termo', i, '=', termo)
print(f'Soma dos elementos:', soma)

#Mesma soma, mas exibindo de outra forma
soma=0
for i in range(1,7):
    termo=1/i
    soma=soma+termo
    print('termo', i, '=''1/i', termo)
print('Soma dos elementos:', soma)

#Contando pares e somando ímpares
cont_par=0
soma_impar=0
for i in range(1,121):
    if i%2==0:
        cont_par=cont_par+1
        print(cont_par) # não é necessario, serve apenas para visualizar o calculo
    else:
        soma_impar=soma_impar+i
        print(soma_impar)# não é necessario, serve apenas para visualizar o calculo
print('No intevalo[1,120]existem', cont_par,'números pares.')
print('No intervalo[1,120]somamos', soma_impar, 'em números impares.') 

#Imprimindo caracteres da string
s = 'programe em Python'
for x in s:
    print(x,end='-')

#ler 10 numeros e falar o maior e o menor
maior_numero = 0
for i in range (10):
    n1=float(input('Me diga um numero'))
    maior_numero = max(maior_numero,n1)
print('Este é seu numero maior',maior_numero)

#somatorio dos numeros
soma=0
for i in range (1,101):
    soma+=i
print('Somatorio do intervalo [1,100]=', soma)



    
