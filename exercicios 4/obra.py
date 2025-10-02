# Durante o planejamento de uma obra, um engenheiro registrou a quantidade de sacos de cimento utilizados em cada um dos 7 dias da semana. Escreva um programa em Python que leia a quantidade de sacos para cada dia e exiba o total de sacos de cimento usados na semana. Crie uma nova lista apenas com os dias em que o consumo foi acima de 29 sacos(utilize list comprehension) e exiba essa lista.
semana= []
lista_maior = []
for i in range(1,8):
    Dia = int(input(f'Digite a quantidade de sacos de cimento da {i}º Dia '))
    semana.append(Dia)
soma = sum(semana)
'''for dia, saco in enumerate(semana):
    if saco > 29:
        lista_maior.append((saco,dia+1))
        print(f"O dia {dia+1}º teve {saco}sacos de cimento.")'''
lista_maior = [(dia+1, saco) for dia, saco in enumerate(semana)if saco >29]
for dia, saco in lista_maior:
    print(f"O dia {dia} teve {saco} sacos")
print(f'O total de sacos de cimento utilizados na semana foi de {soma}')

