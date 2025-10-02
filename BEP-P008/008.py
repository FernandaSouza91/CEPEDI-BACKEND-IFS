#Você tem uma lista de produtos, onde cada produto é um dicionário. Crie uma função filtrar_produtos que recebe a lista de produtos e um preco_maximo. A função deve retornar uma nova lista contendo apenas os produtos cujo preço é menor ou igual ao preco_maximo.


Produtos={'Maca': 3.50,'Pera': 2.50,'Goiaba':2.00,'Uva':4.00 }

def filtra_produtos(preco_maximo,**produtos):
    lista=[]
    for chave, valor in produtos.items():
        if valor <= preco_maximo:
            lista.append((chave,valor))
       
    return lista



#programa principal


produtos={'Maca': 3.50,'Pera': 2.50,'Goiaba':2.00,'Uva':4.00 }
preco_maximo=float(input('Digite o preco maximo do item : '))
resultado = filtra_produtos(preco_maximo,**produtos)

print('Produtos filtrados:')
for nome, preco in resultado:
    print(f'{nome}:{preco}')

