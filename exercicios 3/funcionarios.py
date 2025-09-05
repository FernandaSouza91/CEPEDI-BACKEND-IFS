#6. Desenvolva um programa em Python para registrar informações sobre funcionários em uma empresa. Comece solicitando o número de funcionários. Para cada funcionário, o programa deve requisitar o nome, salário e departamento (“Vendas”, “RH” ou “Gerência”). Ao final, apresente as seguintes estatísticas:●       O nome do funcionário com o salário mais alto.●       A média dos salários dos funcionários.●       A quantidade de funcionários que trabalham no departamento de Vendas.
numero = int(input('Digite a quantidade de funcionarios da empresa: '))
media = 0
salario_maior = None
nome_domaior = ""
somadosalarios = 0
cont = 0
for i in range (numero):
    print(f"----{i}° Funcionario ----")
    nome = str (input('Digite o nome do funcinario: '))
    salario = float (input('Digite o salário:  '))
    departamento = str (input('Digite o departamento (“Vendas”, “RH” ou “Gerência”)')).capitalize()
    somadosalarios += salario
    if salario_maior is None or salario > salario_maior:
        salario_maior = salario
        nome_domaior = nome
    if departamento == 'Vendas':
        cont += 1
print(f'A quantidade de funcionários que trabalham no departamento de Vendas : {cont}.')
        
print(f'A media do salario dos funcionarios é R$ {somadosalarios/ numero:.2f}')

print(f'O funcionario com o maior salário é {nome_domaior} e seu salário é R${salario_maior:.2f}')