''' Gun game '''
import pygame
from pygame.locals import *
import random

# Initialize Pygame
pygame.init()

# Set screen size
screen = pygame.display.set_mode((800, 600))

# Set screen title
pygame.display.set_caption("Gun Shooter Game")

# Set game variables
player_pos = [400, 300]
player_speed = 5
bullets = []
enemies = []
enemy_speed = 3
score = 0
power_ups = []

# Set game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                bullets.append([player_pos[0], player_pos[1]])

    # Handle player movement
    keys = pygame.key.get_pressed()
    if keys[K_LEFT]:
        player_pos[0] -= player_speed
    if keys[K_RIGHT]:
        player_pos[0] += player_speed
    if keys[K_UP]:
        player_pos[1] -= player_speed
    if keys[K_DOWN]:
        player_pos[1] += player_speed

    # Update bullets
    for bullet in bullets:
        bullet[1] -= 10

    # Update enemies
    if random.random() < 0.01:
        enemies.append([random.randint(0, 800), 0])
    for enemy in enemies:
        enemy[1] += enemy_speed

    # Check for collisions
    for bullet in bullets:
        for enemy in enemies:
            if bullet[0] > enemy[0] and bullet[0] < enemy[0] + 20 and bullet[1] > enemy[1] and bullet[1] < enemy[1] + 20:
                score += 1
                bullets.remove(bullet)
                enemies.remove(enemy)

    # Update power-ups
    if random.random() < 0.005:
        power_ups.append([random.randint(0, 800), 0, random.choice(["score", "speed"])])
    for power_up in power_ups:
        power_up[1] += enemy_speed

    # Check for power-up collisions
    for power_up in power_ups:
        if player_pos[0] > power_up[0] and player_pos[0] < power_up[0] + 20 and player_pos[1] > power_up[1] and player_pos[1] < power_up[1] + 20:
            if power_up[2] == "score":
                score += 10
            elif power_up[2] == "speed":
                player_speed += 1
            power_ups.remove(power_up)

    # Draw screen
    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, (255, 255, 255), player_pos, 20)
    for bullet in bullets:
        pygame.draw.circle(screen, (255, 255, 255), bullet, 5)
    for enemy in enemies:
        pygame.draw.rect(screen, (255, 0, 0), (enemy[0], enemy[1], 20, 20))
    for power_up in power_ups:
        if power_up[2] == "score":
            color = (0, 255, 0)
        elif power_up[2] == "speed":
            color = (255, 255, 0)
        pygame.draw.rect(screen, color, (power_up[0], power_up[1], 20, 20))
    font = pygame.font.Font(None, 36)
    text = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(text, (650, 550))
    pygame.display.update()