#Crie uma calculadora de Índice de Massa Corporal (IMC) que, além de calcular o valor (peso / altura²), classifique o resultado de acordo com as seguintes faixas:●      Abaixo de 18.5: Abaixo do peso, ●      18.5 a 24.9: Peso ideal, ●      25.0 a 29.9: Levemente acima do peso,●      30.0 a 34.9: Obesidade grau I, ●      35.0 a 39.9: Obesidade grau II (severa),●      Acima de 40.0: Obesidade grau III (mórbida)

peso=float(input('Digite o seu peso '))
altura=float(input('Digite sua altura '))
IMC = peso/(altura*altura)
if IMC <18.5:
    print('Abaixo do peso')
elif IMC >= 18.9 and IMC <= 24.9:
    print('Peso ideal')
elif IMC >= 25 and IMC <= 29.9:
    print('Levemente acima do peso')
elif IMC >=30 and IMC <= 34.9:
    print('Obesidade Grau I')
elif IMC >= 35 and IMC <= 39.9:
    print('Obesidade grau II(severa)')
elif IMC >= 40:
    print('Obesidade grau III(mórbida)')