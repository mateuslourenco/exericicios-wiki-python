"""
Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120.
A saída deve ser conforme o exemplo abaixo:
Fatorial de: 5
5! =  5 . 4 . 3 . 2 . 1 = 120
"""

numero = int(input('Informe um número inteiro: '))
print(f'{numero}! = ', end='')
fatorial = 1
for num in range(numero, 0, -1):
    fatorial *= num
    if num == numero:
        print(num, end='')
    else:
        print(f' . {num}', end='')

print(f' = {fatorial}')
