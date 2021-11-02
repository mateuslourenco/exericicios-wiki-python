def contas_caracteres(s):
    """Função que conta caracteres de uma string
    Ex:
    >>> contas_caracteres('mateus')
    {'a': 1, 'e': 1, 'm': 1, 's': 1, 't': 1, 'u': 1}

    >>> contas_caracteres('banana')
    {'a': 3, 'b': 1, 'n': 2}

    :param s: string a ser contada
    :return
    """
    resultado = {}

    s = sorted(s)

    for caracter in s:
        resultado[caracter] = resultado.get(caracter, 0) + 1
    return resultado


if __name__ == '__main__':
    print(contas_caracteres('mateus'))
    print()
    print(contas_caracteres('banana'))
