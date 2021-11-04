"""Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.
"""
numero = int(input('Informe um número ou -1 para sair: '))
menor = numero
maior = numero
soma = numero

while True:
    numero = int(input('Informe um número ou -1 para sair: '))
    if numero == -1:
        break
    elif numero not in range(1001):
        print('O número de estar entre 0 e 1000')
    else:
        if numero > maior:
            maior = numero
        elif numero < menor:
            menor = numero
        soma += numero

print(f'Menor: {menor}')
print(f'Maior: {maior}')
print(f'Soma: {soma}')

