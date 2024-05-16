
#EX 12 E 13
class CalculadoraDePesoIdeal: 
    def __init__(self, altura, genero):
        self.altura = altura
        self.genero = genero
    
    def calcular_peso(self):
        if self.genero == "F":
            peso_ideal = (62.1 * self.altura) - 44.7
        else:
            peso_ideal = (72.7 * self.altura) - 58 
        return peso_ideal
