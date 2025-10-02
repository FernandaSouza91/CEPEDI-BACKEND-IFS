#Crie uma função criar_perfil_usuario que aceite dois argumentos obrigatórios (nome e email) e uma quantidade variável de informações adicionais usando argumentos nomeados (**kwargs). A função deve montar e retornar um dicionário contendo todas as informações do perfil do usuário

def criar_perfil_usuario (nome,email,**kwargs):
    perfil ={
        'nome':nome,
        'email':email

    }
    perfil.update(kwargs)
    return perfil







#programa principal 
dic={}
nome=str(input('Digite seu nome:(Obrigatório) '))
email=str(input('Digite seu email:(Obrigatório) '))
dic['telefone']=int(input('Digite seu telefone: '))
dic['sexo']=str(input('Digite se sexo(M/F)'))
dic['CPF']=int(input('Digite seu CPF:'))

resultado=criar_perfil_usuario(nome,email,**dic)
print('~'*30)
print(f'Perfil do Usuário')
for chave, valor in resultado.items():
    print(f'{chave}:{valor}')

