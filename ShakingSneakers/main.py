import pygame
import random
import time

pygame.init()

# Resources
icon = pygame.image.load("source/images/game-icon.png")
sneaker = pygame.image.load("source/images/sneaker-1.png")
coin = pygame.image.load("source/images/coin.png")
font = pygame.font.Font("source/fonts/Teko-Regular.ttf", 40)

# Settings
pygame.display.set_caption("SimulatorShakingSneakers")
pygame.display.set_icon(icon)
screen = pygame.display.set_mode((400, 400))

# Other
background_colors = [
    (91, 209, 171),
    (91, 149, 227),
    (235, 235, 87),
    (93, 235, 87),
    (204, 114, 237),
    (240, 89, 149)
]

background_color = random.choice(background_colors)
coins = 0


running = True
while running:
    coins_text = font.render(str(coins), False, "white")
    screen.fill(background_color)
    screen.blit(coin, (5, 5))
    screen.blit(coins_text, (85, 10))
    screen.blit(sneaker, (15, 50))
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                coins += 1
                background_color = random.choice(background_colors)
