# Simule um caixa eletrônico. Peça ao usuário o valor do saque (inteiro). O programa deve informar o número de notas de R$ 100, R$ 50, R$ 20, R$ 10 necessárias para compor o valor. Suponha que o caixa sempre tem notas disponíveis e que o valor do saque é múltiplo de 10.

valor = int(input('Digite o valor da nota  sendo múltipla de 10: R$ '))
notade100 = valor // 100
valor%= 100
notasde50 = valor // 50
valor%= 50
notasde20 = valor // 20
valor%= 20
notasde10 = valor // 10
print('Notas necessarias:')
if notade100 > 0:
    print(f'{notade100} nota(s) necessarias')
if notasde50 > 0:
    print(f'{notasde50} nota(s) necessarias ')
if notasde20 > 0:
    print(f'{notasde20} nota(s) necessarias')
if notasde10 > 0:
    print(f'{notasde10} nota(s) necessarias')