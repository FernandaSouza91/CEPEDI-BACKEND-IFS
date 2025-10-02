#Faça um programa que leia quanto dinheiro uma pessoa tem na carteira (em R$) e mostre quantos dólares ela pode comprar. Considere US$1,00 = R$5,50. 
dinheiro = float(input('Informe o valor em R$ '))
calculo = (dinheiro/5.50)
print(f'Com esse valor você pode comprar Us${calculo:.2f}.')
