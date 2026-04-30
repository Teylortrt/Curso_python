#Escreva um programa que solicite números até que o usuário digite 0, usando while. 
# serve tambem para a atividade em que o numero 7 encerra o programa.
while True:
    try:
        numero = int(input("Digite um número ou 0 para fechar o programa: "))
        if numero == 0: # or numero == 7:
            print("Programa encerrado.")
            break
        else:
            print(f"Você digitou: {numero} q legal\u2714")
    except ValueError:
        print("Por favor, digite um número inteiro válido.")