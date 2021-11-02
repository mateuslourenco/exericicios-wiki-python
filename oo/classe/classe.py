class CirculoPerfeito:
    def __init__(self):
        self.cor = 'Azul'
        self.circunferencia = 4
        self.material = 'Papel'

    def mostrar_cor(self):
        return self.cor

    def trocar_cor(self, cor):
        self.cor = cor


circulo_primeiro = CirculoPerfeito()
circulo_segundo = CirculoPerfeito()

print(type(circulo_primeiro))
print(circulo_primeiro is circulo_segundo)
print(id(circulo_primeiro))
print(circulo_primeiro.mostrar_cor())
circulo_segundo.cor = 'Amarelo'
print(circulo_primeiro.cor)
circulo_segundo.trocar_cor('Roxo')
print(circulo_segundo.mostrar_cor())
