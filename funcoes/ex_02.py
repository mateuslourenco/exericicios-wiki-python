"""Faça um programa para imprimir:
    1
    1   2
    1   2   3
    .....
    1   2   3   ...  n
"""


def imprimir_triangulo_de_numeros(n: int):
    for linha in range(1, n + 1):
        for coluna in range(1, linha + 1):
            print(coluna, end='   ')
        print('')


imprimir_triangulo_de_numeros(2)
imprimir_triangulo_de_numeros(3)
imprimir_triangulo_de_numeros(10)
