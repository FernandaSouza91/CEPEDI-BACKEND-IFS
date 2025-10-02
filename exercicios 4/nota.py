#Faça um programa para corrigir provas de múltipla escolha. Cada  prova contém 10 questões. A primeira lista a ser carregada é o gabarito da prova. Os outros dados são os números de matrícula dos alunos e as respostas que   deram às questões. Considere que temos 10 alunos. Calcule e mostre o número da matrícula e a nota de cada aluno. Mostre também a porcentagem de aprovação.
Gabarito = []
for p in range(1,11):
    q=str(input(f'Digite o {p}° Gabarito ')).upper()
    Gabarito.append(q)
print(Gabarito)
matri=[]
for m in range(1,11):
    matricula=int(input(f'Digite o numero de matricula do {m}° aluno '))    
    matri.append(matricula)
Resposta = []
for i in range(1,11):
    Resposta_alunos=[]
    print(f'\nAluno {i}° com numero de matricula N°{matri[i-1]} ')
    for j in range(1,11):
        r=str(input(f'Digite a resposta da questão {j}° ')).upper()
        Resposta_alunos.append(r)
    Resposta.append(Resposta_alunos)

notas=[]
for i in range(10):
    nota = 0
    for j in range(10):
        if Resposta[i][j]== Gabarito[j]:
            nota+=1
    notas.append(nota)
    print(f'\no ALUNO com a matricula N° {matri[i]}, tirou nota {notas[i]}.')
print(f'Matriculas {matri}')
print(f'Gabaritos {Gabarito}')
aprovados=0
for n in notas:
    if n >=7:
        aprovados +=1
        percentual = (aprovados/len(notas))*100
print(f"Porcentagem de aprovação: {percentual:.2f}%")