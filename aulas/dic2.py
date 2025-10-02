

dados={}
lista_nome = []
lista_idade = []


while True:
    dados['nome'] = str(input('Nome: '))
    dados['sexo'] = str(input('Sexo [M/F]: ')).upper()
    dados['idade'] = int(input('Idade: '))


    lista_nome.append(dados['nome']) 
    lista_idade.append(dados['idade'])

    while True:
        dados['n1'] = str(input('Deseja Continuar [S/N]')).upper()
        if dados['n1'] not in ['S','N']:
            print('Erro! responda apenas com S ou N')
        else:
            break
                  
    if dados['n1']== 'N':
            break
    
           
total = len(lista_nome)
soma = sum(lista_idade)
total_idade = len(lista_idade)
media = soma/total_idade

print(lista_nome) 
print(total)
print(media)

    
        






