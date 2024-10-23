from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

servico = Service(ChromeDriverManager().install()) 
navegador = webdriver.Chrome(service=servico)

navegador.get("https://alvoradaveiculos.com.br/carros/jeep/compass-limited-2-0-4x4-diesel-16v-aut/2021/354228")

navegador.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[5]/a').click()

div_element = navegador.find_element(By.XPATH, '/html/body/div[9]/div/div[1]')

div_html = div_element.get_attribute('outerHTML')

with open("div_content.html", "w", encoding="utf-8") as file:
    file.write(div_html)

print("HTML da div foi salvo em 'div_content.html'.")

# Aguardar a confirmação para fechar o navegador
input("Pressione Enter para fechar o navegador...")

# Fecha o navegador
navegador.quit()
