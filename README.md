# Snake-RL

This project features a classic Snake game implemented in Python using Pygame, plus an optional reinforcement learning (RL) agent that can be trained with PyTorch. It demonstrates both Python game development and advanced machine learning concepts.

## Features

- **Snake Game (Pygame)**: Control the snake with arrow keys. The game is rendered using Pygame.
- **Optional RL Agent (PyTorch)**: A simple RL setup (Q-learning with a neural network) to learn policies for playing Snake in a headless mode.

## Requirements

- Python 3.9+ (or your chosen Python version)
- Pygame
- PyTorch (optional if you want the RL agent)
- SDL2 libraries (required for Pygame on macOS)

## Setup

```bash
# Clone the repository
git clone https://github.com/<your-username>/snake-rl.git
cd snake-rl

# Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate

# Install SDL dependencies (macOS only)
brew install pkg-config freetype sdl2 sdl2_image sdl2_mixer sdl2_ttf

# Install Python dependencies
pip install pygame==2.1.2

# Optional: Install PyTorch for the RL agent (follow instructions at https://pytorch.org)
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu

# Running the game

From the project’s root directory
python -m src.game.main

Use arrow keys to control the snake.
Close the window or press Ctrl+C in the terminal to exit the game.

# Training the RL Agent (Optional)

If you have PyTorch installed, train the RL agent
python src/agent/train.py

This will run a headless training loop to attempt to learn a policy for playing Snake.

# Directory structure

src/
  game/       # Contains the game logic and rendering code.
  agent/      # Contains RL agent code and training script.
  assets/     # For storing any game assets like images or fonts (currently empty).

# Contributing
Feel free to open issues or submit pull requests on GitHub.

