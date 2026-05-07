class Produtos:
    def __init__(self, nome: str, preco: float):
        self.nome = nome
        self.preco = preco

    def aplicar_desconto(self, percentual: float):
        self.preco -= self.preco * (percentual / 100)
    
    