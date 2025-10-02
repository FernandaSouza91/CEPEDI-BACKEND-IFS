'''aluno = {}
aluno ['nome']= str(input('Nome: '))
aluno ['media'] = float(input(f'Media de {aluno["nome"]} é '))

if aluno['media'] >=7:
    aluno['situação']= 'Aprovado'
elif 5<= aluno ['media'] <7:
    aluno['situação']= 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'
for k, v in aluno.items():
    print(f' {k} é {v}')'''

'''from random import randint
from operator import itemgetter
jogos = dict()
jogo = {'jogador1': randint(1,6),
         'jogador2':randint(1,6), 
         'jogador3': randint(1,6),
         'jogador4': randint(1,6)
}
for k,v  in jogo.items():
    print(f'{k} e {v}')
jogos = sorted(jogo.items(), key = itemgetter(1), reverse=True)
for i, v in enumerate(jogos):
    print(f'{i+1}° lugar {v[0]} com {v[1]}')'''
'''pessoa = {}
pessoa ['nome'] = str(input('Nome :'))
pessoa ['ano'] = int(input('Ano de nascimento: '))
pessoa ['trabalho'] = int(input('CArteira de trabalho (0 não tem):'))
if pessoa['trabalho'] !=0:
        pessoa['anocontrato'] = int(input('O ano de contratação: '))
        pessoa['salario']= int(input('salario: '))

for c, v in pessoa.items():
        print(f'{c} é {v}')'''


    
