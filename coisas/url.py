import requests
from bs4 import BeautifulSoup

def puxa_pagina(url):
    try:
        response = requests.get(url)

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

        soup = BeautifulSoup(html, 'html.parser')

        # Encontra todas as divs com a classe 'lg-item'
        items = soup.find_all('div', class_='lg-item')

        # Procura pela div que contém a classe 'lg-current'
        for item in items:
            if 'lg-current' in item.get('class', []):
                img_tag = item.find('img', class_='lg-object lg-image')
                if img_tag:
                    main_image_url = img_tag.get('src')
                    print(f"URL da imagem principal: {main_image_url}")
                    return main_image_url
                else:
                    print("Nenhuma imagem encontrada na div 'lg-current'.")
                    return None

        print("Div com classe 'lg-current' não encontrada.")
    except Exception as e:
        print(f"Erro ao tentar ler a página: {e}")

# URL: https://alvoradaveiculos.com.br/carros/jeep/compass-limited-2-0-4x4-diesel-16v-aut/2021/354228
# URL2: https://alvoradaveiculos.com.br/carros/jeep/compass-limited-2-0-4x4-diesel-16v-aut/2021/354228#lg=1&slide=0
url = input("Digite a URL da página que deseja salvar: ")
puxa_pagina(url)
imagem = puxa_main_image_url()
