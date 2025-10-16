'''Crie um programa que faça a leitura de uma lista de inteiros que só
poderá ter 10 posições. Feito isso, permita que o usuário digite valores
inteiros a fim de preencher este vetor. Não implemente nenhum tipo
controle referente ao tamanho do vetor (uso do for, por exemplo),
deixe que o usuário digite valores até que a entrada 0 (zero) seja
digitada. Uma vez digitado o valor zero, o mesmo deve ser inserido na
lista e a digitação de novos elementos deve ser interrompida. Feita toda
a coleta dos dados, exiba-os em tela.
Seu programa deve tratar as seguintes exceções:
● Quando o usuário informar mais de 10 valores (RuntimeError) deve
ser lançada uma exceção com a mensagem “Tamanho do vetor previsto
foi excedido.”
● Quando o usuário informar um valor que não é inteiro (ValueError)
deve ser lançada uma exceção com a mensagem “Tipo inválido.”'''



lista = []

try:
    
    while True:
        n1=int(input(f'Digite um numero: '))
        lista.append(n1)
        if n1 == 0:
            break
        if len(lista) > 10:
            raise RuntimeError('Tamanho do vetor previsto foi excedido')
        

except ValueError:
    print('Tipo inválido')
except RuntimeError as erro:
    print(erro)
else:
    print("\nLista final:")
    print(lista)

