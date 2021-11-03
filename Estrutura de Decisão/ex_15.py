"""Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um
triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
Dicas:
Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
Triângulo Equilátero: três lados iguais;
Triângulo Isósceles: quaisquer dois lados iguais;
Triângulo Escaleno: três lados diferentes;"""

lado_a = float(input('Informe o primeiro lado do triangulo: '))
lado_b = float(input('Informe o segundo lado do triangulo: '))
lado_c = float(input('Informe o terceiro lado do triangulo: '))

if lado_a + lado_b > lado_c or lado_a + lado_c > lado_b or lado_b + lado_c > lado_a:
    if lado_a == lado_b and lado_b == lado_c:
        tipo = 'Equilátero'
    elif lado_a != lado_b and lado_a != lado_c and lado_b != lado_c:
        tipo = 'Escaleno'
    else:
        tipo = 'Isósceles'

    print(f'Triangulo {tipo}')

else:
    print('não é triangulo')
