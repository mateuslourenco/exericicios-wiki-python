"""Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa."""
lista = []

for _ in range(10):
    numero = float(input('Digite um numero: '))
    lista.append(numero)

# Para inverter a lista, também pode ser utilizado o método .reverse()
print(lista[::-1]) # Somente imprime a lista na ordem inversa.
