# Electron Simulator

A simple electron simulation using Pygame where electrons repel each other due to Coulomb-like forces. The simulation allows users to input the number of electrons before starting.

## Features
- **Interactive Input**: Users can enter the number of electrons at the start.
- **Physics-Based Movement**: Electrons repel each other, creating dynamic motion.
- **Trail Visualization**: Each electron leaves a short trail to visualize motion.
- **Wall Collision**: Electrons bounce off the edges of the screen.
- **Random Colors**: Each electron is assigned a random color.

## Installation
Ensure you have Python installed, then install Pygame:
```sh
pip install pygame
```

## Usage
Run the script using:
```sh
python electron_simulator.py
```
When prompted, enter the number of electrons to simulate.

## Controls
- **Close the Window**: Click the close button to exit the simulation.

## Code Overview
- `get_user_input()`: Handles user input to determine the number of electrons.
- `Electron` class: Defines electron properties, motion, and rendering.
- `update()`: Calculates repulsion forces and updates motion.
- `draw()`: Draws the electron and its trail.
- Main loop: Updates and renders the simulation at 60 FPS.

## Dependencies
- Python 3.x
- Pygame



