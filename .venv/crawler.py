import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import re

service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

url = "https://www.vivareal.com.br/aluguel/sp/campos-do-jordao/"
driver.get(url)

arr_titulos = driver.find_elements(By.CSS_SELECTOR, ".property-card__title.js-cardLink.js-card-title")
arr_tamanhos = driver.find_elements(By.CSS_SELECTOR, ".property-card__detail-item.property-card__detail-area")
arr_num_quartos = driver.find_elements(By.CSS_SELECTOR,
                                       ".property-card__detail-item.property-card__detail-room.js-property-detail-rooms")
arr_num_banheiros = driver.find_elements(By.CSS_SELECTOR,
                                         ".property-card__detail-item.property-card__detail-bathroom.js-property-detail-bathroom")
arr_vagas_garagem = driver.find_elements(By.CSS_SELECTOR,
                                         ".property-card__detail-item.property-card__detail-garage.js-property-detail-garages")
arr_precos = driver.find_elements(By.CSS_SELECTOR,
                                  ".property-card__price.js-property-card-prices.js-property-card__price-small")

data = []
for i in range(len(arr_titulos)):
    titulo = arr_titulos[i].text
    tamanho = arr_tamanhos[i].text
    num_quartos = arr_num_quartos[i].text
    num_banheiros = arr_num_banheiros[i].text
    vagas_garagem = arr_vagas_garagem[i].text
    preco_text = arr_precos[i].text

    if any(value.startswith("--") for value in
           [titulo, tamanho, num_quartos, num_banheiros, vagas_garagem, preco_text]):
        continue

    preco = 0

    match = re.search(r'R\$\s?(\d+(?:[,.]\d+)?)(?:\s?/\s?Dia)?', preco_text)
    if match:
        preco = match.group(1).replace('.', '')  # Remove the dot to make it an integer or float

        if '/dia' in preco_text:
            preco = float(preco) * 30

    data.append({
        'Titulo': titulo,
        'Tamanho': tamanho,
        'Nmero de Quartos': num_quartos,
        'Numero de Banheiros': num_banheiros,
        'Vagas de Garagem': vagas_garagem,
        'Preco': preco

    })

df = pd.DataFrame(data)

df.to_csv('campos_dataset.csv', index=False)

driver.quit()
