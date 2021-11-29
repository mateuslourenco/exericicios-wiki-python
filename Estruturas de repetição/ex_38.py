"""
Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:
Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior. Faça um
programa que determine o salário atual desse funcionário. Após concluir isto, altere o programa permitindo que o usuário
digite o salário inicial do funcionário.
"""

salario = 1000
ano = 1995
ano_atual = 2022
aumento = 1.5 / 100
while ano < ano_atual:
    ano += 1
    salario *= 1 + aumento
    aumento *= 2

print(salario)
