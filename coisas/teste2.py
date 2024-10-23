import pandas as pd
import os


colunas = ["Foto Frontal", "Foto Lateral", "Foto Interior", "Foto Traseira"]

if os.path.exists("fotos_veiculos.xlsx"):
    df = pd.read_excel("fotos_veiculos.xlsx")
else:
    df = pd.DataFrame(columns=colunas)

while True:
    entrada = input("Insira as fotos (ou pressione Enter para sair): ")
    
    if entrada == '':
        break

    try:
        f, l, i, t = map(str.strip, entrada.split())

        novo_dado = pd.DataFrame([[f, l, i, t]], columns=colunas)

        df = pd.concat([df, novo_dado], ignore_index=True)

    except ValueError:
        print("Por favor, insira exatamente quatro valores separados por espaço.")

df.to_excel("fotos_veiculos.xlsx", index=False)
print("Planilha atualizada com sucesso!")
