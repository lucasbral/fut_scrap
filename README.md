# fut-scrap

A project for scraping football data.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)

## Installation

To install and set up the project, follow these steps:

1. **Clone the repository**:
   ```sh
   git clone https://github.com/yourusername/fut-scrap.git
   cd fut-scrap

2. **Install Poetry**: If you haven't installed Poetry yet, you can do so using the official installation script:
    ```sh
    curl -sSL https://install.python-poetry.org | python3 -

3. **Install dependencies**: Use Poetry to install the project dependencies:
    ```sh
    poetry install

4. **Select Championship**: Visit [Opta Player Stats](https://optaplayerstats.statsperform.com) and choose the championship you are interested in. For example: [Brasileirão Série A 2023](https://optaplayerstats.statsperform.com/pt_BR/soccer/brasileir%C3%A3o-s%C3%A9rie-a-2023/czjx4rda7swlzql5d1cq90r8/opta-player-stats).

Then, update the `url` variable in `main.py` with this link.

5. **Run `main.py`**: To run the project, use the following command:
    ```sh
    poetry run python main.py
    ```

6. **Output**: After `main.py` completes, a file will be generated containing information about all the matches of the selected championship.

## Usage
The output file is a csv with info:

| Column               | Description                                                                                     |
|----------------------|-------------------------------------------------------------------------------------------------|
| **home_team**        | The name of the home team.                                                                      |
| **away_team**        | The name of the away team.                                                                      |
| **home_team_score**  | The number of goals scored by the home team.                                                    |
| **away_team_score**  | The number of goals scored by the away team.                                                    |
| **game_date**        | The date and time when the match was played.                                                    |
| **stadium**          | The name of the stadium where the match was played.                                             |
| **public**           | The number of spectators present at the match. If the data is not available, it is marked as "No data". |
| **ref**              | The name of the referee who officiated the match.                                               |
| **yellow_cards_home**| A JSON array containing information about yellow cards received by players of the home team. Each object in the array includes: <br> - **player**: The name of the player who received the yellow card. <br> - **minute**: The minute when the yellow card was given. |
| **red_cards_home**   | A JSON array containing information about red cards received by players of the home team. Each object in the array includes: <br> - **player**: The name of the player who received the red card. <br> - **minute**: The minute when the red card was given. |
| **gols_home**        | A JSON array containing information about goals scored by players of the home team. Each object in the array includes: <br> - **player**: The name of the player who scored the goal. <br> - **minute**: The minute when the goal was scored. <br> - **cont**: Indicates if the goal was an own goal (1 for own goal, 0 otherwise). <br> - **penal**: Indicates if the goal was a penalty (1 for penalty, 0 otherwise). |
| **yellow_cards_away**| A JSON array containing information about yellow cards received by players of the away team. Each object in the array includes: <br> - **player**: The name of the player who received the yellow card. <br> - **minute**: The minute when the yellow card was given. |
| **red_cards_away**   | A JSON array containing information about red cards received by players of the away team. Each object in the array includes: <br> - **player**: The name of the player who received the red card. <br> - **minute**: The minute when the red card was given. |
| **gols_away**        | A JSON array containing information about goals scored by players of the away team. Each object in the array includes: <br> - **player**: The name of the player who scored the goal. <br> - **minute**: The minute when the goal was scored. <br> - **cont**: Indicates if the goal was an own goal (1 for own goal, 0 otherwise). <br> - **penal**: Indicates if the goal was a penalty (1 for penalty, 0 otherwise). |
| **sec_card_home**    | A JSON array containing information about second yellow cards received by players of the home team. Each object in the array includes: <br> - **player**: The name of the player who received the second yellow card. <br> - **minute**: The minute when the second yellow card was given. |
| **sec_card_away**    | A JSON array containing information about second yellow cards received by players of the away team. Each object in the array includes: <br> - **player**: The name of the player who received the second yellow card. <br> - **minute**: The minute when the second yellow card was given. |
| **link**             | The URL link to the detailed match statistics.                                                  |


## Contributing
Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (git checkout -b feature-branch).
3. Make your changes.
4. Commit your changes (git commit -m 'Add new feature').
5. Push to the branch (git push origin feature-branch).
6. Open a pull request.