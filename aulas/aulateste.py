#  Cadastro de Notas de Alunos Crie um programa em Python que: Peça ao usuário para digitar o nome de 5 alunos e a respectiva nota de cada um. Armazene os nomes em uma lista chamada alunos e as notas em outra lista chamada notas.Após o cadastro, o programa deve:Exibir a lista completa de alunos com suas notas.Mostrar a maior nota e o nome do aluno que a tirou.Mostrar a menor nota e o nome do aluno que a tirou.Calcular e exibir a média da turma.Exibir a lista de alunos que ficaram acima da média.
alunos =[]
notas = []
dicionario_aluno = {}
maior_aluno = 0


for i in range(5):
    aluno = str(input(f'Digite o nome do(a) {i+1}° Aluno(a) '))
    nota = float(input(f'Digite a nota de {aluno} '))
    alunos.append(aluno)
    notas.append(nota)


for aluno, nota in zip (alunos, notas):
    print(f"O aluno(a) {aluno} tirou a nota {nota}")
    

index_maior = notas.index(max(notas))
maior_aluno = alunos[index_maior]
maior_nota = notas[index_maior]
print(f'O(A) aluno(a) {maior_aluno} tirou a maior nota {maior_nota}')
index_menor = notas.index(min(notas))
menor_aluno = alunos[index_menor]
menor_nota = notas[index_menor]
print(f'O(A) aluno(a) {menor_aluno} tirou a menor nota {menor_nota}')
quant = len(notas)
soma = sum(notas)
media = soma/quant
print(f'A media de notas da turma foi {media}')
print('Os alunos acima da media 7 foram :')

for aluno, nota in zip(alunos, notas):
    if nota >=7:
        print(f'{aluno} tirou {nota}')