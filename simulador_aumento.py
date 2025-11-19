# Crie um programa que receba uma lista de produtos com suas categorias, preços e um dicionário
# contendo categorias associadas a percentuais de aumento.
# Ele deve retornar uma nova lista com os preços atualizados, preservando a estrutura original dos dados.

lista = [
    {"produto" : "maçã", "categoria" : "fruta","preço" : 1.5},
    {"produto" : "pera", "categoria" : "fruta","preço" : 1.2},
    {"produto" : "banana", "categoria" : "fruta","preço": 0.9},
    {"produto" : "garfo", "categoria" : "utensílios","preço" : 8.5},
    {"produto" : "faca", "categoria" : "utensílios","preço" : 6.7},
    {"produto" : "copo", "categoria" : "utensílios","preço": 5.5},
    {"produto" : "leite", "categoria" : "bebidas","preço" : 3.5},
    {"produto" : "suco", "categoria" : "bebidas","preço" : 4.2},
    {"produto" : "agua de coco", "categoria" : "bebidas","preço": 5.8},
]

ajuste = [
    {"categoria" : "bebidas", "aumento" : 1.25},
    {"categoria" : "fruta", "aumento" : 1.1},
    {"categoria" : "utensílios", "aumento" : 1.2}
    ]


for conjunto in lista:
    produto = conjunto["produto"]
    categoria_1 = conjunto["categoria"]
    preço = conjunto["preço"]

    for tabela in ajuste:
        categoria_2 = tabela["categoria"]
        aumento = tabela["aumento"]

        if categoria_1 == categoria_2:
            valor_final = preço * aumento

            print(f"O produto", produto, "teve um aumento e passou a custar", valor_final, "reais")
