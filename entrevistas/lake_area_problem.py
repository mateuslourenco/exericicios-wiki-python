"""Você receberá uma matriz (uma lista de listas) de, possivelmente, altura e largura diferentes contendo apenas 0s e 1s
Cada 0 representa terra e cada 1 representa água. Uma lagoa é composta por qualquer número de 1s verticalmente ou
horizontalmente adjacentes (mas não diagonalmente adjacentes). O número de 1s adjacentes determina a área da lagoa.

Escreva uma função que retorna uma lista com as áreas das lagoas contidas na matriz em ordem crescente.
Um exemplo é:
Dada a matriz
matrix = [
    [1, 1, 0, 1, 0],
    [1, 0, 1, 0, 0],
    [0, 0, 1, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 1, 0]
]
A resposta esperada é uma lista com os tamanhos dos rios
sizes = [1, 2, 2, 3, 5]


>>> lake_areas(matrix=[[1, 1, 0, 1, 0],[1, 0, 1, 0, 0],[0, 0, 1, 0, 1],[1, 0, 1, 0, 1],[1, 0, 1, 1, 0]])
sizes = [1, 2, 2, 3, 5]
"""
from typing import List


def lake_areas(matrix: List[List[int]]) -> List[int]:
    for i, linha in enumerate(matrix):
        for elem in linha:
            print(f'{i}. {elem}')


matrix = [
    [1, 1, 0, 1, 0],
    [1, 0, 1, 0, 0],
    [0, 0, 1, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 1, 0]
]

lake_areas(matrix)
