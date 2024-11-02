import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
from tqdm import tqdm
from func import extract_data

start_time = time.time()

# URL of the championship
url = "https://optaplayerstats.statsperform.com/pt_BR/soccer/brasileir%C3%A3o-s%C3%A9rie-a-2023/czjx4rda7swlzql5d1cq90r8/opta-player-stats"

# Set up Selenium with headless Firefox
option = Options()
option.headless = True
driver = webdriver.Firefox(options=option)

# Load the page
driver.get(url)
time.sleep(10)
html = driver.page_source

# Parse the HTML with BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Find the table with the class 'Opta-Crested'
table = soup.find('table', class_='Opta-Crested')

# Close the driver
driver.quit()

# Extract the href attributes of the links
part = [link['href'] for link in table.find_all('a', class_='Opta-MatchLink Opta-Ext')]

print("Total Matches:", len(part))

data_partidas = pd.DataFrame()

# Process each match link
for partida in tqdm(part, desc="Processing matches"):
    p = extract_data(partida, 9)
    data_partidas = pd.concat([data_partidas, p], ignore_index=True)
    data_partidas.to_csv('output/matches.csv', index=False)

print(data_partidas)

end_time = time.time()
execution_time_seconds = end_time - start_time
execution_time_minutes = execution_time_seconds / 60
print(f"Execution Time: {execution_time_minutes:.2f} minutes")

