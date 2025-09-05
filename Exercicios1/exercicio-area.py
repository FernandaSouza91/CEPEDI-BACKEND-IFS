#Faça um programa que leia a largura e altura de uma parede, calcule e mostre a área a ser pintada e a quantidade de tinta necessária para o serviço, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

largura = float(input('Digite a largura: '))
altura = float(input('Digite a altura '))
area = altura*largura
tinta = area/2
print(f'A largura de sua parede é {largura} a sua altura {altura} e sua área {area} portanto são necessarios {tinta} litros de tinta.')