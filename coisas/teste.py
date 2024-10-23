from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

def puxa_imagens(url):
    # Configura o webdriver do Chrome
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    
    try:
        # Acessa o site
        driver.get(url)
        
        # Aguarda o carregamento da página
        time.sleep(3)  # Ajuste o tempo conforme necessário

        # Busca todas as imagens que estão na galeria de fotos
        img_elements = driver.find_elements(By.CSS_SELECTOR, 'img')

        image_urls = []
        for img in img_elements:
            src = img.get_attribute('src')
            if src and 'carros' in src:  # Filtra URLs de imagens relevantes
                image_urls.append(src)
        
        # Exibe ou faz algo com as URLs das imagens encontradas
        for index, url in enumerate(image_urls):
            print(f"Imagem {index + 1}: {url}")

    finally:
        # Encerra o navegador
        driver.quit()

# Exemplo de uso
url = input("Digite a URL da página que deseja buscar as imagens: ")
puxa_imagens(url)
