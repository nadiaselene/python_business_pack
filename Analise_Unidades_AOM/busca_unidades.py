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


unidade = input("Informe uma unidade: ")

if unidade in dados["nome"]:
    idx = dados["nome"].index(unidade)
    
    tipo = dados["tipo"][idx]
    civ = dados["civilizacao"][idx]
    era = dados["era"][idx]

    ouro = dados["custo_ouro"][idx]
    comida = dados["custo_comida"][idx]
    madeira = dados["custo_madeira"][idx]

    bonus = dados["bonus"][idx]

    print(f"A unidade {unidade} é da civilização {civ}, era {era}, tipo {tipo}.")
    print(f"A unidade {unidade} custa {ouro} de ouro, {comida} de comida, {madeira} de madeira. Mas atenção, essa unidade é/tem {bonus}")
else:
    print("Unidade não encontrada.")