#Desenvolva um programa que faça 5 perguntas para uma pessoa sobre um crime: "Telefonou para a vítima no último mês?" "Esteve no local do crime na última semana?" "Mora perto da vítima?" "Devia para a vítima?" "Já trabalhou com a vítima?" O programa deve classificar a pessoa como "Inocente",(1 resposta positiva) "Suspeita" (2 respostas positivas), "Cúmplice" (3 ou 4 respostas positivas) ou "Assassino" (5 respostas positivas).


soma = 0
n1=str(input('Telefonou para a vitima no último mês ?S/Sim ou N/Não ')).upper()
n2=str(input('Esteve no local do crime na ultima semana? S/sim ou N/Não')).upper()
n3=str(input('Mora perto da vitima? S/sim ou N/Não')).upper()
n4=str(input('Devia para a vitima? S/sim ou N/Não')).upper()
n5=str(input('Já trabalhou com a vitima S/sim ou N/Não')).upper()

soma = (n1 =='S')+(n2 =='S')+(n3 =='S')+(n4 =='S')+(n5 =='S')
if soma == 1:
    print('Inocente')
elif soma == 2:
    print('Supeita')
elif soma == 3 or soma == 4:
    print('Cúmplice')
elif soma == 5:
    print('Assassino')


