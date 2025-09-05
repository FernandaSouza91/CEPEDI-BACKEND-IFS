#Elabore um programa que defina uma senha (por exemplo, "1234"). O programa deve pedir ao usuário que digite a senha e, em seguida, informar se o "Acesso foi permitido" ou "negado".
senha=int(input('Crie uma senha de 4 digitos: '))
print('Senha gravada.')
verificacao=int(input('Digite a sua senha: '))
if verificacao == senha:
    print('Acesso foi permitido')
else:
    print('Acesso negado')