#Escreva um programa para ler o número total de eleitores de um município, o número de votos brancos, nulos e válidos. Calcular e escrever o percentual que cada um representa em relação ao total de eleitores.

numero_total_de_eleitores = int(input('Digite o numero total de eleitores'))
v_branco = int(input('Digite o total de votos em branco'))
v_nulos = int(input('Digite o total de votos nulos'))
v_validos = int(input('Digite o numero de votos validos'))
percentual_b = (v_branco/numero_total_de_eleitores)*100
percentual_n = (v_nulos/numero_total_de_eleitores)*100
percentual_v = (v_validos/numero_total_de_eleitores)*100
print (f'O total de eleitores foi {numero_total_de_eleitores}, sendo {v_branco} brancos,{v_nulos} nulos, {v_validos} validos, com um percentual em relação aos eleitores de {percentual_b:.2f}% brancos, {percentual_n:.2f}% nulo e {percentual_v:.2f}% validos.')