import csv
with open("arquivo.txt", "w", encoding="utf-8") as arquivo: #aqui cria o arquivo e botei o nome de arquivo e o "w" é para escrever, o "utf-8" é para garantir que o arquivo seja salvo com a codificação correta
    arquivo.write("Olá, mundo!\n")
    arquivo.write("Este é um arquivo de exemplo.\n")
    arquivo.write("Manipulando arquivos em Python é fácil!\n")

    print("trabalho com arquivo csv")


dados_pessoas = [
    ["Nome", "Idade", "Cidade"],  
    ["Alice", 30, "São Paulo"],
    ["Bob", 25, "Rio de Janeiro"],
    ["Charlie", 35, "Belo Horizonte"]
]
with open ("dados_pessoas .csv", "w", encoding="utf-8", newline="") as arquivo_csv:
    escritor_csv = csv.writer(arquivo_csv)  
    escritor_csv.writerows(dados_pessoas)