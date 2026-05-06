

def calcular_media_turma(notas):

    if len (notas) == 0:
        return 0.0
    soma = sum(notas)
    quantidade = len(notas)

    media = soma / quantidade
    return media

notas_alunos = [7.5,8.0,6.5,9.0]
media_final = calcular_media_turma(notas_alunos)

print(media_final)
