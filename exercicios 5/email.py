#Você recebeu uma lista de e-mails de participantes de um evento, mas a lista contém vários e-mails duplicados. Sua tarefa é criar uma nova coleção que contenha apenas os e-mails únicos e, em seguida, imprimir a quantidade de participantes únicos.
# Dados de Entrada:'''emails_participantes = [ 'ana@email.com', 'bruno@email.com', 'carla@email.com', daniel@email.com', 'ana@email.com', 'bruno@email.com', 'emilia@email.com' ]'''



emails_participantes = [ 'ana@email.com', 'bruno@email.com', 'carla@email.com', 'daniel@email.com', 'ana@email.com', 'bruno@email.com', 'emilia@email.com' ]

lista =[]
for email in emails_participantes:
   if email not in lista:
     lista.append(email)
   
print(lista)

#Pode ser feito desta forma tambem:

emails_participantes = [ 'ana@email.com', 'bruno@email.com', 'carla@email.com', 'daniel@email.com', 'ana@email.com', 'bruno@email.com', 'emilia@email.com' ]

email= set(emails_participantes)
print(email)

