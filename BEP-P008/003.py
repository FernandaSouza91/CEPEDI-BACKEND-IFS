# Escreva uma função chamada saudar que receba um nome e uma saudacao
# opcional. Se a saudação não for fornecida, ela deve usar "Olá" como padrão. A
# função deve retornar uma string formatada.

def saudar(nome, saudacao):
    if saudacao == "":
        saudacao = 'Olá'
    return f"{saudacao},{nome} Que bom que está aqui!"

    



nome=str(input('Digite seu nome: '))
saudacao=str(input('Digite uma saudação(opcional)'))
print(saudar(nome, saudacao))

