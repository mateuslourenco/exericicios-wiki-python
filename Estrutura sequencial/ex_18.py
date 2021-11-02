"""Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet
(em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos)."""

tamanho_em_magabytes = float(input('Informe o tamanho do arquivo em MB: '))
velocidade = float(input('Informe a velocidade em Mbps: '))

tamanho_em_megabits = tamanho_em_magabytes * 8

tempo_aproximado_em_segundos = tamanho_em_megabits / velocidade
tempo_aproximado_em_minutos = tempo_aproximado_em_segundos / 60

print(f'{tempo_aproximado_em_minutos:.2f}')
