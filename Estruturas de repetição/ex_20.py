"""Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e limitando o
fatorial a números inteiros positivos e menores que 16.
"""

while True:
    numero = int(input('Informe o número ou -1 para sair: '))
    if numero == -1:
        break
    elif numero > 16:
        print('O número deve ser menor que 16')
    else:
        fatorial = numero
        while numero > 1:
            fatorial *= numero - 1
            numero -= 1
        print(fatorial)
