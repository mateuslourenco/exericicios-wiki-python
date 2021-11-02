"""Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue
pedindo até que o usuário informe um valor válido."""

while True:
    try:
        numero = int(input("Informe uma nota de 0 a 10: "))
    except ValueError:
        print('Deve ser fornecido um valor inteiro')
    else:
        if 0 <= numero <= 10:
            print(f'Nota informada é {numero}')
            break
        else:
            print(f'A nota deve estar entre 0 e 10')
