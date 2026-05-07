class Produto:
    
    def __init__(self, nome: str, preco: float):
        self.nome = nome
        self.preco = preco

    def __str__(self) -> str:
        return f"Produto: {self.nome} | R${self.preco:.2f}"

    def aplicar_desconto(self, percentual: float):
        self.preco -= self.preco * (percentual / 100)
