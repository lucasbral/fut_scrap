import pandas as pd
import numpy as np

df = pd.read_csv('output/partidas.csv')

links_array = df['link'].values



import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
from func import extract_data
from tqdm import tqdm


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
new_links = [link for link in part if link not in links_array]

print(new_links)





