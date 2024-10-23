from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


def busca_carro():
    try:
        servico = Service(ChromeDriverManager().install())
        
        driver = webdriver.Chrome(service=servico)
        driver.get("https://alvoradaveiculos.com.br")

        # Aguarda carregar a página
        time.sleep(3)

        # Localiza o campo de pesquisa pelo ID e insere o termo de pesquisa
        search_box = driver.find_element(By.ID, 'term')
        search_box.send_keys("COMPASS LIMITED 2.0 4x4 Diesel 16V Aut")

        # Localiza o botão de pesquisa pelo ID e clica nele
        search_button = driver.find_element(By.ID, 'submit-search')
        search_button.click()

        # Aguarda carregar os resultados da pesquisa
        time.sleep(3)

        print("Pesquisa realizada com sucesso!")
    
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
    finally:
        # Fecha o navegador
        driver.quit()

# Executa a função de busca
busca_carro()
