"""Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';"""

print('''####
Sexo: 'f' ou 'm'
Estado Civil: 's', 'c', 'v', 'd'
####
''')
nome = str(input('Nome: '))
idade = int(input('Idade: '))
salario = float(input('Salário: '))
sexo = str(input('sexo: '))
estado_civil = str(input('Estado Civil: '))

sexos = ['f', 'm']
estados_civis = ['s', 'c', 'v', 'd']


while (len(nome) < 3) or (idade not in range(0, 151)) or (salario <= 0) or (sexo not in sexos) or (estado_civil not in estados_civis):
    print('Informções inválidas')
    nome = str(input('Nome: '))
    idade = str(input('Idade: '))
    salario = str(input('Salário: '))
    sexo = str(input('sexo: '))
    estado_civil = str(input('Estado Civil: '))
