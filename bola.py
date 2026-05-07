#Crie uma classe Bola com atributos cor, circunferencia e material. Adicione métodos para trocar a cor (trocaCor) e mostrar a cor (mostraCor). 
class Bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def trocaCor(self, nova_cor):
        self.cor = nova_cor

    def mostraCor(self):
        return self.cor
    

#Ex de uso:
bola = Bola("vermelha", 30, "borracha")
print(bola.mostraCor())