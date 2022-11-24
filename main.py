import pygame
import random
import keyboard
import pyautogui
import time

pygame.init()

screen = pygame.display.set_mode([pygame.display.Info().current_w, pygame.display.Info().current_h], pygame.FULLSCREEN)
isRunning = True
clock = pygame.time.Clock()
my_font = pygame.font.SysFont("Comic Sans MS", 40)
restart_font = pygame.font.SysFont("Comic Sans MS", 80)

player2X = pygame.display.Info().current_w - 150
player2Y = pygame.display.Info().current_h - 150
player2Height = 50
player2Width = 50
player2Velocity = 8
player2Direction = False

dogX = 20
dogY = 20

timing = 0

start_text = my_font.render("First one to get 10 score wins!", False, (0, 0, 255))
screen.blit(start_text, (pygame.display.Info().current_w / 2 - 250, pygame.display.Info().current_h / 2))
pygame.display.update()
time.sleep(1.3)

screen.fill((0, 0, 0))
start_text = my_font.render("Press 'ctrl+q' to end the game early!", False, (0, 0, 255))
screen.blit(start_text, (pygame.display.Info().current_w / 3 + 40, pygame.display.Info().current_h / 2))
pygame.display.update()
time.sleep(1.3)

screen.fill((0, 0, 0))
start_text = my_font.render("Press 'i' to restart the game!", False, (0, 0, 255))
screen.blit(start_text, (pygame.display.Info().current_w / 3 + 80, pygame.display.Info().current_h / 2))
pygame.display.update()
time.sleep(1.3)

foodX = random.randint(10, pygame.display.Info().current_w - 20)
foodY = random.randint(10, pygame.display.Info().current_h - 20)

y = 100
x = 60
playerWidth = 50
playerHeight = 50
playerVelocity = 8
playerDirection = False

ammoX = x
ammoY = y
ammo2X = player2X
ammo2Y = player2Y

imgObject = pygame.image.load("dog.jpg")
imgObject = pygame.transform.scale(imgObject, (100, 100))
mainCharacter = pygame.image.load("pixelart.png")
mainCharacter = pygame.transform.scale(mainCharacter, (60, 60))

s = pygame.Surface((1000, 750))  # the size of your rect
s.set_alpha(128)  # alpha level
s.fill((255, 255, 255))  # this fills the entire surface
screen.blit(s, (0, 0))  # (0,0) are the top-left coordinates

while isRunning:
    timing += 1
    clock.tick(60)
    # screen.blit(s, (0, 0))  # (0,0) are the top-left coordinates
    pygame.display.set_caption(f'{clock.get_fps() :.1f} FPS ')
    ammo = pygame.draw.rect(screen, (40, 0, 0), (ammoX, ammoY, 400, 200))
    ammo2 = pygame.draw.rect(screen, (0, 0, 40), (ammo2X - 300, ammo2Y - 100, 400, 200))
    cursorImg = pygame.draw.circle(screen, (255, 0, 0), [pyautogui.position().x, pyautogui.position().y], playerWidth)
    food = pygame.draw.rect(screen, (255, 255, 255), (foodX, foodY, 20, 20))

    # Score label
    player1_score = my_font.render(f'Player1: {playerWidth - 50}', False, (255, 0, 255))
    player2_score = my_font.render(f'Player2: {player2Width - 50}', False, (0, 0, 255))
    screen.blit(player1_score, (25, 25))
    screen.blit(player2_score, (pygame.display.Info().current_w - 240, 25))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False

    keys = pygame.key.get_pressed()

    # convert alpha to draw only the object without transparent background -> collision
    playerRect = pygame.draw.rect(screen, (255, 0, 255), (x, y, playerWidth, playerHeight))
    player2Rect = pygame.draw.rect(screen, (0, 50, 50), (player2X, player2Y, player2Width, player2Height))
    player2Img = pygame.image.load("player1Right.png").convert_alpha()
    player2Img = pygame.transform.flip(player2Img, player2Direction, False)
    player2Img = pygame.transform.scale(player2Img, (3 * player2Width, 3 * player2Height))
    # pes = screen.blit(imgObject, (pyautogui.position().x, pyautogui.position().y))
    # screen.blit(player2Img, (player2X - player2Rect.width, player2Y - player2Rect.height))
    screen.blit(imgObject, (dogX, dogY))
    screen.blit(mainCharacter, (x, y))

    # if clock.get_time() % 2 == 0:
    #  timing += 1

    # print(timing)
    if 0 <= timing <= 10:
        playerRect = pygame.draw.rect(screen, (0, 0, 255), (x, y, playerWidth, playerHeight))
        food = pygame.draw.rect(screen, (100, 100, 100), (foodX, foodY, 20, 20))
        player2Img = pygame.image.load("player1Right.png").convert_alpha()
        player2Img = pygame.transform.flip(player2Img, player2Direction, False)
        player2Img = pygame.transform.scale(player2Img, (3 * player2Width, 3 * player2Height))
    elif 10 <= timing <= 20:
        playerRect = pygame.draw.rect(screen, (255, 0, 0), (x, y, playerWidth, playerHeight))
        food = pygame.draw.rect(screen, (10, 255, 50), (foodX, foodY, 20, 20))
        player2Img = pygame.image.load("player1Left.png").convert_alpha()
        player2Img = pygame.transform.flip(player2Img, player2Direction, False)
        player2Img = pygame.transform.scale(player2Img, (3 * player2Width, 3 * player2Height))
    elif 20 <= timing <= 30:
        playerRect = pygame.draw.rect(screen, (0, 255, 255), (x, y, playerWidth, playerHeight))
        food = pygame.draw.rect(screen, (30, 55, 150), (foodX, foodY, 20, 20))
        player2Img = pygame.image.load("player1Left.png").convert_alpha()
        player2Img = pygame.transform.flip(player2Img, player2Direction, False)
        player2Img = pygame.transform.scale(player2Img, (3 * player2Width, 3 * player2Height))
    elif 30 <= timing <= 40:
        playerRect = pygame.draw.rect(screen, (0, 0, 50), (x, y, playerWidth, playerHeight))
        food = pygame.draw.rect(screen, (0, 30, 90), (foodX, foodY, 20, 20))
        player2Img = pygame.image.load("player1Right.png").convert_alpha()
        player2Img = pygame.transform.flip(player2Img, player2Direction, False)
        player2Img = pygame.transform.scale(player2Img, (3 * player2Width, 3 * player2Height))
    elif timing >= 40:
        timing = 0
    screen.blit(player2Img, (player2X - player2Rect.width, player2Y - player2Rect.height))

    if keys[pygame.K_w] and y > 0:
        y -= playerVelocity
        # pygame.transform.rotate(rect, 60)
    if keys[pygame.K_s] and y < pygame.display.Info().current_h - playerRect.height:
        y += playerVelocity
    if keys[pygame.K_a] and x > 0:
        x -= playerVelocity
    if keys[pygame.K_d] and x < pygame.display.Info().current_w - playerRect.width:
        x += playerVelocity
    if keys[pygame.K_ESCAPE]:
        isRunning = False
        # Restarting game
    if keys[pygame.K_i]:
        screen.fill((0, 50, 50))
        end_text = restart_font.render(f'Restarting the game!', False, (0, 0, 0))
        screen.blit(end_text, (pygame.display.Info().current_w / 2 - 350, pygame.display.Info().current_h / 2))
        pygame.display.update()
        time.sleep(1)
        playerWidth = 50
        playerHeight = 50
        y = 100
        x = 60
        playerRect = pygame.draw.rect(screen, (255, 0, 255), (x, y, playerWidth, playerHeight))

        player2Width = 50
        player2Height = 50
        player2X = pygame.display.Info().current_w - 150
        player2Y = pygame.display.Info().current_h - 150

        foodX = random.randint(10, pygame.display.Info().current_w - food.width)
        foodY = random.randint(10, pygame.display.Info().current_h - food.height)
    if keys[pygame.K_e]:
        ammoX = x
        ammoY = y
    if keys[pygame.K_1]:
        ammo2X = player2X
        ammo2Y = player2Y

    if keys[pygame.K_UP] and player2Y > 0:
        player2Y -= player2Velocity
    if keys[pygame.K_DOWN] and player2Y < pygame.display.Info().current_h - player2Rect.height:
        player2Y += player2Velocity
    if keys[pygame.K_LEFT] and player2X > 0:
        player2X -= player2Velocity
        player2Direction = True
    if keys[pygame.K_RIGHT] and player2X < pygame.display.Info().current_w - player2Rect.width:
        player2X += player2Velocity
        player2Direction = False

    pygame.mouse.set_visible(False)

    if playerRect.colliderect(ammo2):
        playerVelocity = 4
    elif playerRect.colliderect(ammo):
        playerVelocity = 15
    else:
        playerVelocity = 8

    if player2Rect.colliderect(ammo):
        player2Rect = pygame.draw.rect(screen, (40, 0, 0), (player2X, player2Y, player2Width, player2Height))
        screen.blit(player2Img, (player2X - player2Rect.width, player2Y - player2Rect.height))
        player2Velocity = 4
    elif player2Rect.colliderect(ammo2):
        player2Rect = pygame.draw.rect(screen, (0, 0, 40), (player2X, player2Y, player2Width, player2Height))
        screen.blit(player2Img, (player2X - player2Rect.width, player2Y - player2Rect.height))
        player2Velocity = 15
    else:
        player2Velocity = 8

    if playerRect.colliderect(food):
        playerWidth += 1
        playerHeight += 1
        print(playerWidth)
        foodX = random.randint(10, pygame.display.Info().current_w - food.width)
        foodY = random.randint(10, pygame.display.Info().current_h - food.height)
        food = pygame.draw.rect(screen, (255, 0, 255), (foodX, foodY, 10, 10))

    if player2Rect.colliderect(food):
        player2Width += 1
        player2Height += 1
        print(player2Width)
        foodX = random.randint(10, pygame.display.Info().current_w - food.width)
        foodY = random.randint(10, pygame.display.Info().current_h - food.height)
        food = pygame.draw.rect(screen, (255, 0, 255), (foodX, foodY, 10, 10))

        if playerRect.colliderect(ammo2):
            playerVelocity = 0

    # playerRect
    # player2Img
    # ammo
    # ammo2

    pygame.display.update()
    screen.fill((0, 50, 50))

    dogX = random.randint(10, pygame.display.Info().current_w)
    dogY = random.randint(10, pygame.display.Info().current_h)

    if playerWidth >= 60 or player2Width >= 60 or keyboard.is_pressed("ctrl+q"):
        if playerWidth >= 60 or playerWidth > player2Width:
            end_text = my_font.render(f'Player1 wins with {playerWidth - 50} score', False, (255, 0, 255))
            screen.blit(end_text, (pygame.display.Info().current_w / 2 - 250, pygame.display.Info().current_h / 2))
        else:
            if playerWidth == player2Width:
                end_text = my_font.render(f'Tie!', False, (255, 0, 255))
                screen.blit(end_text, (pygame.display.Info().current_w / 2, pygame.display.Info().current_h / 2))
            else:
                end_text = my_font.render(f'Player2 wins with {player2Width - 50} score', False, (0, 0, 255))
                screen.blit(end_text, (pygame.display.Info().current_w / 2 - 250, pygame.display.Info().current_h / 2))
        # screen.blit(end_text, (pygame.display.Info().current_w / 2 - 250, pygame.display.Info().current_h / 2))
        pygame.display.update()
        time.sleep(2)
        isRunning = False
        pygame.quit()

pygame.quit()
