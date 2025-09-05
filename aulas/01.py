num = int(input("Digite um número (0 para sair): "))
while num!=0:
    if num%2==0:
        print(f'Numero {num} é par.')
    else:
        print (f'Numero {num} é impar')
    num=int(input('digite um numero (Digite 0 para sair)'))
print("Programa encerrado.")