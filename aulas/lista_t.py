#Crie um programa que:Peça ao usuário para digitar o nome e a idade de 5 pessoas.Armazene os nomes em uma lista e as idades em outra.Mostre todos os nomes com suas respectivas idades.Encontre e mostre:A pessoa mais velha A pessoa mais jovem
lista_nome=[]
lista_idade=[]
for i in range(5):
    nome=str(input(f'Digite o {i+1}° Nome: '))
    Idade = int(input(f'Digite a idade de {nome}: '))
    lista_nome.append(nome)
    lista_idade.append(Idade)
for nome, idade in zip (lista_nome, lista_idade):
    print(f"{nome} tem {idade} ano(s). ")
index_maior = lista_idade.index(max(lista_idade))
maior_idade = lista_idade[index_maior]
nome_maior = lista_nome[index_maior]
print(f'A pessoa mais velha é {nome_maior} com {maior_idade} ano(s).')
index_menor = lista_idade.index(min(lista_idade))
menor_nome = lista_nome[index_menor]
menor_idade = lista_idade[index_menor]
print(f'A pessoa mais nova é {menor_nome} com {menor_idade} ano(s).')