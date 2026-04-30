cachorro = input("qual o nome do seu cachorro? ")
nome = input("e qual o seu nome? ")
while True:
    try:
        anos = int(input("quantos anos tem seu cachorro? "))
        break
    except ValueError:
        print("Por favor, digite um número inteiro válido.")
print(f"Olá {anos}, o seu cachorro {nome} tem {cachorro} anos!"'\N{SNAKE}')
