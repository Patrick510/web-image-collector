from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

servico = Service(ChromeDriverManager().install())

navegador = webdriver.Chrome(service=servico)

navegador.get("https://alvoradaveiculos.com.br/carros/jeep/compass-limited-2-0-4x4-diesel-16v-aut/2021/354228")

navegador.find_element('xpath', '/html/body/div[3]/div[1]/div[5]/a').click()

input("Pressione Enter para fechar o navegador...")

navegador.quit()