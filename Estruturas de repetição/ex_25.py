"""Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média de idade da
turma varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme a média
calculada.
"""
idades = []
while True:
    opcao = int(input('Digite a idade ou digite -1 para sair: '))
    if opcao != -1:
        idades.append(opcao)
    else:
        break

media = sum(idades) / len(idades)

if media > 60:
    print('idosa')
elif media >= 26:
    print('adulta')
elif media >= 0:
    print('jovem')
else:
    print('idades invalidas')
