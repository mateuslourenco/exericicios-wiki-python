"""Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.
"""
from ex_17 import ano_bissexto


def validar_data(data):
    dia, mes, ano = (data.split(sep='/'))
    dia = int(dia)
    mes = int(mes)
    ano = int(ano)
    meses_com_trinta = (4, 6, 9, 11)
    data_valida = True

    if (dia <= 0 or dia > 31) or (mes <= 0 or mes > 12):
        data_valida = False
    elif mes == 2:
        bissexto = ano_bissexto(ano)
        if not bissexto and dia > 28:
            data_valida = False
        elif dia > 29:
            data_valida = False
    elif mes in meses_com_trinta:
        if dia > 30:
            data_valida = False

    if data_valida:
        print(f'A data {data} é valida!')
    else:
        print('Data invalida!')


if __name__ == '__main__':
    validar_data('28/02/1995')
