# jogo de batalha naval
import random
while True:
    print("Bem-vindo ao Batalha Naval!")
    print("1. Jogar")
    print("0. Sair")
    escolha = input("Digite sua escolha: ")
    
    if escolha == "1":
        print("----------bem vindo ao batalha naval----------")
        tabuleiro = [
            [0,0,0,0,0],
            [0,0,0,0,0], 
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
    ]
    else:
        print("Saindo do jogo. Até a próxima!")
        break
    
    tabuleiro_oculto = [linha[:] for linha in tabuleiro]
    
    tabuleiro_visivel = [
        ["~","~","~","~","~"],
        ["~","~","~","~","~"],
        ["~","~","~","~","~"],
        ["~","~","~","~","~"],
        ["~","~","~","~","~"],
    ]
    
    barcos = 6
    while barcos > 0:
        Lx, Ly = random.randint(0,4), random.randint(0,4)
        if tabuleiro_oculto[Lx][Ly] == 0:
            tabuleiro_oculto[Lx][Ly] = 1
            barcos -= 1
    
    barcos_restantes = 6
    tentativas = 0
    while True:
        for linha in tabuleiro_visivel:
            print(linha)
        try:
            x = int(input("coordenada X (0-4): ")) #linha
            y = int(input("coordenada Y (0-4): ")) #coluna
        except ValueError:
            print("Por favor, digite um número inteiro válido.")
            continue
        tentativas += 1
        if tabuleiro_visivel[x][y] != "~":
            print("Você já tentou aqui!")
            continue
            
        if tabuleiro_oculto[x][y] == 1:
            print("Acertou!")
            tabuleiro_visivel[x][y] = "X"
            barcos_restantes -= 1
            if barcos_restantes == 0:
                print(f"Parabéns! Você venceu em {tentativas} tentativas.")
                break
        else:
            print("Errou!")
            tabuleiro_visivel[x][y] = "O"
    print("Obrigado por jogar!")

