valor = float(input('Digite o deposito inicial '))
juros = float(input('Digite os juros da poupança'))
porc = juros/100
for i in range (1,25):
    rendimento = (valor*porc)
    valor = valor + rendimento
    print(f'O rendimento mensal é {i} x {valor:.2f}')
print (f'O total de ganhos é {valor:.2f}' )