import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
from func import extract_data
from tqdm import tqdm

start_time = time.time()

#link da tabela do campeonato no ano de 2023
url = "https://optaplayerstats.statsperform.com/pt_BR/soccer/brasileir%C3%A3o-s%C3%A9rie-a-2023/czjx4rda7swlzql5d1cq90r8/opta-player-stats"

option = Options()
option.headless = True
driver = webdriver.Firefox()

driver.get(url)
time.sleep(10)
html = driver.page_source

soup = BeautifulSoup(html, 'html.parser')

table = soup.find('table', class_='Opta-Crested')

driver.quit()

links = table.find_all('a', class_='Opta-MatchLink Opta-Ext')

# Extraia os atributos href dos links
part = [link['href'] for link in links]

print("Total de Partidas:",len(part))

data_partidas = pd.DataFrame()

for partida in tqdm(part, desc="Processando partidas"):
    p = extract_data(partida, 7)
    data_partidas = pd.concat([data_partidas, p], ignore_index=True)


print(data_partidas)
data_partidas.to_csv('partidas.csv', index=False)

end_time = time.time()
execution_time_seconds = end_time - start_time
execution_time_minutes = execution_time_seconds / 60
print(f"Tempo total de execução: {execution_time_minutes:.2f} minutos")