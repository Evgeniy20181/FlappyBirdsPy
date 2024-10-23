# Flappy Bird Game
[![Build](https://github.com/Evgeniy20181/FlappyBirdsPy/actions/workflows/python-app.yml/badge.svg)](https://github.com/Evgeniy20181/FlappyBirdsPy/actions/workflows/python-app.yml)
![Flappy Bird](./imgs/flappy_bird_banner.png)

A classic Flappy Bird game built with Python and Pygame.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [How to Play](#how-to-play)
- [Code Overview](#code-overview)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This project is a recreation of the popular Flappy Bird game using Python and the Pygame library. The game involves guiding a bird through pipes by tapping the space bar to make the bird flap its wings. The objective is to pass through as many pipes as possible without hitting them or the ground.

## Features

- Classic Flappy Bird gameplay
- Animated bird with smooth flapping
- Randomly generated pipes
- Score tracking with high score memory
- Game over screen with high score display
- Main menu screen

## Installation

1. **Clone the repository:**
    ```sh
    git clone https://github.com/Evgeniy20181/FlappyBirdsPy.git
    cd https://github.com/Evgeniy20181/FlappyBirdsPy.git
    ```

2. **Create a virtual environment:**
    ```sh
    python -m venv venv
    ```

3. **Activate the virtual environment:**
    - On Windows:
        ```sh
        venv\Scripts\activate
        ```
    - On macOS and Linux:
        ```sh
        source venv/bin/activate
        ```

4. **Install the required packages:**
    ```sh
    pip install pygame -y
    ```

5. **Run the game:**
    ```sh
    python main.py
    ```

## How to Play

1. **Start the game:**
   - Run the `flappy_bird.py` script to start the game.
   - You will see the main menu screen.

2. **Controls:**
   - Press the `SPACE` bar to start the game and make the bird flap its wings.
   - The bird will move upward when you press the space bar and fall due to gravity when you release it.

3. **Objective:**
   - Guide the bird through the gaps between the pipes.
   - Avoid hitting the pipes, ground, or sky.
   - The game ends if the bird collides with any obstacles.
   - Try to achieve the highest score possible.

## Code Overview

### Main Components

- **`flappy_bird.py`**: The main script that runs the game.
- **`Bird` class**: Manages bird behavior, including flapping, movement, and animation.
- **`Pipes` class**: Handles pipe generation, movement, and collision detection.
- **`Game` class**: Manages the overall game state, including the main menu, game loop, score tracking, and rendering.

### Key Methods

- **Bird Class:**
  - `update()`: Updates the bird's position and applies gravity.
  - `flap()`: Makes the bird flap its wings.
  - `rotate()`: Rotates the bird image based on its movement.
  - `animate()`: Cycles through bird images for animation.
  - `reset()`: Resets the bird's position and movement.
  - `draw(screen)`: Draws the bird on the screen.

- **Pipes Class:**
  - `create_pipes()`: Creates a pair of pipes at random height.
  - `update(bird_rect)`: Moves pipes and checks for collisions with the bird.
  - `draw(screen)`: Draws pipes on the screen.
  - `add_pipe()`: Adds a new pair of pipes to the list.

- **Game Class:**
  - `draw_floor()`: Draws the moving floor.
  - `draw_score(game_state)`: Draws the score on the screen.
  - `score_update()`: Updates the score when the bird passes through pipes.
  - `draw_menu()`: Draws the main menu screen.
  - `run()`: The main game loop.

## Contributing

Contributions are welcome! If you have any ideas, suggestions, or bug reports, please create an issue or submit a pull request.

1. **Fork the repository**
2. **Create a new branch** (`git checkout -b feature-branch`)
3. **Commit your changes** (`git commit -am 'Add new feature'`)
4. **Push to the branch** (`git push origin feature-branch`)
5. **Create a new Pull Request**

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
