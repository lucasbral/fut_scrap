import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
import json

def extract_data(url: str, delay: int) -> pd.DataFrame:
    """
    Faz web scraping dos dados de todas as partidas do Campeonato Brasileiro a partir do link fornecido e
    retorna os dados em um DataFrame do Pandas.

    Args:
        url (str): A URL da página contendo os dados das partidas do Campeonato Brasileiro.
        delay (int): Tempo em segundos para aguardar entre as requisições, útil para evitar sobrecarga no servidor.

    Returns:
        pd.DataFrame: DataFrame contendo as informações das partidas, como times, datas, placares, etc.
    """

    option = Options()
    option.headless = True
    driver = webdriver.Firefox(options=option)

    driver.get(url)
    time.sleep(delay)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    driver.quit()

    # Encontre os times da casa e visitantes
    home_teams = soup.find_all('td', class_=lambda x: x and x.startswith('Opta-Team Opta-Home Opta-Team-Left Opta-TeamName'))
    away_teams = soup.find_all('td', class_=lambda x: x and x.startswith('Opta-Team Opta-Away Opta-Team-Right Opta-TeamName'))

    # Extraia os nomes dos times
    home_team_names = [team.text.strip() for team in home_teams]
    away_team_names = [team.text.strip() for team in away_teams]

    # Encontre os placares dos times da casa e visitantes
    match_widget_container = soup.find('div', class_='match-widget-container')
    home_scores = match_widget_container.find_all('td', class_=lambda x: x and x.startswith('Opta-Score Opta-Home Opta-Team'))
    away_scores = match_widget_container.find_all('td', class_=lambda x: x and x.startswith('Opta-Score Opta-Away Opta-Team'))

    # Extraia os placares dos times
    home_team_score = [score.find('span', class_='Opta-Team-Score').text.strip() for score in home_scores]
    away_team_score = [score.find('span', class_='Opta-Team-Score').text.strip() for score in away_scores]

    game_dates = soup.find_all('span', class_='Opta-Date')
    game_date_text = [date.text.strip() for date in game_dates]

    # Encontre os dados da partida
    match_data = soup.find_all('div', class_='Opta-Matchdata')
    match_data_text = [data.text.strip() for data in match_data]
    if match_data_text:
        match_data_parts = match_data_text[0].split('\n')
        est = public = arbitro = "No data"
        for part in match_data_parts:
            if part.startswith('Est'):
                est = part.replace('Est', '').strip()
            elif part.startswith('P'):
                public = part.replace('P', '').strip()
            else:
                arbitro = part.strip()
    else:
        est = public = arbitro = "No data"

    # Events club home
    home_events_list = soup.find_all('ul', class_='Opta-Events Opta-Home')
    events_home = []
    for home_events in home_events_list:
        events_home.extend(home_events.find_all('li', class_=lambda x: x and x.startswith('Opta-MatchEvent Opta-Event-Type')))

    yellow_cards_home = []
    red_cards_home = []
    gols_home = []

    for event in events_home:
        minute = event.find('span', class_='Opta-Event-Min').text.strip().replace('\u200e', '').replace('\u200f', '')
        if event.find('p', class_='Opta-Icon Opta-IconYellow'):
            player = event.find('img')['alt'].strip()
            yellow_cards_home.append({'player': player, 'minute': minute})
        elif event.find('p', class_='Opta-Icon Opta-IconRed'):
            player = event.find('img')['alt'].strip()
            red_cards_home.append({'player': player, 'minute': minute})
        elif event.find('p', class_='Opta-Icon Opta-IconGoal'):
            player = event.find('img')['alt'].strip()
            gols_home.append({'player': player, 'minute': minute,'cont':0,'penal':0})
        elif event.find('p', class_='Opta-Icon Opta-IconOwn'):
            player = event.find('img')['alt'].strip()
            gols_home.append({'player': player, 'minute': minute,'cont':1,'penal':0})
        elif event.find('p', class_='Opta-Icon Opta-IconPenGoal'):
            player = event.find('img')['alt'].strip()
            gols_home.append({'player': player, 'minute': minute,'cont':0,'penal':1})

    # Events club away
    away_events_list = soup.find_all('ul', class_='Opta-Events Opta-Away')
    events_away = []
    for away_events in away_events_list:
        events_away.extend(away_events.find_all('li', class_=lambda x: x and x.startswith('Opta-MatchEvent Opta-Event-Type')))

    yellow_cards_away = []
    red_cards_away = []
    gols_away = []

    for event in events_away:
        minute = event.find('span', class_='Opta-Event-Min').text.strip().replace('\u200e', '').replace('\u200f', '')
        if event.find('p', class_='Opta-Icon Opta-IconYellow'):
            player = event.find('img')['alt'].strip()
            yellow_cards_away.append({'player': player, 'minute': minute})
        elif event.find('p', class_='Opta-Icon Opta-IconRed'):
            player = event.find('img')['alt'].strip()
            red_cards_away.append({'player': player, 'minute': minute})
        elif event.find('p', class_='Opta-Icon Opta-IconGoal'):
            player = event.find('img')['alt'].strip()
            gols_away.append({'player': player, 'minute': minute,'cont':0,'penal':0})
        elif event.find('p', class_='Opta-Icon Opta-IconOwn'):
            player = event.find('img')['alt'].strip()
            gols_away.append({'player': player, 'minute': minute,'cont':1,'penal':0})
        elif event.find('p', class_='Opta-Icon Opta-IconPenGoal'):
            player = event.find('img')['alt'].strip()
            gols_away.append({'player': player, 'minute': minute,'cont':0,'penal':1})

    # Criação do DataFrame
    data = {
        'home_team': home_team_names,
        'away_team': away_team_names,
        'home_team_score': home_team_score,
        'away_team_score': away_team_score,
        'game_date': game_date_text,
        'stadium': est,
        'public': public,
        'ref': arbitro,
        'yellow_cards_home': json.dumps(yellow_cards_home),
        'red_cards_home': json.dumps(red_cards_home),
        'gols_home': json.dumps(gols_home),
        'yellow_cards_away': json.dumps(yellow_cards_away),
        'red_cards_away': json.dumps(red_cards_away),
        'gols_away': json.dumps(gols_away)
    }

    # Criação do DataFrame sem listas aninhadas
    df = pd.DataFrame(data)
    return df

#pd.set_option('display.max_columns', None)
#df = extract_data("https://optaplayerstats.statsperform.com/pt_BR/soccer/brasileir%C3%A3o-s%C3%A9rie-a-2023/czjx4rda7swlzql5d1cq90r8/match/view/darutr6zq3l6dxq434ifndg5w/match-summary", 6)

##print(df)
#df.to_csv('partidas.csv', index=False)


#url_p = "https://optaplayerstats.statsperform.com/pt_BR/soccer/brasileir%C3%A3o-s%C3%A9rie-a-2023/czjx4rda7swlzql5d1cq90r8/match/view/darutr6zq3l6dxq434ifndg5w/match-summary"
#url_contra = "https://optaplayerstats.statsperform.com/pt_BR/soccer/brasileir%C3%A3o-s%C3%A9rie-a-2023/czjx4rda7swlzql5d1cq90r8/match/view/d9r0p4ogsqatqq3gn5qv2krh0/match-summary"