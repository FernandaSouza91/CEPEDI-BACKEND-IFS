'''(Adaptado de Rossi) Crie um programa que solicite o nome e o salário
do usuário e calcule o valor que a empresa deve depositar em sua conta
do FGTS.
Se o nome informado não for válido, o programa deve imprimir uma
mensagem de erro e solicitá-lo novamente. Conjunto teste na imagem
abaixo.
a) o nome deve conter de 5 a 50 caracteres.
b) o nome não pode conter números.
Se o salário informado não for válido, o aplicativo deve imprimir uma
mensagem de erro e solicitá-lo novamente.
a) o salário deve ser um número
b) o salário deve ser igual ou superior a R$ 1100,00.
Ao final o programa deve imprimir os dados que serão registrados no
recibo de pagamento do usuário: nome, salário e o valor do FGTS (8%
do salário).'''


def fgts (salario):
        valor_fgts= salario*0.08
        return valor_fgts                       



while True:
    try:
        nome = str(input('Digite seu nome: ')).upper()
        if len(nome) < 5 or len(nome)> 50:
            raise TypeError('Número de caracteres invalido')
        if any(char.isdigit() for char in nome):
            raise ValueError('Erro: o nome não pode conter números.')
        break
    except TypeError as t:
         print(t)
    except ValueError as v:
         print(v)
         


while True:
    try:
        salario = float(input('Digite seu salario:R$ ').replace(',','.'))
        if salario < 1100:
                raise TypeError('Erro: Sálario abaixo do mínimo')
                
        break
    except TypeError as t:
        print(t)
    except ValueError:
        print('Erro: Informe um número válido (ex: 2000,00)')
    



print(f'''
      Recibo de Pagamento
Nome:         {nome}
Sálario:      R${salario:.2f}
FGTS:         R${fgts(salario):.2f}
  
  ''')

    
    

