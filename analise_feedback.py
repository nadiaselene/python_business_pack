# Desenvolva um programa que receba uma lista de feedbacks de clientes (strings).
# O programa deve analisar:
# contagem total de palavras
# palavras mais frequentes
# porcentagem de menções a palavras-chave de interesse (ex.: “atraso”, “qualidade”, “atendimento”).

lista_fb = ["O atendimento foi impecável",
"Adorei a qualidade dos produtos",
"Serviço efeiciente",
"Muito bom atendimento",
"Problemas no prazo de entrega",
"Processo burocrático",
"Má qualidade do produto"
]


total_palavras = 0

for feedback in lista_fb:
    palavras = feedback.split()
    contagem = len(palavras)
    total_palavras += contagem

print("A lista de feedbacks tem um total de", total_palavras, "palavras")

palavras_chave = ["qualidade", "atendimento", "entrega"]


for chave in palavras_chave:
    cont_chave = 0
    for feedback in lista_fb:
        palavras = feedback.split()
        for palavra in palavras:
            if chave == palavra:
                rep_chave = feedback.count(chave)
                cont_chave += rep_chave
                percentual = cont_chave/total_palavras
    print("A palavra", chave, "foi mencionada", cont_chave, "vezes o que corresponde a", percentual*100, "% menções")






