from selenium import webdriver 
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd
import os

serviço = Service(ChromeDriverManager().install()) 
navegador = webdriver.Chrome(service=serviço)

def chama_pagina(url):
    navegador.get(url)

    try:
        botao_inicial = WebDriverWait(navegador, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[1]/div[5]/a'))
        )
        botao_inicial.click()
    except Exception as e:
        print(f"Erro ao encontrar o elemento inicial: {e}")
        navegador.quit()

    time.sleep(3)

def carrega_imagens():
    for i in range(1, 10):
        try:
            proximo_botao = WebDriverWait(navegador, 10).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/div[9]/div/div[3]/button[2]"))
            )
            proximo_botao.click()
            time.sleep(1)
        except Exception as e:
            print(f"Erro ao clicar no botão: {e}")

def gera_html_e_coleta_imagens():
    # Lista de XPaths das divs que você quer pegar
    xpaths = [
        '/html/body/div[9]/div/div[1]/div[1]',  # FRENTE
        '/html/body/div[9]/div/div[1]/div[2]',  # LATERAL
        '/html/body/div[9]/div/div[1]/div[8]',  # INTERIOR
        '/html/body/div[9]/div/div[1]/div[4]'   # TRASEIRA
    ]

    # Inicializa uma lista para armazenar as URLs das imagens
    urls_imagens = []

    for xpath in xpaths:
        try:
            div_element = WebDriverWait(navegador, 10).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            # Coletando URLs das imagens dentro da div
            imagens = div_element.find_elements(By.TAG_NAME, "img")
            urls = [img.get_attribute("src") for img in imagens]
            urls_imagens.append(urls)  # Adiciona as URLs ao array
            
        except Exception as e:
            print(f"Erro ao encontrar a div com o XPath {xpath}: {e}")
            urls_imagens.append([])  # Adiciona uma lista vazia se ocorrer erro

    # Salva o conteúdo HTML em um arquivo
    with open("div_content.html", "w", encoding="utf-8") as file:
        file.write("\n".join([str(url) for url in urls_imagens]))

    print("HTML das divs foi salvo em 'div_content.html'.")

    return urls_imagens  # Retorna as URLs coletadas

def salvar_em_excel(urls):
    colunas = ["Foto Frontal", "Foto Lateral", "Foto Interior", "Foto Traseira"]

    # Cria ou lê o arquivo Excel existente
    if os.path.exists("fotos_veiculos.xlsx"):
        df = pd.read_excel("fotos_veiculos.xlsx")
    else:
        df = pd.DataFrame(columns=colunas)

    # Adiciona as URLs como nova linha no DataFrame
    novo_dado = pd.DataFrame([urls], columns=colunas)
    df = pd.concat([df, novo_dado], ignore_index=True)

    # Salva o DataFrame no arquivo Excel
    df.to_excel("fotos_veiculos.xlsx", index=False)
    print("Planilha atualizada com sucesso!")

# Chame as funções na ordem desejada
url = "https://alvoradaveiculos.com.br/carros/jeep/compass-limited-2-0-4x4-diesel-16v-aut/2021/354228"
chama_pagina(url)
carrega_imagens()
urls = gera_html_e_coleta_imagens()

# Coleta as URLs e salva no Excel
urls_planilha = []
if urls:  # Verifica se há URLs coletadas
    for i in range(4):  # As divs são 4
        urls_planilha.append(urls[i][0] if urls[i] else "")  # Adiciona a URL ou uma string vazia

salvar_em_excel(urls_planilha)

input("Pressione Enter para fechar o navegador...")
navegador.quit()
