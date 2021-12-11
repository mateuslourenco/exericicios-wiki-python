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
    :return: 
    """
    prox_numero_dict = {
        '0': '1', '1': '2', '2': '3', '3': '4', '4': '5', '5': '6', '6': '7', '7': '8', '8': '9', '9': '0'
    }
    numero_str = str(numero)
    maior_numero = ''
    prox_digito = numero_str[1]
    total_numeros_localizados = []
    for digito in numero_str:
        if prox_digito == prox_numero_dict[digito]:
            maior_numero += digito
            prox_digito = str(int(prox_digito) + 1)
        else:
            total_numeros_localizados.append(int(maior_numero))
            prox_digito = str(int(digito) + 1)
            maior_numero = digito

    maior_numero_localizado = max(total_numeros_localizados)
    print(maior_numero_localizado)


if __name__ == '__main__':
    encontrar_maior_numero_digitos_consecutivos(1237890)
