#Faça um programa que receba o nome de cinco produtos e seus respectivos preços, armazene-os em listas, calcule e mostre: a) a quantidade de produtos com preço inferior a R$ 50,00; b) o nome dos produtos com preço entre R$ 50,00 e R$ 100,00; c) a média dos preços dos produtos com preço superior a R$ 100;
nome_list= []
preco_list=[]
quan_inf=[]
nome_entre = []
preco_sup_100 = []
media = 0
soma = 0
quant = 0
for i in range(5):
    print(f'------PRODUTO {i+1}-------')
    nome = str(input('Digite o nome do produto: '))
    preco = float(input('Digite o preço deste produto R$ '))
    nome_list.append(nome)
    preco_list.append(preco)
for n, p in enumerate(preco_list):
    if p < 50:
        quan_inf.append(p)
print(f' Teve {len(quan_inf)} produto(s) com preço inferior a R$ 50,00.')

for nome , preco in zip(nome_list, preco_list):
    if preco >= 50 and preco <= 100:
        nome_entre.append(nome)
print(f' O nome do produto com preço entre R$ 50,00 e R$ 100,00 é {nome_entre}')

for preco in preco_list:
    if preco > 100:
        preco_sup_100.append(preco)
        soma = sum(preco_sup_100)
        quant = len(preco_sup_100)
    media = soma / quant
print(f' A madia de preço dos produtos acima de R$ 100,00 foi {media}')

