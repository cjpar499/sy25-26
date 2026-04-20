import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Player properties
player_pos = [WIDTH // 2, HEIGHT - 50]
player_size = 50

# Enemy properties
enemy_size = 50
enemy_pos = [random.randint(0, WIDTH - enemy_size), 0]
enemy_speed = 10

score = 0
game_over = False

# Trail properties
trail = []
trail_length = 10

# Player speed
player_speed = 5

# Load and scale images
player_image = pygame.image.load("download (2).jpg").convert()
player_image = pygame.transform.scale(player_image, (player_size, player_size))
enemy_image = pygame.image.load("download (3).jpg").convert()
enemy_image = pygame.transform.scale(enemy_image, (enemy_size, enemy_size))

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    # --- BUG 1: Movement Logic ---
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_pos[0] -= player_speed  # Should move left
    if keys[pygame.K_RIGHT]:
        player_pos[0] += player_speed  # Should move right

    # Update enemy position
    enemy_pos[1] += enemy_speed

    # --- BUG 2: Resetting the Enemy ---
    if enemy_pos[1] > HEIGHT:
        enemy_pos[1] = 0
        enemy_pos[0] = random.randint(0, WIDTH - enemy_size)
        score += 1
        enemy_speed += 1
        player_speed += 1
        print(f"Score: {score}")

    # --- BUG 3: Collision Detection ---
    if (enemy_pos[0] < player_pos[0] + player_size and
        enemy_pos[0] + enemy_size > player_pos[0] and
        enemy_pos[1] < player_pos[1] + player_size and
        enemy_pos[1] + enemy_size > player_pos[1]):
        print("Game Over!")
        game_over = True

    # Add the current player position to the trail
    trail.append(player_pos[:])  # Append a copy of the current position
    if len(trail) > trail_length:
        trail.pop(0)  # Remove the oldest position if the trail is too long

    # Drawing
    screen.fill((0, 0, 0))

    # Draw the enemy
    screen.blit(enemy_image, (enemy_pos[0], enemy_pos[1]))

    # Draw the trail
    for i, pos in enumerate(trail):
        # Create a semi-transparent version of the player image
        ghost_image = player_image.copy()
        ghost_image.set_alpha(255 - (i * (255 // trail_length)))  # Fade effect
        screen.blit(ghost_image, (pos[0], pos[1]))

    # Draw the player
    screen.blit(player_image, (player_pos[0], player_pos[1]))

    pygame.display.update()
    clock.tick(30)

pygame.quit()

