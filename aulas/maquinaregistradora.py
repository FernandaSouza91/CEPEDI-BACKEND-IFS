produto = int(input('''
Digite o codigo do produto:
    Codigo de preços 
 1  R$ 0,50. 
 2  R$ 1,00
 3  R$ 4,00
 5  R$ 7,00
 9  R$ 8,00
 :  '''))
quant = int(input('Digite a quantidade desejada '))
soma=0
if produto == 1:
    soma=quant*0.50
    print(f'O total foi {soma}')
elif produto == 2:
    soma=quant*1
    print(f'O total foi {soma}')
elif produto == 3:
    soma=quant*4
    print(f'O tatal foi{soma}')
elif produto == 5:
    soma=quant*7
    print(f'o total foi {soma}')
elif produto == 9:
    soma=quant*8
    print(f'O total foi {soma}')
else:
    print('Código invalido')

    
