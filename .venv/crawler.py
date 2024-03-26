import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

url = "https://www.vivareal.com.br/aluguel/sp/campos-do-jordao/"
driver.get(url)

arr_titulos = driver.find_elements(By.CSS_SELECTOR, ".property-card__title.js-cardLink.js-card-title")
arr_tamanhos = driver.find_elements(By.CSS_SELECTOR, ".property-card__detail-item.property-card__detail-area")
arr_num_quartos = driver.find_elements(By.CSS_SELECTOR, ".property-card__detail-item.property-card__detail-room.js-property-detail-rooms")
arr_num_banheiros = driver.find_elements(By.CSS_SELECTOR, ".property-card__detail-item.property-card__detail-bathroom.js-property-detail-bathroom")
arr_vagas_garagem = driver.find_elements(By.CSS_SELECTOR, ".property-card__detail-item.property-card__detail-garage.js-property-detail-garages")
arr_precos = driver.find_elements(By.CSS_SELECTOR, ".property-card__price.js-property-card-prices.js-property-card__price-small")

data = []
for i in range(len(arr_titulos)):
    data.append({
        'Titulo': arr_titulos[i].text,
        'Tamanho': arr_tamanhos[i].text,
        'Nmero de Quartos': arr_num_quartos[i].text,
        'Numero de Banheiros': arr_num_banheiros[i].text,
        'Vagas de Garagem': arr_vagas_garagem[i].text,
        'Preco': arr_precos[i].text

    })

df = pd.DataFrame(data)

df.to_csv('campos_dataset.csv', index=False)

driver.quit()
