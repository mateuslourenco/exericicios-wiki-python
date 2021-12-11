def encontrar_maior_numero_digitos_consecutivos(numero):
    """
    Função que recebe um número qualquer e encontra o maior número formado por dígitos consecutivos.
    Ex:
    >>> encontrar_maior_numero_digitos_consecutivos(53590)
    90
    >>> encontrar_maior_numero_digitos_consecutivos(674030098567819)
    5678
    >>> encontrar_maior_numero_digitos_consecutivos(9012364509789)
    90123
    >>> encontrar_maior_numero_digitos_consecutivos(123789)
    789

    :param numero:
    """
    prox_numero_dict = {
        '0': '1', '1': '2', '2': '3', '3': '4', '4': '5', '5': '6', '6': '7', '7': '8', '8': '9', '9': '0'
    }
    numero_str = str(numero)
    maiores_numeros = []
    numero_localizado = ''
    for i, num in enumerate(numero_str):
        try:
            if numero_str[i + 1] == prox_numero_dict[num]:
                numero_localizado += num
            else:
                numero_localizado += num
                maiores_numeros.append(int(numero_localizado))
                numero_localizado = ''
        except IndexError:
            if numero_str[i] == prox_numero_dict[num]:
                numero_localizado += num
                maiores_numeros.append(int(numero_localizado))
                maiores_numeros.append(int(numero_localizado))

    maior_numero_localizado = max(maiores_numeros)
    print(maior_numero_localizado)


if __name__ == '__main__':
    encontrar_maior_numero_digitos_consecutivos(123789)
