#Use um laço for para imprimir os números pares de 0 a 10. eu adiconei que o usuario possa digitar 
# um número e o programa irá dizer se ele é par ou não, e se for par ele será adicionado
# a uma lista de forma crescente usando a biblioteca bisect.

import bisect #biblioteca para inserir o numero de forma cresscente na lista
lista = []
while True: 
    while True:
        x = int(input("Digite um número de 0 a 10: "))
        if 0 <= x <= 10: 
            print(f"Você digitou: {x}")
            break
        else: 
            print("Número inválido. Por favor, tente novamente.")
    if x > 10:   
        print(f"{x} é maior que 10. Por favor, tente novamente.")
    elif x % 2 == 0:
        print(f"{x} é par.")
        bisect.insort(lista, x)  #esse bisect.insort insere o número na lista de forma crescente
        print(lista)

    else:
     print(f"{x} não é par.")
        
