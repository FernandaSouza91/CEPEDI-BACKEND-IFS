#Uma escola ofereceu dois workshops: "Introdução à Robótica" e "Clube de Programação". Você tem a lista de presença de ambos. Sua tarefa é identificar quais alunos participaram dos dois eventos para que eles possam receber um certificado especial.
robotica = ['João', 'Maria', 'Pedro', 'Ana', 'Tiago']
programacao = ['Ana', 'Pedro', 'Sofia', 'João', 'Laura']


conjrobotica=set(robotica)
conjprogramação=set(programacao)
conjfinal=conjrobotica.intersection(conjprogramação)
print(conjrobotica)
print(conjprogramação)
print(conjfinal)

#Um GPS precisa armazenar uma lista de pontos (waypoints) de uma rota. Cada ponto é definido por um par de coordenadas: latitude e longitude. Esses pares de coordenadas, uma vez definidos para um ponto, não devem ser alterados. Sua tarefa é criar uma lista contendo três pontos de uma rota.
'''Dados de Entrada:
Ponto A: Latitude -23.5505, Longitude -46.6333 
Ponto B: Latitude -22.9068, Longitude -43.1729 
Ponto C: Latitude -19.9167, Longitude -43.9345'''

from collections import namedtuple
cordenadas = namedtuple('cordenadas',['latitude','Longitude'])
pontoa=cordenadas(-23.5505, -45.6333)
pontob=cordenadas(-22.9068, -43.1729)
pontoc=cordenadas(-19.9167,-439345)
print(pontoa)
rota=[pontoa,pontob,pontoc]
print(rota)

# praticando

