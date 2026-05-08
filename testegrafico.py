import tkinter as tk

janela = tk.Tk()
janela.title("Esfera 3D")
janela.geometry("500x400")

canvas = tk.Canvas(janela, width=500, height=400, bg="black")
canvas.pack()

canvas.create_oval(160, 230, 340, 280, fill="gray40", outline="")

canvas.create_oval(150, 100, 350, 300, fill="#ff7c1e", outline="")

canvas.create_oval(30, 30, 50, 50, fill="#ffffff", outline="")

canvas.create_oval(100, 100, 250, 250, fill="#00bbff", outline="")

janela.mainloop()