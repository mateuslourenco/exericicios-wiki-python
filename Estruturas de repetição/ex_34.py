"""Os números primos possuem várias aplicações dentro da Computação, por exemplo na Criptografia. Um número primo é
aquele que é divisível apenas por um e por ele mesmo. Faça um programa que peça um número inteiro e determine se ele é
ou não um número primo."""

numero = int(input('Numero inteiro: '))

divisores = 0

for div in range(1, numero + 1):
    if numero % div == 0:
        divisores += 1

if divisores == 2:
    print('primo')
else:
    print('nao primo')
