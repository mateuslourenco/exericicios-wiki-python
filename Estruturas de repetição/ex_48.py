"""
Faça um programa que peça um numero inteiro positivo e em seguida mostre este numero invertido.
Exemplo:
  12376489
  => 98467321
"""

try:
    numero = int(input('Informe um número inteiro positivo: '))
except ValueError:
    print('Não foi informado um número inteiro positivo')
else:
    if numero < 0:
        print('Não foi informado um número inteiro positivo')
    else:
        num_str = str(numero)
        num_invertido = ''
        for i in range(len(num_str), 0, -1):
            num_invertido += num_str[i - 1]
        print(num_invertido)
