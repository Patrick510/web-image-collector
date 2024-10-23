from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

servico = Service(ChromeDriverManager().install())

driver = webdriver.Chrome(service=servico)

driver.get("https://www.google.com")

input("Pressione Enter para fechar o navegador...")

driver.quit()