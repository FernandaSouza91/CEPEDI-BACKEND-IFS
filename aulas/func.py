
'''from datetime import date
def voto():
    nascimento=int(input('Digite o ano de nascimento')) 
    anoatual = date.today().year
    atual = (anoatual - nascimento)
    if atual >= 18 and atual <=70:
        print('Obrigatorio')
    if atual > 70:
        print('Opcional')
    else:
        print('Negado')


voto()'''

def ficha(nome='DEsconhecido',gol=0):
    nome = str(input('Digite o nome do jogador: '))
    gol = int(input("Digite a quantidade de gols: "))
    print(f'Nome: {nome}')
    print(f'Gol: {gol}')





ficha(nome='DEsconhecido',gol=0)