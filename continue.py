#Reescreva uma das atividades anteriores utilizando continue.
while True:
    try:
        numero = int(input("Digite um número ou 0 para fechar o programa: "))
        if numero == 0: # or numero == 7:
            print("Programa encerrado.")
            continue
        else:
            print(f"Você digitou: {numero} q legal\u2714")
    except ValueError:
        print("Por favor, digite um número inteiro válido.")