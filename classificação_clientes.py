# Implemente um programa que receba um dicionário contendo clientes associados a um valor de compras realizadas.
# Com base em limites definidos pelo usuário ou pelo sistema, o programa deve classificar cada cliente em categorias como Bronze, Prata ou Ouro.
# O resultado deve ser retornado em um novo dicionário.

clientes = {
"Joao" : 1270.50,
"Maria" : 550.8,
"Jorge" : 4590.7,
"Mauro" : 234.5,
"Cleide" : 3935.1,
"Miriam" : 1822.9
}

categorias = {
"Bronze" : range(0,1500),
"Prata" : range(1500,3000),
"Ouro" : range(3000,9999999999)
}

resultado = {}

for nome, compra in clientes.items():
    compra_int = int(compra)
    for cat, valor in categorias.items():
        if compra_int in valor:
            resultado[nome] = cat

print(resultado)
