import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
ELECTRON_RADIUS = 5
BACKGROUND_COLOR = (0, 0, 0)
CHARGE = 500  # Repulsion strength
FPS = 60

# Create screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Electron Simulator")
font = pygame.font.Font(None, 36)


# Function to get user input inside the game
def get_user_input():
    input_box = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 - 20, 200, 40)
    color_active = pygame.Color('dodgerblue2')
    color_inactive = pygame.Color('lightskyblue3')
    color = color_inactive
    active = False
    text = ''
    done = False

    while not done:
        screen.fill(BACKGROUND_COLOR)
        txt_surface = font.render("Enter number of electrons:", True, pygame.Color('white'))
        screen.blit(txt_surface, (WIDTH // 2 - 130, HEIGHT // 2 - 60))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        return int(text) if text.isdigit() and int(text) > 0 else 10
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    elif event.unicode.isdigit():  # Only allow numbers
                        text += event.unicode

        pygame.draw.rect(screen, color, input_box, 2)
        txt_surface = font.render(text, True, pygame.Color('white'))
        screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
        pygame.display.flip()



# Get user input for number of electrons
NUM_ELECTRONS = get_user_input()


# Generate random colors for electrons
def random_color():
    return (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))


class Electron:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.vx = random.uniform(-2, 2)
        self.vy = random.uniform(-2, 2)
        self.color = color
        self.path = []

    def update(self, electrons):
        ax, ay = 0, 0

        for other in electrons:
            if other == self:
                continue
            dx = other.x - self.x
            dy = other.y - self.y
            dist = math.sqrt(dx ** 2 + dy ** 2)
            if dist < 2 * ELECTRON_RADIUS:
                dist = 2 * ELECTRON_RADIUS  # Prevent division by zero
            force = CHARGE / dist ** 2
            ax -= force * (dx / dist)
            ay -= force * (dy / dist)

        self.vx += ax
        self.vy += ay
        self.vx *= 0.99  # Damping effect
        self.vy *= 0.99

        self.x += self.vx
        self.y += self.vy

        # Bounce off walls
        if self.x - ELECTRON_RADIUS < 0 or self.x + ELECTRON_RADIUS > WIDTH:
            self.vx *= -1
        if self.y - ELECTRON_RADIUS < 0 or self.y + ELECTRON_RADIUS > HEIGHT:
            self.vy *= -1

        self.x = max(ELECTRON_RADIUS, min(WIDTH - ELECTRON_RADIUS, self.x))
        self.y = max(ELECTRON_RADIUS, min(HEIGHT - ELECTRON_RADIUS, self.y))

        # Store path for visualization
        self.path.append((self.x, self.y))
        if len(self.path) > 50:
            self.path.pop(0)

    def draw(self, screen):
        for i in range(1, len(self.path)):
            pygame.draw.line(screen, self.color, self.path[i - 1], self.path[i], 1)
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), ELECTRON_RADIUS)


# Create electrons, all starting from the center
electrons = [Electron(WIDTH // 2, HEIGHT // 2, random_color()) for _ in range(NUM_ELECTRONS)]

running = True
clock = pygame.time.Clock()
while running:
    screen.fill(BACKGROUND_COLOR)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for electron in electrons:
        electron.update(electrons)
        electron.draw(screen)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
