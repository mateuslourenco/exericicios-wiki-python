"""
Nome na vertical em escada invertida. Altere o programa anterior de modo que a escada seja invertida.
"""

nome = 'FULANO'

for indice in range(len(nome), 0, -1):
    print(nome[:indice])
