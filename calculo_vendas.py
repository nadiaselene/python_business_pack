# Implemente um programa em Python que receba uma lista de dicionários representando vendas,
# onde cada item contém: nome do produto, quantidade vendida e valor unitário.
# O programa deve calcular e exibir:
# total vendido no mês,
# ticket médio,
# produto mais vendido e
# valor total por produto

vendas = [
    {"produto" : "yoga mat",
    "preço" : 149,
    "quantidade" : 12},

    {"produto" : "bloco",
    "preço" : 55,
    "quantidade" : 22},
    
    {"produto" : "bolster",
    "preço" : 225,
    "quantidade" : 8},
   
    {"produto" : "incenso",
    "preço" : 19,
    "quantidade" : 18}
]

total_vendido = 0
valor_venda = 0

for infos_vendas in vendas:
    quantidade = infos_vendas["quantidade"]
    preço = infos_vendas["preço"]
    produto = infos_vendas["produto"]
    
    total_vendido += quantidade
    valor_venda += preço

    print(f"O produto", infos_vendas["produto"], "vendeu um total de", quantidade*preço, "reais")

qtd_venda = [infos_vendas["quantidade"] for infos_vendas in vendas]
max_vendas = max(qtd_venda)

for produto in vendas:
    if produto["quantidade"] == max_vendas:
        produto_top = produto["produto"]
        break


print("O total vendido no mês foi de", total_vendido, "unidades")
print("O valor total das vendas no mês foi de", total_vendido*valor_venda, "reais")
print("O ticket médio do mês foi de", (total_vendido*valor_venda)/total_vendido, "reais")
print("O produto com mais vendas foi o", produto_top, "com um total de", max_vendas, "unidades vendidas")



