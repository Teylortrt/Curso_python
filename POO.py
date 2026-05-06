# um objeto é algo que que estao com o mesmo grupo de caracteristicas, 
# mas cada um tem suas proprias caracteristicas, por exemplo, um cachorro é um objeto, ele tem caracteristicas 
# como cor, raça, idade, mas cada cachorro tem suas proprias caracteristicas, 
# ex, um cachorro pode ser preto, outro pode ser branco, outro pode ser marrom, etc.

"""cachorro1 = {
    "nome": "Rex",
    "cor": "preto",
    "raça": "Labrador",
    "idade": 3
}
print("o nome do meu cachorro é " + cachorro1["nome"])
print("a cor do meu cachorro é " + cachorro1["cor"])
print("a raça do meu cachorro é " + cachorro1["raça"])
print("a idade do meu cachorro é " + str(cachorro1["idade"]))"""
# as classes são como moldes para criar objetos, elas definem as caracteristicas e comportamentos que os objetos terão,
# por exemplo, podemos criar uma classe Cachorro, que tem as caracteristicas nome, cor, raça e idade, e os comportamentos latir e comer.
class cachorro:
    def __init__(self, nome, cor, raça, idade):
        self.nome = nome
        self.cor = cor
        self.raça = raça
        self.idade = idade
    
    #definir o comportamento latir
    def latir(self):
        if self.idade < 4:
            return "Au au!"
        else:
            return "AUU AUU!"

cachorro1 = cachorro("Rex", "preto", "Labrador", 3)
cachorro2 = cachorro("Bella", "branco", "Poodle", 5)

print(cachorro1.latir())
print(cachorro2.latir())