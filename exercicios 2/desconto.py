#1. Um e-commerce permite que um cliente aplique múltiplos cupons em uma compra. O sistema deve calcular o valor final com base nos cupons válidos inseridos e no valor do frete de R$ 15. Crie um programa que leia o valor total da compra e dois cupons (como texto). O valor final deve ser atualizado sequencialmente. Cupons Válidos:●      ‘desconto10’: Aplica 10% de desconto sobre o valor.●      ‘fretegratis’: Subtrai R$ 15,00 do valor.

compra=float(input('Qual o valor total da compra R$ ? '))
print('Voce tem direito a 10% de desconto sobre o valor e frete gratis.')
desconto= compra -(compra*0.1)
frete= desconto-15
print(f'O valor total de sua compra ficou, R$ {frete:.2f}')