import tkinter as tk
from tkinter import messagebox

def calcular_valor():
    try:
        kg_str = entry_kg.get().replace(",", ".")
        preco_str = entry_preco.get().replace(",", ".")

        kg = float(kg_str)
        preco = float(preco_str)

        valor_total = kg * preco
        resultado_label.config(text=f"O valor total do produto é: R${valor_total:.2f}")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, digite valores numéricos válidos.")

def resetar():
    entry_kg.delete(0, tk.END)
    entry_preco.delete(0, tk.END)
    resultado_label.config(text="")

janela = tk.Tk()
janela.title("Calculadora de Valor de Produto")

frame = tk.Frame(janela)
frame.pack(padx=20, pady=20)

label_kg = tk.Label(frame, text="Digite a quantidade em kg do produto:")
label_kg.pack()

entry_kg = tk.Entry(frame)
entry_kg.pack()

label_preco = tk.Label(frame, text="Digite o preço do produto por kg:")
label_preco.pack()

entry_preco = tk.Entry(frame)
entry_preco.pack()

calcular_button = tk.Button(frame, text="Calcular", command=calcular_valor)
calcular_button.pack()

resultado_label = tk.Label(frame, text="")
resultado_label.pack()

resetar_button = tk.Button(frame, text="Resetar", command=resetar)
resetar_button.pack()

janela.mainloop()
