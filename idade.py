1. #Crie um programa que peça a idade do usuário e diga se ele é maior ou menor de idade. 
idade = int(input("Digite sua idade: "))
tempo = 2026 - idade
if idade >= 18:
    print(f"Você é maior de idade.tendo {idade} anos, você nasceu em {tempo}.")
else:
    print(f"Você é menor de idade. tendo  {idade} anos, você nasceu em {tempo}.")
