while True:
    try:
        populacao_a = int(input('População A: '))
        populacao_b = int(input('População B: '))
        taxa_crescimento_a = float(input('Taxa A: '))
        taxa_crescimento_b = float(input('Taxa B: '))
    except (ValueError, TypeError):
        print('Valores inválidos!')
    else:
        break

# codigo continua parando aqui

anos = 0
while populacao_a < populacao_b:
    anos += 1
    populacao_a = int(populacao_a * ((taxa_crescimento_a/100) + 1))
    populacao_b = int(populacao_b * ((taxa_crescimento_b/100) + 1))
    print(f' ### População no ano:{anos} ####')
    print(f' Pupulação A:{populacao_a}')
    print(f' Pupulação B:{populacao_b}')
