#Crie uma variável que vai armazenar a palavra secreta “Programação”. Em seguida, utilize uma estrutura de repetição que deve parar de solicitar uma palavra apenas quando o usuário acertar a palavra secreta.

while True:
    nome = str(input('Digite um nome: '))
    if nome == 'programacao':
        break
print('Você digitou a palavra secreta, o programa finalizou.')