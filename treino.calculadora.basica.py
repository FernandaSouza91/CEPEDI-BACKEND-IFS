#Criando uma calculadora basica
codigo1 = float (input("Digite um numero: "))
codigo2 = input ("Digite a operação(+, -, /, *): ")
codigo3 = float (input("Digite um segundo numero: "))
soma = codigo1+codigo3
diminuicao = codigo1-codigo3
divisao = codigo1/codigo3
mutiplicacao = codigo1*codigo3
if codigo2 =='+':
   operacao = soma
elif codigo2 =='-':
   operacao = diminuicao
elif codigo2 =='*':
   operacao = mutiplicacao
elif codigo2 =='/':
   operacao = divisao
else :
   operacao = "operação invalida"
print("o resultado foi", operacao)