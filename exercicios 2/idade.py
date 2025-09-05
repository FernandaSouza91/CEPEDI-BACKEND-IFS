 #Peça a idade de um usuário e, com base nela, classifique-o em uma das seguintes categorias: "Criança" (0-12 anos), "Adolescente" (13-17 anos) ou "Adulto" (18 anos ou mais).
idade= int(input('Digite a sua idade '))
if idade <= 12 :
    print('Criança')
elif idade <= 17 :
    print('Adolecente')
else:
    print('Adulto')