"""Classe Quadrado: Crie uma classe que modele um quadrado:

Atributos: Tamanho do lado
Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;"""


class Quadrado:
    def __init__(self, valor_lado = 1):
        self.valor_lado = valor_lado

    def mudar_valor_lado(self, novo_valor):
        self.valor_lado = novo_valor

    def mostrar_valor_lado(self):
        return self.valor_lado

    def calcular_area(self):
        return self.valor_lado ** 2


novo_quadrado = Quadrado(4)
print(novo_quadrado.mostrar_valor_lado())
novo_quadrado.mudar_valor_lado(6)
print(novo_quadrado.mostrar_valor_lado())
print(novo_quadrado.calcular_area())
