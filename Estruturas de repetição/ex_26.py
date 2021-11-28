"""Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para cada eleitor
votar e ao final mostrar o número de votos de cada candidato.
"""

numero_de_eleitores = int(input('Informe o número de eleitores: '))
votos = {'1': 0, '2': 0, '3': 0}

for eleitor in range(numero_de_eleitores):
    print(f'{ "*" * 10} Candidatos {"*" * 10}')
    print('Digite 1 para votar no candidato 1')
    print('Digite 2 para votar no candidato 2')
    print('Digite 3 para votar no candidato 3')
    voto = input('Votar: ')
    votos[voto] += 1

for candidato, total_votos in votos.items():
    print(f'Total de {total_votos} para candidato {candidato}')
