# Barrage Setup Assistant

![CI](https://github.com/pijor189/BarrageSetupAssistant/actions/workflows/ci.yml/badge.svg)
![codecov](https://codecov.io/gh/pijor189/BarrageSetupAssistant/branch/main/graph/badge.svg?token=72470889-6903-4fd7-8b78-6aa15a96ef74)

## About The Project

**Barrage Setup Assistant** is an application that fully automates the random selection of all necessary components for a game of Barrage board game. With this application, players can focus on the game itself rather than the time-consuming process of preparing the game components.

The project aims to:
- **Automatically randomize** the complete game setup
- **Eliminate errors** from manual game preparation
- **Provide speed and convenience** for players

## Technologies

The project was built using the following technologies:

| Technology | Purpose |
|---|---|
| **Python 3.x** | Programming language |
| **pytest** | Unit testing framework |
| **GitHub Actions** | Continuous Integration (CI) |
| **Codecov** | Code coverage reporting |
| **JSON** | Configuration data storage format |

## Future Development
The project is in active development. Our plans for the future include:

🌐 Web Application – version accessible in a web browser

📱 Mobile Application – support for iOS and Android devices

✨ Additional Features – expanding simulation and configuration capabilities

## Installation

### Requirements
- Python 3.x
- Git

### Cloning the Repository

To download the project to your machine, use the following command:

```bash
git clone https://github.com/pijor189/BarrageSetupAssistant.git
cd BarrageSetupAssistant
```

### Installing Dependencies

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Running the Application

To run the application as a CLI:

```bash
python main.py
```

## Running Tests

The project includes a comprehensive test suite. To run the tests, execute:

```bash
pytest .
```

To display a code coverage report:

```bash
pytest --cov
```
