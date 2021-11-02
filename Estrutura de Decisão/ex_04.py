"""Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
"""

vogais = ['A', 'E', 'I', 'O', 'U']

letra = str(input('Informe um letra: ')).upper()

if letra in vogais:
    print('Vogal')
else:
    print('Consoante')
