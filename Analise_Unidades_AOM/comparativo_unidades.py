## para esse comparativo vamos considerar que a força total é o HP divido pela soma do ataque e defesa

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


unidade_1 = input("Informe a primeira unidade: ")
unidade_2 = input("Informe a segunda unidade: ")

if unidade_1 in dados["nome"]:
    idx = dados["nome"].index(unidade_1)

    hp_1 = dados["hp"][idx]
    ataque_1 = dados["ataque"][idx]
    defesa_1 = dados["defesa"][idx]

    força_1 = int(hp_1)/int(ataque_1 + defesa_1)

else:
    print("Unidade não encontrada.")


if unidade_2 in dados["nome"]:
    idx = dados["nome"].index(unidade_1)

    hp_2 = dados["hp"][idx]
    ataque_2 = dados["ataque"][idx]
    defesa_2 = dados["defesa"][idx]

    força_2 = int(hp_2)/int(ataque_2 + defesa_2)
else:
    print("Unidade não encontrada.")    

if força_1 > força_2:
    print(f"A unidade {unidade_1} venceria em uma disputa com a unidade {unidade_2}.")
else:
    print(f"A unidade {unidade_2} venceria em uma disputa com a unidade {unidade_1}.")
