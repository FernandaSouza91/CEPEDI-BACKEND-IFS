'''try:
    numero=int(input('Digite um numero inteiro: '))
    print('Número já foi digitado.')
except ValueError:
    print('Tipo do número não é inteiro.')
else:
    print('O numero digitado foi: ', numero)'''

'''
def dividir(a,b):
    return a/b

try:
    n1=int(input('Digite um numero inteiro: '))
    n2=int(input('Digite um numero inteiro: '))
    print('Resultado: ', dividir(n1,n2))
except ValueError as e:
    print('Tipo do número não é inteiro.Em inglês --->', e)
except ZeroDivisionError as zd:
    print('Divisão por zero não pode ser executada.Em ingles --->', zd)'''


'''try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a/b
except Exception as erro:
    print(f'Problema encontrado foi {erro.__class__}')
else:
    print(f'O resultado é {r:.1f}')
finally:
    print('Volte sempre!')'''
'''
try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a/b
except (ValueError, TypeError):
    print(f'Tivemos um probelma com os tipos de dados que voce digitou')
except ZeroDivisionError:
    print('Não é possivel dividir um numero por 0')
except Exception as erro:
    print(f'O erro encontrado foi {erro.__cause__}')
else:
    print(f'O resultado é {r:.1f}')
finally:
    print('Volte sempre!')'''


