# LearnType

## Description

LearnType is a typing game that helps you memorize topics by uploading a text file into the program. It is a simple game that is easy to play and fun to learn with as it integrates a typing styled game with an academic twist.

## Requirements

- Python 3.10.9

## Recommended

- Visual Studio Code
- Python Extension for Visual Studio Code - for linting
- autopep8 Extension for Visual Studio Code - for formatting

## Running the game

```
python3 main.py
```

## Testing

### Unit tests

```
python3 -m unittest discover
```

### UI testing

```
python3 test-ui.py
```

## Python coding standards

- [PEP 8 -- Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/) - Comply to the PEP 8 coding standard, use the autopep8 extension for Visual Studio Code to format your code.
- [PEP 257 -- Docstring Conventions](https://www.python.org/dev/peps/pep-0257/) - Every function should have a docstring.

## Git/PR standards

- PRs should be made directly to the `main` branch
- PR branches should be rebased on `main` before merging
- Feature branches should be named `feat/<feature-name>`
- [Semantic Commit Messages](https://www.conventionalcommits.org/en/v1.0.0/) - Use semantic commit messages.

## File structure

- main.py - main file to run the game
- game.py - game logic
- ui.py - UI logic
- load.py - file loading logic
- test.py - unit tests
- test-ui.py - UI tests
