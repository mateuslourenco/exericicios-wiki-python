def contas_caracteres(s):
    """Função que conta caracteres de uma string
    Ex:
    >>> contas_caracteres('mateus')
    a: 1
    e: 1
    m: 1
    s: 1
    t: 1
    u: 1
    >>> contas_caracteres('banana')
    a: 3
    b: 1
    n: 2

    :param s: string a ser contada
    """
    caracteres_ordenados = sorted(s)

    caracter_anterior = caracteres_ordenados[0]
    contagem = 1

    for caracter in caracteres_ordenados[1:]:
        if caracter == caracter_anterior:
            contagem += 1
        else:
            print(f'{caracter_anterior}: {contagem}')
            caracter_anterior = caracter
            contagem = 1
    print(f'{caracter_anterior}: {contagem}')


if __name__ == '__main__':
    contas_caracteres('mateus')
    print()
    contas_caracteres('banana')
