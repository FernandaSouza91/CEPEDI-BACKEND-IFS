'''(Adaptado de Rossi) Crie um novo script que solicite um número
inteiro e indique se ele é um número perfeito. Um número perfeito é
um número inteiro para o qual a soma de todos os seus divisores
positivos menores que ele é igual ao próprio número. Ex: 6 = 1+2+3.
O número informado deve ser maior que zero e deve ser menor ou
igual a 32767.
Se o dado informado não for um número ou se o número for maior que
32767, o programa deve informar a mensagem: “Erro: dado inválido”.
Se o número não for maior que zero, o programa deve imprimir a
mensagem: “Erro: o número deve ser maior que zero.”. Conjunto teste
na imagem abaixo.'''

try:
    
    entrada=(input('Digite um numero: '))

    if not entrada.isdigit():
        raise TypeError('Erro: dado inválido.')
    
    numero = int(entrada)
    

    if numero <= 0:
        raise ValueError('Erro: O numero deve ser maior que zero.')
    if numero > 32767:
        raise RuntimeError('Erro: Dado invalido') 
    
    
    divisores=[]
    for n in range (1,numero ):     
        if numero % n == 0:
            divisores.append(n)


    soma= sum(divisores)

    if soma == numero:
        print(f'O numero {numero} é perfeito')
    else:
        print(f'O numero {numero} não é perfeito')

       
except (ValueError, RuntimeError, TypeError) as v:
    print(v)
except :
    print('Erro: dado inválido.')



