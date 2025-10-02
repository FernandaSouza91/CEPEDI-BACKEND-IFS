#Você recebeu uma frase e sua tarefa é contar a frequência de cada palavra. Para simplificar, desconsidere maiúsculas/minúsculas (ou seja, "Python" e "python" devem ser contadas como a mesma palavra). O resultado final deve mostrar cada palavra única e o número de vezes que ela apareceulista = []
cont= 0
n1=str(input('Digite uma frase: ')).lower()
print(n1)
palavra = n1.split()

contadorPalavras = {}
print(palavra)
for pal in palavra:
    contadorPalavras[pal] = 0
    print(contadorPalavras[pal])

for pal in palavra:
    contadorPalavras[pal] +=1
    print(f'{contadorPalavras[pal]}')
        

print(contadorPalavras)
print( )

#Pode ser feito desta forma tambem.

'''from collections import Counter


n1=str(input('Digite uma frase: ')).lower()
print(n1)
palavra = n1.split()
contagem = Counter(palavra)
print(contagem)'''
