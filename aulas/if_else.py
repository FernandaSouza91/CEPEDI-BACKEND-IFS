# Aprender a função IF
numero = float(input('Digite um numero ?'))
if numero <15:
    print('Seu numero é menor que 15, parabens!')
else :
    print('Que pena tente novamente')

# verificando se um numero é par
numero = float(input('Digite um numero'))
if numero%2==0:
    print('Este numero é par')
else :
    print('Esse numero é impar')    

 #verificar se o triangulo é equilatero
l1= float(input('Digite o primeiro lado do triagulo'))
l2= float(input('Digite o segundo lado do triagulo'))
l3 = float(input('Digite o terceiro lado do triangulo'))

if l1 == l2 and l2 == l3:
    print('Este é um triangulo equilátero')
else :
    print('Este não é um triangulo equilátero')    

    #criar um codigo que pergunte a velocidade do carro, caso ultrapasse 80km exiba uma mensagem dizendo que o usuario foi multado, neste caso exiba o valor da multa, cobrando, R$ 15 por cada km acima da velocidade permitida.

v1 = float(input('Qual a velocidade do automovel ?'))
operacao=0
if v1 > 80: 
    print('Ultrapassou o limite de velocidade')
    operacao = (v1-80)*15
    print('O valor de sua multa foi', operacao)
else :
    print ('Dentro do limite de velocidade')

 # Faca um algoritmo que leia um determinado ano e mostre se ele é um ano bissexto. um ano é bissext se ele for divisivel por 400; ou se ele for divisivel por 4 e não por 100.
ano = int(input('Digite o ano' ))
if ano % 4 == 0 :
    print ('Este é um ano bissexto')
else :
    print ('Não é um ano bissexto')


#Verificar se o numero é maior ou menor que 10
numero = float(input('Digite um numero'))  
if numero > 10:
    print('Esse numero é maior que 10')
elif numero == 10:
    print('Este numero é igual a 10')
else :
    print('Este numero é menor que 10')
# Leia 2 valores e diga qual o maior

n1 = float(input('Digite um numero'))
n2 = float(input('Digite outro numero'))
if n1 > n2:
    print('O maior numero é',n1)
else:
    print('O maior numero é', n2)
# Ler 2 numeros , calcular a media e dizer se estar aprovado ou reprovado.
n1 = float(input('Informe uma a primeira nota'))
n2 = float(input('Informe a seguda nota'))
media = (n1+n2)/2
if media < 6:
    print('Aluno está reprovado')
else:
    print('Aluno aprovado')
# faca um algoritmo para calcular e mostrar o salario reajustado de um funcionario. O percentual de aumento encontra-se na tabela a seguir: salario até 300,00 percentual de aumento 35%, acima de 300,00 15%.
s1= float(input('Qual o valor do salário ?'))
if s1 > 300 :
    print('Seu novo salario será de ',(s1+((15/100)*s1)))
else :
    print('Seu novo salario será',(s1+((35/100)*s1)))
          
 # leia um numero fornecido pelo usuario . se esse numero for positivo, calcule a raiz quadrada do numero. se o numero for negativo , mostre uma mensagem dizend que o nuemro é invalido.th
 # 
#import math
from math import sqrt
n1 = float(input('Digite um numero'))  
if n1 > 0:
    print ('a raiz quadrada é',sqrt(n1))  

    
else:    
    print('Numero invalido')
# faca um programa que receba a altura e o sexo de uma pessoa e calcule mostre seu peso ideal, utilizando as seguintes formulas (onde h corresponde a altura) homens (72.7*h)-58, mulheres (62.1*h)-44.7
al= float(input('Qual a sua altura ?'))
sexo = str(input('Qual seu sexo?'))
if sexo == 'M':
    print("Seu peso ideal é",(72.7*al)-58 )
else:
    print('Seu peso ideal é',(62.1*al)-44.7)