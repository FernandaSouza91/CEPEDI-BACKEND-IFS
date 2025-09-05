#calculadora
for i in range (10):
    n1=float(input('Digite um numero'))
    n2=float(input('Digite um segundo numero'))
    n3 = str(input('Escolha uma operação (+,-,*,/)'))
    operacao = 0
    if n3 == '+' :
        operacao = n1 + n2
    elif n3 == '-' :
        operacao = n1 - n2
    elif n3 == '*' :
        operacao = n1 * n2
    elif n3 == '/' :
        operacao = n1 / n2
    else:
        print('Operação invalida')
    print('Sua resposta foi : ', operacao)
# energia eletrica, calculo de valor a pagar pelos KWH consumidos. 
n1= float(input('Informe qual o KWH consumido'))
n2 = str(input('Informe o tipo de instalação(R- para residencia, I- para industria e C- para comercios)')).upper()

operacao = 0

if n2 == 'R' :
    if n1 >500 :
        operacao = n1* 0.65
        print(f'O preço apagar é R$ {operacao}') # para colocar dentro do parenteses 
    else:
        operacao = n1 * 0.40
        print('O preço apagar é R$ ',operacao)

if n2 == 'C' :
    if n1 > 1000 :
        operacao = n1 *0.60
        print(f'O preço apagar é R$ {operacao:.2f}')# para colocar 2 casas decimais :.2f
    else:
        operacao = n1 * 0.55
        print('O preço apagar é R$ ',operacao)

if n2 == 'I':
    if n1 > 5000 :
        operacao = n1 * 0.60
        print('O preço apagar é R$ ',operacao)
    else:
        operacao = n1 * 0.55
        print('O preço apagar é R$ ',operacao)




    
