#Escreva um programa para ler o salário mensal atual de um funcionário e o percentual de reajuste. Calcular e escrever o valor do novo salário com duas casas decimais.
salario = float(input('Digite seu salário atual R$ '))
reajuste = float(input('Digite o percentual do reajuste '))
porcentagem = reajuste/100
novo_salario = (salario+(salario*porcentagem))
print('O valor de seu salario atalizado é R$ {:.2f}'.format(novo_salario))
