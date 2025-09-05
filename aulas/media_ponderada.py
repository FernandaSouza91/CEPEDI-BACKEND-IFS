nome = input("Digite seu nome: ")
n1 = float(input("Primeira nota: "))
n2 = float( input("Segunda nota: "))
media = (n1 + n2 )/2
print(media)
p1 = 2
p2 = 4
peso = ((n1*p1)+(n2*p2))/(p1+p2)
print(peso)
print("Seu nome é",nome,"Sua nota foi," ,n1,"e" , n2, "Sua media ponderada é",peso)