import tkinter as tk

janela = tk.Tk()
janela.title("Calculadora")
janela.geometry("400x250")


def calculo():
    try:
        valor1 = float(entrada1.get())
        valor2 = float(entrada2.get())
        operacao = EntradaOperacao.get()

        if operacao == "+":
            calcular = valor1 + valor2
        elif operacao == "-":
            calcular = valor1 - valor2
        elif operacao == "*":
            calcular = valor1 * valor2
        elif operacao == "/":
            calcular = valor1 / valor2
        else:
            result.config(text="Operação inválida")
            return

        result.config(text=f"Resultado: {calcular}")

    except:
        result.config(text="Informe números válidos")


# ----------- Interface -----------

num1 = tk.Label(janela, text="Primeiro número:")
num1.grid(row=0, column=0, padx=10, pady=10)

entrada1 = tk.Entry(janela)
entrada1.grid(row=0, column=1)

Labeloperacao = tk.Label(janela, text="Operação (+ - * /):")
Labeloperacao.grid(row=1, column=0)

EntradaOperacao = tk.Entry(janela)
EntradaOperacao.grid(row=1, column=1)

num2 = tk.Label(janela, text="Segundo número:")
num2.grid(row=2, column=0, padx=10, pady=10)

entrada2 = tk.Entry(janela)
entrada2.grid(row=2, column=1)

result = tk.Label(janela, text="Resultado:")
result.grid(row=3, column=0, columnspan=2, pady=10)

botao = tk.Button(janela, text="Calcular", command=calculo)
botao.grid(row=4, column=0, columnspan=2, pady=10)

janela.mainloop()