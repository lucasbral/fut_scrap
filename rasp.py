import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
from func import extract_data
from tqdm import tqdm

start_time = time.time()

#link da tabela do campeonato no ano de 2023
url = "https://optaplayerstats.statsperform.com/pt_BR/soccer/brasileir%C3%A3o-s%C3%A9rie-a-2021/czjx4rda7swlzql5d1cq90r8/opta-player-stats"

chrome_options = Options()
chrome_options.add_argument('--headless')  # Run in headless mode if desired
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

# Specify the path to the chromedriver
chromedriver_path = '/usr/lib/chromium-browser/chromedriver'  # Adjust this path as necessary

# Create a Service object with the chromedriver path
service = Service(chromedriver_path)

# Initialize the Chrome WebDriver with service and options
driver = webdriver.Chrome(service=service, options=chrome_options)

url = "https://optaplayerstats.statsperform.com/pt_BR/soccer/brasileir%C3%A3o-s%C3%A9rie-a-2023/czjx4rda7swlzql5d1cq90r8/match/view/dbtewel5a77wv34aurem31n2s/match-summary"

driver.get(url)
time.sleep(8)
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
driver.quit()

table = soup.find('table', class_='Opta-Crested')

driver.quit()

links = table.find_all('a', class_='Opta-MatchLink Opta-Ext')

# Extraia os atributos href dos links
part = [link['href'] for link in links]

print("Total de Partidas:",len(part))

#data_partidas = pd.DataFrame()

#for partida in tqdm(part, desc="Processando partidas"):
#    p = extract_data(partida, 9)
#    data_partidas = pd.concat([data_partidas, p], ignore_index=True)


#print(data_partidas)
#data_partidas.to_csv('output/partidas.csv', index=False)

end_time = time.time()
execution_time_seconds = end_time - start_time
execution_time_minutes = execution_time_seconds / 60
print(f"Tempo total de execução: {execution_time_minutes:.2f} minutos")