"""Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada de dados
quando for informado um valor igual a -1 (que não deve ser armazenado). Após esta entrada de dados, faça:
Mostre a quantidade de valores que foram lidos;
Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
Calcule e mostre a soma dos valores;
Calcule e mostre a média dos valores;
Calcule e mostre a quantidade de valores acima da média calculada;
Calcule e mostre a quantidade de valores abaixo de sete;
Encerre o programa com uma mensagem;"""

notas = []

numero = float(input("Informe a nota ou -1 para sair: "))

while numero != -1:
    notas.append(numero)
    numero = float(input("Informe a nota ou -1 para sair: "))

# Mostre a quantidade de valores que foram lidos;
qtd_valores_lidos = len(notas)
print(f'Quanditade de valores lidos: {qtd_valores_lidos}')

# Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
print(' '.join([str(nota) for nota in notas]))

# Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
notas.reverse()
for nota in notas:
    print(nota)

# Calcule e mostre a soma dos valores;
soma = sum(notas)
print(f'Soma: {soma}')

# Calcule e mostre a média dos valores;
media = soma / qtd_valores_lidos
print(f'Media: {media}')

# Calcule e mostre a quantidade de valores acima da média calculada;
qtd_acima_da_media = 0
print('Notas acima da media:')
print(' '.join([str(nota) for nota in notas if nota > media]))

# Calcule e mostre a quantidade de valores abaixo de sete;
print('Notas abaixo de 7: ')
print(' '.join([str(nota) for nota in notas if nota < 7]))

print('Programa encerrado')
