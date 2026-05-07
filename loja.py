from produto import Produto

print("---- Sistema de venda da loja -----")

# criando objeto usando a classe que veio de outro script
item1 = Produto("Notebook", 3500)
item2 = Produto("Celular", 1200)
item3 = Produto("Mouse", 45)

item1.aplicar_desconto(10)

print(item1)
print(item2)
print(item3)