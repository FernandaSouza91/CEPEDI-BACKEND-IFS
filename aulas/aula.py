def filtrar_produtos(preco_maximo, **produtos):
    produtos_validados = []

    for produto, preco in produtos.items():
         
         if preco <= preco_maximo:
              produtos_validados.append(produto)

    return f"Produtos cujo preço é menor ou igual ao preço máximo (R$ {preco_maximo:.2f}): {", ".join(produtos_validados)}"


produtos = {
    "Laranja": 18.90,
    "Uva": 10.10,
    "Banana": 7.00
}


print(filtrar_produtos(10.20, **produtos)) #