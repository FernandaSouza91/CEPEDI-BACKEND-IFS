#5. Escrever um programa que leia um conjunto de 50 informações contendo, cada uma delas, a altura e o sexo biológico de uma pessoa (1 - masculino 2-feminino), calcule e mostre o seguinte: a) a maior e a menor altura da turma b) a média da altura das mulheres c) a média da altura da turma.
maioraltura = None
menoraltura = None
cont = 0
soma = 0
m =0
mediageral = 0
media = 0
for i in range (3):
    print(f'---{i}° PESSOA ----')
    altura = float(input('Digite a sua altura: '))
    sexo = int(input('Digite o seu sexo 1 - masculino e 2- feminino'))
    m+=altura
    cont+=1
    mediageral=m/cont
    print(f'A{media}')
    if maioraltura is None or altura > maioraltura:
        maioraltura = altura
    if menoraltura is None or altura < menoraltura:
        menoraltura = altura
    if sexo == 2:
        cont+=1
        soma +=altura
        media = soma/cont
print(media)
print(f' A maior altura da turma é {maioraltura}')
print(f' A menor altura da turma é {menoraltura}')
