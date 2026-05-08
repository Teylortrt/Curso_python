import tkinter as tk
import teste1

def login():
    usuario = entrarusuario.get()
    senha = entraresenha.get()

    if usuario == "admin" and senha == "1234":
        label = tk.Label(janela, text=f"bem vindo, {usuario}!")
        label.pack(pady=10)
        #janela.destroy()
        teste1.sistemabanco()
    else:
        label = tk.Label(janela, text="Usuário ou senha incorretos. Tente novamente.")
        label.pack(pady=10)

janela = tk.Tk()
janela.geometry("300x200")
janela.title("Login")

label = tk.Label(janela, text="Usuário:")
label.pack(pady=10)

entrarusuario = tk.Entry(janela)
entrarusuario.pack()