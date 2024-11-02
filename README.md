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

## Contributing
Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (git checkout -b feature-branch).
3. Make your changes.
4. Commit your changes (git commit -m 'Add new feature').
5. Push to the branch (git push origin feature-branch).
6. Open a pull request.