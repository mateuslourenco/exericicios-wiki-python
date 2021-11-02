"""Classe Bomba de Combustível: Faça um programa completo utilizando classes e métodos que:

Possua uma classe chamada bombaCombustível, com no mínimo esses atributos:
tipoCombustivel.
valorLitro
quantidadeCombustivel
Possua no mínimo esses métodos:
abastecerPorValor( ) – método onde é informado o valor a ser abastecido e mostra a quantidade de litros que foi colocada
 no veículo
abastecerPorLitro( ) – método onde é informado a quantidade em litros de combustível e mostra o valor a ser pago pelo
cliente.
alterarValor( ) – altera o valor do litro do combustível.
alterarCombustivel( ) – altera o tipo do combustível.
alterarQuantidadeCombustivel( ) – altera a quantidade de combustível restante na bomba.
OBS: Sempre que acontecer um abastecimento é necessário atualizar a quantidade de combustível total na bomba."""


class BombaCombustivel:
    def __init__(self, combustivel: str, valor_litro: float, quantidade_combustivel: float):
        self.tipo_combustivel = combustivel
        self.valor_litro = valor_litro
        self.quantidade_combustivel = quantidade_combustivel

    def abastecer_por_valor(self, valor: float):
        litros_abastecidos = valor / self.valor_litro
        self.apresentar_abastecimento_se_possivel(litros_abastecidos, valor)

    def apresentar_abastecimento_se_possivel(self, litros_abastecidos: float, valor: float):
        if litros_abastecidos > self.quantidade_combustivel:
            print(
                f'Não é possível abastecer {litros_abastecidos} litro(s),' 
                f'faltam {litros_abastecidos - self.quantidade_combustivel:.2f} litro(s)'
            )
        else:
            self.quantidade_combustivel -= litros_abastecidos
            print(f'Foram abastecidos {litros_abastecidos:.2f} litro(s) a um valor de R$ {valor:.2f}')
            print(f'Total de combustível restante: {self.quantidade_combustivel}')

    def abastecer_por_litro(self, litros_abastecidos):
        valor = self.valor_litro * litros_abastecidos
        self.apresentar_abastecimento_se_possivel(litros_abastecidos, valor)

    def alterar_valor(self, valor):
        self.valor_litro = valor

    def alterar_combustivel(self, combustivel):
        self.tipo_combustivel = combustivel

    def alterar_quantidade_combustivel(self, quantidade):
        if quantidade < self.quantidade_combustivel:
            print('NOPE')
        else:
            self.quantidade_combustivel = quantidade


bomba = BombaCombustivel(combustivel='Gasolina', valor_litro=3, quantidade_combustivel=1000)

bomba.abastecer_por_valor(3)
bomba.abastecer_por_litro(1)
bomba.abastecer_por_litro(1001)
