# ⚛️ Electron Simulator

[![Python 3.6+](https://img.shields.io/badge/python-3.13+-blue.svg)](https://www.python.org/downloads/)
[![Pygame](https://img.shields.io/badge/pygame-2.0.1+-green.svg)](https://www.pygame.org/)
[![MIT License](https://img.shields.io/badge/license-MIT-yellow.svg)](LICENSE)

A high-performance physics-based particle simulation demonstrating electron repulsion behaviors visualized with Pygame.

![Electron Simulator Demo](sim.gif)

## 🔭 Overview

Electron Simulator is an interactive visualization that models the repulsive forces between electrons. The simulation starts with a single particle at the center of the screen and gradually increases the number of particles over time, allowing you to observe how complex emergent behaviors develop from simple physics rules.

## ✨ Features

- **Physics-based Simulation**: Accurately models electron repulsion forces using Coulomb's law
- **Visual Trails**: Each electron leaves a colored trail showing its recent path
- **Auto-scaling Complexity**: The simulation gradually adds more electrons (up to 200) every 10 seconds
- **Boundary Collision**: Electrons bounce realistically off the edges of the screen
- **Colored Particles**: Each electron has a unique randomly-generated color for easier tracking
- **Performance Optimized**: Designed for smooth animation even with hundreds of particles

## 🛠️ Installation

### Prerequisites
- Python 3.6+
- Pygame library

### Setup
1. Clone this repository:
```bash
git clone https://github.com/yourusername/electron-simulator.git
cd electron-simulator
```

2. Install dependencies:
```bash
pip install pygame
```

## 🚀 Usage

Run the simulation with:
```bash
python app.py
```

The simulation will automatically:
- Start with 1 electron in the center
- Add 10 new electrons every 10 seconds (up to a maximum of 200)
- Display the current electron count in the top-left corner

## 🎮 Controls

- Close the window to exit the simulation

## 📐 Mathematical Model

The simulation is based on Coulomb's law of electrostatic force between charged particles:

### Coulomb's Law

The electrostatic force between two point charges is directly proportional to the product of the magnitude of the charges and inversely proportional to the square of the distance between them:

$$F = k \frac{q_1 q_2}{r^2}$$

Where:
- $F$ is the electrostatic force
- $k$ is Coulomb's constant
- $q_1$ and $q_2$ are the magnitudes of the charges
- $r$ is the distance between the charges

## 💻 Technical Implementation

For each electron in our simulation:

1. **Force Calculation**: For each pair of electrons, the repulsive force is calculated as:
   ```python
   force = CHARGE / distance² 
   ```
   where `CHARGE` is a constant (set to 500)

2. **Acceleration**: Force is converted to acceleration (assuming unit mass):
   ```python
   ax = -force * (dx / distance)
   ay = -force * (dy / distance)
   ```
   The negative sign implements repulsion rather than attraction.

3. **Velocity Update**: Each frame, velocity is updated by the acceleration:
   ```python
   vx += ax
   vy += ay
   ```

4. **Damping**: A damping factor is applied to stabilize the system:
   ```python
   vx *= 0.99
   vy *= 0.99
   ```

5. **Position Update**: Position is updated based on velocity:
   ```python
   x += vx
   y += vy
   ```

6. **Boundary Collisions**: Velocities are inverted when electrons hit the edges:
   ```python
   if x - RADIUS < 0 or x + RADIUS > WIDTH:
       vx *= -1
   if y - RADIUS < 0 or y + RADIUS > HEIGHT:
       vy *= -1
   ```

This implementation creates a simplified but physically plausible model of electron behavior in a confined space.

## 🔍 Observed Behaviors

As the simulation progresses, you may observe:

- **Equilibrium Positioning**: Electrons naturally distribute themselves to minimize potential energy
- **Edge Clustering**: Many electrons tend to get pushed toward the boundaries
- **Dynamic Stability**: The system continuously shifts but maintains certain geometric patterns
- **Path Complexity**: As more electrons are added, individual paths become more chaotic

## ⚙️ Customization

You can modify these constants in the code to change the simulation behavior:

| Parameter | Description | Default Value |
|-----------|-------------|---------------|
| `WIDTH, HEIGHT` | Screen dimensions | 800, 600 |
| `ELECTRON_RADIUS` | Size of the particles | 5 |
| `CHARGE` | Strength of repulsion forces | 500 |
| `START_ELECTRONS` | Initial number of electrons | 1 |
| `MAX_ELECTRONS` | Maximum number of electrons | 200 |
| `INCREMENT` | Number of electrons added each interval | 10 |

## 📄 License

[LICENSE]

## 👏 Acknowledgments

- Inspired by physics simulations and particle systems
- Built with [Pygame](https://www.pygame.org/)
