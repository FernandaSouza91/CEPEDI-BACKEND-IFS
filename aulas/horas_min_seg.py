#ler quantidade de segundos e tranformar em hora min e segundo
segundos = float (input("Qual o valor dos segundos? "))

horas = (segundos//3600)
minutos = int(((segundos%3600)/60))
segundosfinais = (segundos%60)

print (" Horas :", horas, "Minutos:", minutos, "Segundos:", segundosfinais)