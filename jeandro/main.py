import tkinter as tk

numero = 0

def lernome():
    global numero
    numero += 1
    texto.config(text=f"Contador: {numero}")

janela = tk.Tk()

janela.title("Minha janela principal!")
janela.geometry("600x400")

texto = tk.Label(janela, text=f"Contador: {numero}")
texto.pack()

botao = tk.Button(janela, text="+1", command=lernome)
botao.pack()

janela.mainloop()
