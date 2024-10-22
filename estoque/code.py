import pandas as pd

# Carregar a planilha
arquivo_excel = "estoque.xlsx"  
df = pd.read_excel(arquivo_excel)

# Função para definir a transmissão automaticamente
def definir_transmissao(versao):
    if pd.isna(versao):  # Verifica se o valor é NaN
        return "None"
    if "Aut" in versao:
        return "Automático"
    elif "Mec" in versao or "Manual" in versao:
        return "Manual"
    else:
        return "None"

# Preenche a coluna Transmissão com base na versão
df["Transmissão"] = df["Versão"].apply(definir_transmissao)

# Lê o arquivo de bloco de notas com os dados manuais
arquivo_txt = "none car.txt"  
linhas_manual = {}

# Ler o arquivo txt e preencher o dicionário com os valores
with open(arquivo_txt, "r") as arquivo:
    for line in arquivo:
        # Divide a linha e trata se tiver mais ou menos de dois elementos
        linha_info = line.strip().split()
        if len(linha_info) == 2:
            linha, transmissao = linha_info
            linhas_manual[int(linha)] = "Automático" if transmissao == "Aut" else "Manual"

# Exibe as linhas do arquivo TXT lidas para garantir que foram lidas corretamente
print("Linhas do arquivo TXT:", linhas_manual)

# Atualiza os valores da coluna 'Transmissão' com base nas linhas fornecidas apenas onde o valor é 'None'
for linha, transmissao in linhas_manual.items():
    # Certifique-se de que o índice exista no DataFrame e que a transmissão atual seja "None"
    if linha - 1 in df.index and df.at[linha - 1, "Transmissão"] == "None":
        print(f"Atualizando linha {linha} para {transmissao}")
        df.at[linha - 1, "Transmissão"] = transmissao
    else:
        print(f"Linha {linha} já preenchida ou não encontrada no DataFrame")

# Salva as alterações no arquivo Excel
df.to_excel(arquivo_excel, index=False)

print("A coluna 'Transmissão' foi preenchida com sucesso!")
