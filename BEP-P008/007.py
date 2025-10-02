#Crie uma função processar_pedido que receba o nome de um cliente como primeiro argumento, seguido por uma lista variável de itens do pedido (*args), e por fim, detalhes adicionais como argumentos nomeados (**kwargs, ex:pagamento="cartão", entrega="urgente"). A função deve imprimir um resumo do pedido.


def processar_pedido(nome,*args,**kwargs):
    print()
    print(f'cliente:{nome}')
    print('Produtos:')
    for produto in args:
        print(f'{produto}')
    print('Detalhes adicionais:')
    for chave, valor in kwargs.items():
        print(f'{chave}:{valor}')




#pricipal
dic={}
produtos=[]
nome = str(input('Digite seu nome: '))

while True:
    args = str(input('Digite o produto:'))
    n1=str(input('Deseja continuar?(S/N)')).upper()
    produtos.append(args)
    if n1 =="N":
        break

dic['pagamento']=str(input('Forma de pagaemnto(Cartao/Pix/Dinheiro)'))
dic['entrega']=str(input('Entrega(Rapido/Urgente)'))
processar_pedido(nome,*produtos,**dic)
