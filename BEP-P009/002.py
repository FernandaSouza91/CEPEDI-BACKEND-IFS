'''2. Crie uma função que valide se uma string corresponde ao formato de placa de
carro brasileira antiga (3 letras, 4 números) ou nova (3 letras, 1 número, 1 letra,
2 números). A função deve retornar True se a placa for válida e False caso
contrário.
Exemplos de Teste:
● "ABC1234" -> True (formato antigo)
● "XYZ9A87" -> True (formato novo)
● "ABC123" -> False
● "1234ABC" -> False
● "ABCD1234" -> False'''


import re

def validar_placa(placa):
    padrao = re.compile(r'^[A-Z]{3}[0-9]{4}$|^[A-Z]{3}[0-9][A-Z][0-9]{2}$')
    return bool(padrao.match(placa))

# Testes
placas = ["ABC1234", "XYZ9A87", "ABC123", "1234ABC", "ABCD1234"]

for p in placas:
    print(f"{p} -> {validar_placa(p)}")
