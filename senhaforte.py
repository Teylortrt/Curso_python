'''Crie uma função que recebe uma senha e verifica se ela é válida:
Regras:
Pelo menos 8 caracteres
Pelo menos 1 número
Pelo menos 1 letra maiúscula
Pelo menos 1 caractere especial
Retorne:
"Senha válida" ou "Senha inválida"
mostrar quais critérios não foram atendidos'''
import re

print("Bem-vindo ao verificador de senhas!")
print("Sua senha deve atender aos seguintes critérios:")
print("- Pelo menos 8 caracteres,\n - Pelo menos 1 número, \n - Pelo menos 1 letra maiúscula, \n - Pelo menos 1 caractere especial")

senha = input("Digite sua senha: ")

def verificar_senha(senha):
    faltando = []

    if len(senha) < 8:
        faltando.append("Pelo menos 8 caracteres")
    if not re.search(r"\d", senha):
        faltando.append("Pelo menos 1 número")
    if not re.search(r"[A-Z]", senha):
        faltando.append("Pelo menos 1 letra maiúscula")
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>_-]", senha):
        faltando.append("Pelo menos 1 caractere especial")

    if faltando:
        return False, faltando
    return True, []

valida, faltantes = verificar_senha(senha)

if valida:
    print("Senha válida")
    print("Senha forte!")
else:
    print("Senha inválida")
    print("Sua senha não atende aos seguintes critérios:")
    for criterio in faltantes:
        print(f"- {criterio}")
    print("Senha fraca. Por favor, siga as diretrizes de segurança: use caracteres especiais, números e letras maiúsculas.")