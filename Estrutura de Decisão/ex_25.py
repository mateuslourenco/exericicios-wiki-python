"""Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice"
e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente"."""

print('--- RESPONDA COM SIM OU NAO ---')
telefonema = str(input('Telefonou para a vítima? ')).upper()
esteve_no_local = str(input('Esteve no local do crime? ')).upper()
mora_perto = str(input('Mora perto da vítima? ')).upper()
devia = str(input('Devia para a vítima? ')).upper()
trabalhou_junto = str(input('Já trabalhou com a vítima? ')).upper()

nivel_de_suspeito = 0

if telefonema == 'SIM':
    nivel_de_suspeito += 1
if esteve_no_local == 'SIM':
    nivel_de_suspeito += 1
if mora_perto == 'SIM':
    nivel_de_suspeito += 1
if devia == 'SIM':
    nivel_de_suspeito += 1
if trabalhou_junto == 'SIM':
    nivel_de_suspeito += 1

if nivel_de_suspeito == 5:
    classificado = 'Assassino'
elif nivel_de_suspeito >= 3:
    classificado = 'Cúmplice'
elif nivel_de_suspeito == 2:
    classificado = 'Suspeita'
else:
    classificado = 'Inocente'

print(classificado)
