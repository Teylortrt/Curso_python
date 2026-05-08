#Crie uma classe Quadrado com atributo tamanho_lado.Inclua métodos para mudar o valor do lado, retornar o valor do lado e calcular a área. 
class Quadrado:
    def __init__(self, tamanho_lado):
        self.tamanho_lado = tamanho_lado

    def mudar_valor_lado(self, novo_tamanho):
        self.tamanho_lado = novo_tamanho

    def retornar_valor_lado(self):
        return self.tamanho_lado

    def calcular_area(self):
        return self.tamanho_lado ** 2
    
#Ex de uso:
quadrado = Quadrado(4)
print("Valor do lado:", quadrado.retornar_valor_lado())
print("Área do quadrado:", quadrado.calcular_area())