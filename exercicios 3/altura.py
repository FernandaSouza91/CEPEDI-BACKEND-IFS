#5. Escrever um programa que leia um conjunto de 50 informações contendo, cada uma delas, a altura e o sexo de uma pessoa (1 - masculino 2-feminino), calcule e mostre o seguinte: a) a maior e a menor altura da turma b) a média da altura das mulheres c) a média da altura da turma.

maioraltura = None
menoraltura = None
soma_mulher = 0
quant_mulheres = 0
soma_turma = 0
for i in range (50):
    print(f'---{i}° PESSOA ----')
    altura = float(input('Digite a sua altura: '))
    sexo = int(input('Digite o seu sexo 1 - masculino e 2- feminino'))       
    if maioraltura is None or altura > maioraltura:
        maioraltura = altura
    if menoraltura is None or altura < menoraltura:
        menoraltura = altura
    if sexo == 2:
        soma_mulher = soma_mulher + altura
        quant_mulheres = quant_mulheres + 1
    soma_altura = soma_mulher + altura
    if quant_mulheres > 0:
        media_mulheres = soma_mulher/quant_mulheres
    else:
        0
    soma_turma = soma_turma + altura
media_turma = soma_turma / 50
print(f' A maior altura da turma é {maioraltura:.2f}m')
print(f' A menor altura da turma é {menoraltura:.2f}m')
print(f'A media da altura das mulheres é {media_mulheres:.2f}m')
print(f'A media da altura da turma é {media_turma:.2f}m')
