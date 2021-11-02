"""Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano
 é ou não bissexto."""


def ano_bissexto(ano):
    if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
        return True
    else:
        return False


if __name__ == '__main__':
    print(ano_bissexto(1996))
