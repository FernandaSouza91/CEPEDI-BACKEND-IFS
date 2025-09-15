#Ler uma sequência de números reais e armazená-los. A sequência termina quando for digitado o número (0) zero. Determinar o maior elemento dessa sequência e imprimir a lista resultante.
lista_reais = []
maior = 0
while True:
    reais = float(input('Digite um número real '))
    lista_reais.append(reais)
    maior = max(lista_reais)
    if reais == 0:
        break
print(f'A sua lista de numeros reais é {lista_reais} e seu maior elemento é {maior}')