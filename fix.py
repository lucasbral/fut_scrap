import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
from func import extract_data
from tqdm import tqdm

def fix_missings(url: str, df: pd.DataFrame) -> pd.DataFrame:
    """
    Corrige possíveis jogos faltantes

    Args:
        url (str): A URL da página contendo os dados das partidas do Campeonato Brasileiro.
        df(int): Tempo em segundos para aguardar entre as requisições, útil para evitar sobrecarga no servidor.

    Returns:
        pd.DataFrame: DataFrame contendo as informações das partidas, como times, datas, placares, etc com os jogos faltantes.
    """
   
    options = Options()
    options.headless = True
    options.add_argument('--headless')
    driver = webdriver.Firefox(options=options)

    driver.get(url)
    time.sleep(8)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    driver.quit()

    table = soup.find('table', class_='Opta-Crested')
    links = table.find_all('a', class_='Opta-MatchLink Opta-Ext')

    part = [link['href'] for link in links]

    links_array = df['link'].values

    missing = [link for link in part if link not in links_array]

    for miss in tqdm(missing, desc="Partidas faltantes:"):
        print(miss)
        p = extract_data(miss, 9)
        data_partidas = pd.concat([df, p], ignore_index=True)

    return data_partidas


url = "https://optaplayerstats.statsperform.com/pt_BR/soccer/brasileir%C3%A3o-s%C3%A9rie-a-2022/css9eoc46vca8gkmv5z7603ys/opta-player-stats"

aa = pd.read_csv('output/partidas_22.csv')
print(aa)

b = fix_missings(url,aa)

print(b)

b.to_csv('output/partidas_22.csv', index=False)