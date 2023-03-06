import pygame
import random
import keyboard
import pyautogui
import time
from settings import Settings
from entity.Entity import Entity
import Game

pygame.init()

screen = pygame.display.set_mode([pygame.display.Info().current_w, pygame.display.Info().current_h], pygame.FULLSCREEN)
clock = pygame.time.Clock()
my_font = pygame.font.SysFont("Comic Sans MS", 40)
restart_font = pygame.font.SysFont("Comic Sans MS", 80)

player1 = Entity(50, 50, 60, 100, 0, "player1Left.png", False, 8)
player2 = Entity(50, 50, Settings.SCREEN_WIDTH - 150, Settings.SCREEN_HEIGHT - 150, 0,
                 "player1Left.png", False, 8)

boost = 100.0

# player2X = pygame.display.Info().current_w - 150
# player2Y = pygame.display.Info().current_h - 150
# player2Height = 50
# player2Width = 50
# player2Velocity = 8
# player2Velocity = 8
# player2Direction = False
# player2Direction = False

dogX = 20
dogY = 20

timing = 0

start_text = my_font.render("First one to get 10 score wins!", False, (0, 0, 255))
screen.blit(start_text,
            (pygame.display.Info().current_w // 2 - start_text.get_width() // 2, pygame.display.Info().current_h // 2))
pygame.display.update()
time.sleep(Settings.seconds)

screen.fill(Settings.BLACK)
start_text = my_font.render("Press 'ctrl+q' to end the game early!", False, (0, 0, 255))
screen.blit(start_text,
            (pygame.display.Info().current_w // 2 - start_text.get_width() // 2,
             pygame.display.Info().current_h // 2 - start_text.get_height()))
pygame.display.update()
time.sleep(Settings.seconds)

screen.fill(Settings.BLACK)
start_text = my_font.render("Press 'i' to restart the game!", False, (0, 0, 255))
screen.blit(start_text,
            (pygame.display.Info().current_w // 2 - start_text.get_width() // 2,
             pygame.display.Info().current_h // 2 - start_text.get_height() // 2))
pygame.display.update()
time.sleep(Settings.seconds)

foodX = random.randint(10, pygame.display.Info().current_w - 20)
foodY = random.randint(10, pygame.display.Info().current_h - 20)

# y = 100
# x = 60
# playerWidth = 50
# playerHeight = 50
# playerVelocity = 8
# playerDirection = False

ammoX = player1.x
ammoY = player1.y
ammo2X = player2.x
ammo2Y = player2.y

imgObject = pygame.image.load("dog.jpg")
imgObject = pygame.transform.scale(imgObject, (100, 100))
mainCharacter = pygame.image.load("pixelart.png")
mainCharacter = pygame.transform.scale(mainCharacter, (60, 60))

s = pygame.Surface((1000, 750))  # the size of your rect
s.set_alpha(128)  # alpha level
s.fill((255, 255, 255))  # this fills the entire surface
screen.blit(s, (0, 0))  # (0,0) are the top-left coordinates

# def gameLoop():
while Settings.isRunning:
    timing += 1
    if boost < 100:
        boost += 0.1
    clock.tick(60)
    # screen.blit(s, (0, 0))  # (0,0) are the top-left coordinates
    # screen.blit(s, (0, 0))  # (0,0) are the top-left coordinates
    pygame.display.set_caption(f'{clock.get_fps() :.1f} FPS ')
    ammo = pygame.draw.rect(screen, (40, 0, 0), (ammoX, ammoY, 20, 20))
    ammo2 = pygame.draw.rect(screen, (0, 0, 40), (ammo2X - 300, ammo2Y - 150, 20, 20))
    cursorImg = pygame.draw.circle(screen, (255, 0, 0), [pyautogui.position().x, pyautogui.position().y],
                                   player1.width)
    food = pygame.draw.rect(screen, (255, 255, 255), (foodX, foodY, 20, 20))

    # Score label
    fps_text = my_font.render(f'{clock.get_fps() : .1f} FPS', False, (0, 0, 0))
    player1_score = my_font.render(f'Player1: {player1.width - 50}', False, (255, 0, 255))
    player2_score = my_font.render(f'Player2: {player2.width - 50}', False, (0, 0, 255))
    player1_boost = my_font.render(f'Boost: {round(boost, 2)}', False, (255, 0, 255))
    screen.blit(player1_boost, (20, pygame.display.Info().current_h / 2))
    screen.blit(player1_score, (25, 30))
    screen.blit(player2_score, (pygame.display.Info().current_w - player2_score.get_width() - 25, 30))
    screen.blit(fps_text, (pygame.display.Info().current_w // 2 - fps_text.get_width() // 2, 10))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Settings.isRunning = False

    keys = pygame.key.get_pressed()

    # convert alpha to draw only the object without transparent background -> collision
    playerRect = pygame.draw.rect(screen, (255, 0, 255), (player1.x, player1.y, player1.width, player1.height))
    player2Rect = pygame.draw.rect(screen, (136, 89, 47), (player2.x, player2.y, player2.width, player2.height))
    player2Img = pygame.image.load(player2.image).convert_alpha()
    player2Img = pygame.transform.flip(player2Img, player2.direction, False)
    player2Img = pygame.transform.scale(player2Img,
                                        (Settings.SCALE * player2.width, Settings.SCALE * player2.height))
    # pes = screen.blit(imgObject, (pyautogui.position().x, pyautogui.position().y))
    # screen.blit(player2Img, (player2X - player2Rect.width, player2Y - player2Rect.height))
    screen.blit(imgObject, (dogX, dogY))
    screen.blit(mainCharacter, (player1.x, player1.y))

    # if clock.get_time() % 2 == 0:
    #  timing += 1

    # print(timing)
    if 0 <= timing <= 10:
        playerRect = pygame.draw.rect(screen, (0, 0, 255), (player1.x, player1.y, player1.width, player1.height))
        food = pygame.draw.rect(screen, (100, 100, 100), (foodX, foodY, 20, 20))
        player2Img = pygame.image.load("player1Right.png").convert_alpha()
        player2Img = pygame.transform.flip(player2Img, player2.direction, False)
        player2Img = pygame.transform.scale(player2Img,
                                            (Settings.SCALE * player2.width, Settings.SCALE * player2.height))
    elif 10 <= timing <= 20:
        playerRect = pygame.draw.rect(screen, (255, 0, 0), (player1.x, player1.y, player1.width, player1.height))
        food = pygame.draw.rect(screen, (10, 255, 50), (foodX, foodY, 20, 20))
        player2Img = pygame.image.load("player1Left.png").convert_alpha()
        player2Img = pygame.transform.flip(player2Img, player2.direction, False)
        player2Img = pygame.transform.scale(player2Img,
                                            (Settings.SCALE * player2.width, Settings.SCALE * player2.height))
    elif 20 <= timing <= 30:
        playerRect = pygame.draw.rect(screen, (0, 255, 255), (player1.x, player1.y, player1.width, player1.height))
        food = pygame.draw.rect(screen, (30, 55, 150), (foodX, foodY, 20, 20))
        player2Img = pygame.image.load("player1Left.png").convert_alpha()
        player2Img = pygame.transform.flip(player2Img, player2.direction, False)
        player2Img = pygame.transform.scale(player2Img,
                                            (Settings.SCALE * player2.width, Settings.SCALE * player2.height))
    elif 30 <= timing <= 40:
        playerRect = pygame.draw.rect(screen, (0, 0, 50), (player1.x, player1.y, player1.width, player1.height))
        food = pygame.draw.rect(screen, (0, 30, 90), (foodX, foodY, 20, 20))
        player2Img = pygame.image.load("player1Right.png").convert_alpha()
        player2Img = pygame.transform.flip(player2Img, player2.direction, False)
        player2Img = pygame.transform.scale(player2Img,
                                            (Settings.SCALE * player2.width, Settings.SCALE * player2.height))
    elif timing >= 40:
        timing = 0
    screen.blit(player2Img, (player2.x - player2Rect.width, player2.y - player2Rect.height))

    if keys[pygame.K_w] and player1.y > 0:
        player1.y -= player1.velocity
        # pygame.transform.rotate(rect, 60)
    if keys[pygame.K_s] and player1.y < pygame.display.Info().current_h - playerRect.height:
        player1.y += player1.velocity
    if keys[pygame.K_a] and player1.x > 0:
        player1.x -= player1.velocity
    if keys[pygame.K_d] and player1.x < pygame.display.Info().current_w - playerRect.width:
        player1.x += player1.velocity
    if keys[pygame.K_ESCAPE]:
        Settings.isRunning = False

        # Restarting game
    if keys[pygame.K_i]:
        screen.fill((136, 89, 47))
        end_text = restart_font.render(f'Restarting the game!', False, (0, 0, 0))
        screen.blit(end_text, (pygame.display.Info().current_w // 2 - 350, pygame.display.Info().current_h // 2))
        pygame.display.update()
        time.sleep(1)
        player1.width = 50
        player1.height = 50
        player1.y = 100
        player1.x = 60
        playerRect = pygame.draw.rect(screen, (255, 0, 255), (player1.x, player1.y, player1.width, player1.height))

        player2.width = 50
        player2.height = 50
        player2.x = pygame.display.Info().current_w - 150
        player2.y = pygame.display.Info().current_h - 150

        foodX = random.randint(10, pygame.display.Info().current_w - food.width)
        foodY = random.randint(10, pygame.display.Info().current_h - food.height)

    if keys[pygame.K_LSHIFT]:
        if boost >= 1:
            # player1.velocity = 15
            ammoX = player1.x
            ammoY = player1.y
        if boost > 0:
            boost -= 1
    if keys[pygame.K_1]:
        ammo2X = player2.x
        ammo2Y = player2.y

    if keys[pygame.K_UP] and player2.y > 0:
        player2.y -= player2.velocity
    if keys[pygame.K_DOWN] and player2.y < pygame.display.Info().current_h - player2Rect.height:
        player2.y += player2.velocity
    if keys[pygame.K_LEFT] and player2.x > 0:
        player2.x -= player2.velocity
        player2.direction = True
    if keys[pygame.K_RIGHT] and player2.x < pygame.display.Info().current_w - player2Rect.width:
        player2.x += player2.velocity
        player2.direction = False

    pygame.mouse.set_visible(False)

    if playerRect.colliderect(ammo2):
        player1.velocity = 4
    elif playerRect.colliderect(ammo):
        player1.velocity = 15
    else:
        player1.velocity = 8

    if player2Rect.colliderect(ammo):
        player2Rect = pygame.draw.rect(screen, (40, 0, 0), (player2.x, player2.y, player2.width, player2.height))
        screen.blit(player2Img, (player2.x - player2Rect.width, player2.y - player2Rect.height))
        player2.velocity = 4
    elif player2Rect.colliderect(ammo2):
        # player2Rect = pygame.draw.rect(screen, (0, 0, 40), (player2.x, player2.y, player2.width, player2.height))
        # screen.blit(player2Img, (player2.x - player2Rect.width, player2.y - player2Rect.height))
        player2.velocity = 15
    else:
        player2.velocity = 8

    if playerRect.colliderect(food):
        player1.width += 1
        player1.height += 1
        print(player1.width)
        foodX = random.randint(10, pygame.display.Info().current_w - food.width)
        foodY = random.randint(10, pygame.display.Info().current_h - food.height)
        food = pygame.draw.rect(screen, (255, 0, 255), (foodX, foodY, 10, 10))

    if player2Rect.colliderect(food):
        player2.width += 1
        player2.height += 1
        print(player2.width)
        foodX = random.randint(10, pygame.display.Info().current_w - food.width)
        foodY = random.randint(10, pygame.display.Info().current_h - food.height)
        food = pygame.draw.rect(screen, (255, 0, 255), (foodX, foodY, 10, 10))

        if playerRect.colliderect(ammo2):
            player1.velocity = 0

    # playerRect
    # player2Img
    # ammo
    # ammo2

    pygame.display.update()
    screen.fill((136, 89, 47))

    dogX = random.randint(10, pygame.display.Info().current_w)
    dogY = random.randint(10, pygame.display.Info().current_h)

    if player1.width >= 60 or player2.width >= 60 or keyboard.is_pressed("ctrl+q"):
        if player1.width >= 60 or player1.width > player2.width:
            end_text = my_font.render(f'Player1 wins with {player1.width - 50} score', False, (255, 0, 255))
            screen.blit(end_text, (pygame.display.Info().current_w / 2 - 250, pygame.display.Info().current_h / 2))
        else:
            if player1.width == player2.width:
                end_text = my_font.render(f'Tie!', False, (255, 0, 255))
                screen.blit(end_text, (pygame.display.Info().current_w / 2, pygame.display.Info().current_h / 2))
            else:
                end_text = my_font.render(f'Player2 wins with {player2.width - 50} score', False, (0, 0, 255))
                screen.blit(end_text,
                            (pygame.display.Info().current_w / 2 - 250, pygame.display.Info().current_h / 2))
        # screen.blit(end_text, (pygame.display.Info().current_w / 2 - 250, pygame.display.Info().current_h / 2))
        pygame.display.update()
        time.sleep(2)
        Settings.isRunning = False
        pygame.quit()

pygame.quit()


def initGame():
    pass


if __name__ == '__main__':
    Game.run()
    initGame()
#    gameLoop()
