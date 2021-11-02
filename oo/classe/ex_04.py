"""Classe Pessoa: Crie uma classe que modele uma pessoa:

Atributos: nome, idade, peso e altura
Métodos: Envelhercer, engordar, emagrecer, crescer. Obs: Por padrão, a cada ano que nossa pessoa envelhece, sendo a
idade dela menor que 21 anos, ela deve crescer 0,5 cm."""


class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.altura = altura
        self.peso = peso
        self.idade = idade
        self.nome = nome

    def envelhecer(self):
        if self.idade < 21:
            self.altura += 0.5
        self.idade += 1

    def engordar(self, kilos):
        self.peso += kilos

    def emagrecer(self, kilos):
        self.peso -= kilos

    def crescer(self, cm):
        self.altura += cm


mateus = Pessoa(nome='Mateus', idade=25, peso=100, altura=181)

print(mateus.nome)
print(mateus.idade)
print(mateus.peso)
mateus.engordar(1)
print(mateus.peso)
mateus.envelhecer()
print(mateus.idade)
