## esse script foi feito com a ajuda do chatgpt, como forma de deixar ainda mais visual a ideia de comparação entre unidades
## foi usado também para estudar e algumas alterações foram feitas a partir do código-mãe

import tkinter as tk
from tkinter import ttk

# =======================
# 1. Carregar o CSV
# =======================
arquivo = "unidades_AOM.csv"

dados = dict()

with open(arquivo, encoding='utf-8') as open_file:
    aom = open_file.readlines()

chaves = aom[0].strip("\n").split(",")

for cat in chaves:
    dados[cat] = []

for infos in aom[1:]:
    valores = infos.strip("\n").split(",")
    for indice in range(len(valores)):
        dados[chaves[indice]].append(valores[indice])

# Lista de unidades para o combobox
lista_unidades = dados["nome"]

# =======================
# 2. Função de comparação
# =======================
def comparar():
    unidade_1 = combo1.get()
    unidade_2 = combo2.get()

    if unidade_1 not in dados["nome"] or unidade_2 not in dados["nome"]:
        resultado_label.config(text="Unidade inválida")
        return

    # -------- Unidade 1 --------
    idx1 = dados["nome"].index(unidade_1)

    hp_1 = int(dados["hp"][idx1])
    ataque_1 = int(dados["ataque"][idx1])
    defesa_1 = int(dados["defesa"][idx1])

    força_1 = hp_1 / (ataque_1 + defesa_1)

    # -------- Unidade 2 --------
    idx2 = dados["nome"].index(unidade_2)

    hp_2 = int(dados["hp"][idx2])
    ataque_2 = int(dados["ataque"][idx2])
    defesa_2 = int(dados["defesa"][idx2])

    força_2 = hp_2 / (ataque_2 + defesa_2)

    # Resultado
    if força_1 > força_2:
        resultado_label.config(
            text=f"{unidade_1} venceria em uma disputa com {unidade_2}."
        )
    elif força_2 > força_1:
        resultado_label.config(
            text=f"{unidade_2} venceria em uma disputa com {unidade_1}."
        )
    else:
        resultado_label.config(
            text=f"Os soldados são igualmente fortes."
        )

# =======================
# 3. Construir a GUI
# =======================
janela = tk.Tk()
janela.title("Batalha de soldados - Age of Mythology")
janela.geometry("400x200")
janela.configure(bg="#725374")

# Label e combobox da primeira unidade
ttk.Label(janela, text="Escolha o primeiro soldado:").grid(row=0, column=0, padx=10, pady=10)
combo1 = ttk.Combobox(janela, values=lista_unidades, state="readonly")
combo1.grid(row=0, column=1)

# Label e combobox da segunda unidade
ttk.Label(janela, text="Escolha o segundo soldado:").grid(row=1, column=0, padx=10, pady=10)
combo2 = ttk.Combobox(janela, values=lista_unidades, state="readonly")
combo2.grid(row=1, column=1)

# Botão para comparar
botao = ttk.Button(janela, text="Comparar as unidades", command=comparar)
botao.grid(row=2, column=0, columnspan=2, pady=15)

# Label para mostrar o resultado
resultado_label = ttk.Label(janela, text="")
resultado_label.grid(row=3, column=0, columnspan=2, pady=10)

# Iniciar a interface
janela.mainloop()
