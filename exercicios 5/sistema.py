#2. Você precisa criar um sistema simples para armazenar informações sobre produtos de uma loja. Cada produto tem um código único (ID) e um nome. Seu programa deve armazenar três produtos e, em seguida, permitir que o usuário digite um ID para buscar e imprimir o nome do produto correspondente.
'''Dados de Entrada:
● Produto 1: ID 101, Nome Camiseta
● Produto 2: ID 102, Nome Calça Jeans
● Produto 3: ID 103, Nome Tênis'''


armazenar = {}

for i in range (3):
    nome=str(input('Digite o nome do produto: '))
    id=int(input('Digite a ID do produto: '))
    armazenar[id]=nome
print(f' Os produtos armazenados foram {armazenar}')

N1=int(input('Digite o Id que quer verificar'))
if N1 in armazenar:
    print(f'O Id {N1} corresponde a {armazenar[N1]}')


