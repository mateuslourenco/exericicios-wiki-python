"""A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até
o n−ésimo termo.
"""

termo_n = int(input('Informe o enésimo termo: '))
n1 = 0
n2 = 1

for i in range(termo_n):
    fib = n1 + n2
    if i == 0:
        print(fib)
    else:
        print(fib)
        n1 = n2
        n2 = fib
