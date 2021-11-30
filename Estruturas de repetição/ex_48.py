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
        num_invertido = ''.join(reversed(num_str))
        print(num_invertido)
