"""Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide
a entrada e permita repetir a operação.
"""

while True:
    try:
        populacao_pais_a = int(input('Informe a população do pais A: '))
        populacao_pais_b = int(input('Informe a população do pais B: '))
        taxa_crescimento_a = float(input('Informe a taxa de crescimento do pais A: '))
        taxa_crescimento_b = float(input('Informe a taxa de crescimento do pais B: '))
    except ValueError:
        print('Valores informados inválidos!')
    else:
        if populacao_pais_a >= populacao_pais_b:
            print('A população do pais A já é maior ou igual que a população do pais B!')
        elif taxa_crescimento_a < taxa_crescimento_b:
            print(
                'A taxa de crescimento da população B é maior que a taxa da população A, sendo assim, a população A '
                'nunca irá alcançar ou superar a população B'
            )
        else:
            taxa_crescimento_a = 1 + (taxa_crescimento_a / 100)
            taxa_crescimento_b = 1 + (taxa_crescimento_b / 100)
            anos_necessarios = 0
            while populacao_pais_a < populacao_pais_b:
                anos_necessarios += 1
                populacao_pais_a *= taxa_crescimento_a
                populacao_pais_b *= taxa_crescimento_b
            print(f'Anos necessários: {anos_necessarios}')
            break
