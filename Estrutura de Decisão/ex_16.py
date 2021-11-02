"""Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá pedir
os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os
demais valores, sendo encerrado;
Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;
>>> calcular_equacao_segundo_grau(1, 2, 5)
A equação não possui raizes reais!

>>> calcular_equacao_segundo_grau(1, -10, 25)
Conjunto solução [ x = 5.0 ]

>>> calcular_equacao_segundo_grau(5, -3, -2)
Conjunto solução [ x' = 1.0, x'' = -0.4 ]

"""


def calcular_equacao_segundo_grau(a, b, c):
    delta = b**2 - 4 * a * c
    if delta < 0:
        print('A equação não possui raizes reais!')
    elif delta == 0:
        x = (-1 * b) / (2 * a)
        print(f"Conjunto solução [ x = {x} ]")
    else:
        x_uma_linha = ((-1 * b) + (delta ** 0.5)) / (2 * a)
        x_duas_linhas = ((-1 * b) - (delta ** 0.5)) / (2 * a)
        print(f"Conjunto solução [ x' = {x_uma_linha}, x'' = {x_duas_linhas} ]")


if __name__ == '__main__':
    calcular_equacao_segundo_grau(1, 2, 5)
    calcular_equacao_segundo_grau(1, -10, 25)
    calcular_equacao_segundo_grau(5, -3, -2)
