#Calcular juros simples
capital = float (input('Qual o valor do captal?'))
taxadejuros = float (input('Qual o valor da taxa de juros (10,20,30...%)?'))
tempo = float (input('Qual o tempo da aplicação em meses ?'))

juros = (capital*taxadejuros*tempo)/100

print ( "o valor do seu juros simples é de ", juros)