# Desenvolva um programa em Python que seja responsável por calcular o preço final de um produto
# com base em faixas de preço definidas.
# O usuário deve informar o valor de compra, e a função deve aplicar automaticamente o percentual de desconto correspondente à faixa.
# O programa deve exibir o preço final formatado e o percentual aplicado.

preço = float(input("Informe o preço do produto: "))

categoria = {
        range(0,11) : 0.1,
        range(11,31) : 0.2,
        range(31, 61) : 0.3,
        range(61, 101) : 0.4
    }

for faixa, desconto in categoria.items():
    if preço in faixa:
        preço_final = preço - (preço * desconto)

        print("O preço final a ser pago é igual a", preço_final, "reais.")
        print("O percentual de desconto aplicado foi igual a", desconto*100, "%.")

