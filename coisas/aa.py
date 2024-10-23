import requests
from bs4 import BeautifulSoup

def puxa_pagina(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    
    try:
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            with open('pagina_alvorada_veiculos.html', 'w', encoding='utf-8') as file:
                file.write(response.text)
            print("Página salva com sucesso!")
        else:
            print(f"Erro ao acessar o site. Status code: {response.status_code}")
    except Exception as e:
        print(f"Erro ao tentar acessar a página: {e}")

def puxa_main_image_url():
    try:
        with open('pagina_alvorada_veiculos.html', 'r', encoding='utf-8') as file:
            html = file.read()

        # Faz o parse do HTML com BeautifulSoup
        soup = BeautifulSoup(html, 'html.parser')

        # Encontra a div com a classe 'main-img'
        main_img_div = soup.find('div', class_='main-img')

        if main_img_div:
            img_tag = main_img_div.find('img')
            if img_tag:
                # Extrai o atributo 'src'
                main_image_url = img_tag.get('src')
                print(f"URL da imagem principal: {main_image_url}")
                return main_image_url
            else:
                print("Nenhuma imagem encontrada na div 'main-img'.")
        else:
            print("Div 'main-img' não encontrada.")
    except Exception as e:
        print(f"Erro ao tentar ler a página: {e}")

# URL de exemplo: https://alvoradaveiculos.com.br/carros/jeep/compass-limited-2-0-4x4-diesel-16v-aut/2021/354228
url = input("Digite a URL da página que deseja salvar: ")
puxa_pagina(url)
puxa_main_image_url()
