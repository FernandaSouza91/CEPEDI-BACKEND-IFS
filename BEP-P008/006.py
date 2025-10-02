#Crie uma função chamada gerar_relatorio que receba um número variável de argumentos nomeados (keyword arguments) e imprima um relatório formatado com cada par chave-valor. Ex: gerar_relatorio(nome="João Silva", idade=30, cidade="São Paulo", profissao="Engenheiro") e retornaria: Nome: João Silva Idade: 30 Cidade: São Paulo Profissao: Engenheiro


def gerar_relatorio(**keyword_arguments):
    print()
    print('~'*20)
    for chave,valor in keyword_arguments.items():
        print(f'{chave}: {valor}')
  
    return 



dados = {}
dados['nome']=str(input('Nome: '))
dados['idade']=int(input('Idade: '))
dados['cidade']=str(input('Cidade: '))
dados['profissao']=str(input('profissao: '))

gerar_relatorio(**dados)