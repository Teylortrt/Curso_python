# jogo de batalha naval

while True:
    print("Bem-vindo ao Batalha Naval!")
    print("1. Jogar")
    print("2. Sair")
    escolha = input("Digite sua escolha: ")
    
    if escolha == "1":
        tabuleiro = [
            [0,0,0,0,0],
            [0,0,0,0,0], 
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
    ]
    for linha in tabuleiro:
        print(linha)
    colocar_barco = input("Digite as coordenadas para colocar o barco (linha,coluna): ")
    
        print("Obrigado por jogar!")
        