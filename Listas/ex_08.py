"""
Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. Imprima a
idade e a altura na ordem inversa a ordem lida.
"""

idade = []
altura = []

for _ in range(5):
    idade.append(int(input('Idade: ')))
    altura.append(float(input('Altura: ')))

# Pode ser usado o meteodo .reverse() para atribuir valor
print(idade[::-1])  # Somente mostra invertido, não altera a lista
print(altura[::-1])

