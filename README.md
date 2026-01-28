# Tic Tac Toe with Minimax AI

This project implements an AI-powered Tic Tac Toe game using the **Minimax algorithm**.  
The AI plays optimally and cannot be beaten.

## Overview

This project is based on the **CS50 AI Tic-Tac-Toe assignment**.

- `runner.py` and the overall project structure were provided by CS50.
- `tictactoe.py` contains **my own implementation** of the game logic and the Minimax decision-making algorithm.
- The AI uses a recursive Minimax search to evaluate game states and select optimal moves.

## Features

- Human vs AI gameplay
- Unbeatable AI using Minimax
- Graphical interface built with Pygame
- Clean separation between game logic and UI

## How It Works

The AI evaluates all possible future game states using Minimax:
- **X** attempts to maximize the score
- **O** attempts to minimize the score
- Terminal states are scored as:
  - `+1` for X win
  - `-1` for O win
  - `0` for a draw

The algorithm recursively explores moves and chooses the optimal action assuming perfect play.

## Requirements

- Python 3.10+
- Pygame

## How to Run

Install dependencies using:

```bash
pip install -r requirements.txt
```
python runner.py

## Credits

This project is inspired by Harvard University's
**CS50 Introduction to Artificial Intelligence with Python**.

All game logic and AI implementation in `tictactoe.py` were written by me as part of the assignment.