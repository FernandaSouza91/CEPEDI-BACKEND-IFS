'''from datetime import datetime
dados = {}
dados['nome']= str(input('nome: '))
dados['ano de nascimento']= int(input('Ano de nascimento: '))
dados['carteira de trabalho']= int(input('Nº da Carteira de trabalho: '))
idade = datetime.now().year-dados['ano de nascimento']

if dados['carteira de trabalho'] !=0:
    dados['ano de contratacao']= int(input('Ano de contratação: '))
    dados['salario']= float(input('Valor do sálario: '))
    

for c,v in dados.items():
    print(f'{c} é {v}')'''

'''dados ={}
gols=[]
dados['nome']=str(input('Nome do jogador: '))
dados['partidas']=int(input(f'Quantas partidas {dados["nome"]} jogou? '))
for i in range(dados['partidas']):
    gol=int(input(f'Quantos gols na partida {i+1}º ?'))
    gols.append(gol)
    soma = sum(gols)
dados['gols']= gols
dados['total']= soma
print('~'*30)
print(dados)
print('~'*30)

for c,v in dados.items():
    print(f'O campo {c} tem valor {v}')
print('~'*30)

print(f'O jogador {dados["nome"]} jogou {dados["partidas"]} partidas')
for i in range(dados['partidas']):
    print(f'-> Na partida {i+1}, fez {gols[i]}')
print(f'Foi um total de {dados["total"]} gols')'''





