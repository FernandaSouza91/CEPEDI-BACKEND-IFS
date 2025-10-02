# Crie uma função chamada analisar_notas que receba uma lista de notas. A
# função deve retornar três valores: a maior nota, a menor nota e a média das
# notas

def analisar_notas(*lista_notas):
    maior_nota = max(lista_notas)
    menor_nota = min(lista_notas)
    cont = len(lista_notas)
    soma= sum(lista_notas)
    media = soma/cont
    return f'Sua maior nota foi : {maior_nota}\nSua menor nota foi : {menor_nota}\nSua media foi :{media}'
    


lista_notas=[1,2,3,7,8]
print(analisar_notas(*lista_notas))