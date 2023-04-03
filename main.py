import pygame
import random
import keyboard
import pyautogui
import time
from settings import Settings
from entity.Entity import Entity
from entity.Player import Player
import Game
from settings.Settings import my_font
from utils.Utils import Utils
from utils.sounds import Sounds

pygame.init()
pygame.mixer.init()

# SET UP
dogX = 20
dogY = 20
animationSwitcher = 0
timer = -100
collided = False
is_player_collision = False
test_vel = 8


def draw_text(text, color, width, height):
    # Fix width, height
    my_text = my_font.render(text, False, color)
    screen.blit(my_text, width, height)
    pygame.display.update()


screen = pygame.display.set_mode([pygame.display.Info().current_w, pygame.display.Info().current_h], pygame.FULLSCREEN)
clock = pygame.time.Clock()
pygame.mouse.set_visible(False)

Utils.play_music("intro.wav")

# OBJECT INITIALIZATION
player1 = Player(60, 120, 15 * Settings.SCALE, 22 * Settings.SCALE, 0, False, 8, 100.0,
                 Settings.IMG_PREFIX + "character.png", False)
player2 = Player(Settings.SCREEN_WIDTH - 150, Settings.SCREEN_HEIGHT - 150, 19 * Settings.SCALE, 24 * Settings.SCALE, 0,
                 False, 8, 100.0, Settings.IMG_PREFIX + "player2Left.png", False)

pebble = Entity(0, 0, 14 * Settings.SCALE, 11 * Settings.SCALE, Settings.IMG_PREFIX + "stone.png")
pebble.x = random.randint(pebble.width, pygame.display.Info().current_w - pebble.width)
pebble.y = random.randint(pebble.height, pygame.display.Info().current_h - pebble.height)

powerup = Entity(0, 0, 14 * Settings.SCALE, 12 * Settings.SCALE, Settings.IMG_PREFIX + "stemb.png")
powerup.x = random.randint(0, pygame.display.Info().current_w - powerup.width)
powerup.y = random.randint(0, pygame.display.Info().current_h - powerup.height)

# IMG INITIALIZATION
# convert alpha to draw only the object without transparent background -> collision
player1Img = pygame.image.load(player1.image).convert_alpha()
player1Img = pygame.transform.flip(player1Img, player1.direction, False)
player1Img = pygame.transform.scale(player1Img, (player1.width, player1.height))
player2Img = pygame.image.load(player2.image).convert_alpha()
player2Img = pygame.transform.flip(player2Img, player2.direction, False)
player2Img = pygame.transform.scale(player2Img, (player2.width, player2.height))

imgObject = pygame.image.load(Settings.IMG_PREFIX + "dog.jpg")
imgObject = pygame.transform.scale(imgObject, (100, 100))

s = pygame.Surface((1000, 750))  # the size of your rect
s.set_alpha(128)  # alpha level
s.fill((255, 255, 255))  # this fills the entire surface
# screen.blit(s, (0, 0))  # s is surface we draw on; (0,0) are the top-left coordinates

boosterX = player1.x
boosterY = player1.y
booster2X = player2.x
booster2Y = player2.y

# START UP TEXT
start_text = Settings.my_font.render("First one to get 10 score wins!", False, (0, 0, 255))
screen.blit(start_text,
            (pygame.display.Info().current_w // 2 - start_text.get_width() // 2,
             pygame.display.Info().current_h // 2))
pygame.display.update()
time.sleep(Settings.seconds)

screen.fill(Settings.BLACK)
start_text = Settings.my_font.render("Press 'ctrl+q' to end the game early!", False, (0, 0, 255))
screen.blit(start_text,
            (pygame.display.Info().current_w // 2 - start_text.get_width() // 2,
             pygame.display.Info().current_h // 2 - start_text.get_height()))
pygame.display.update()
time.sleep(Settings.seconds)

screen.fill(Settings.BLACK)
start_text = Settings.my_font.render("Press 'i' to restart the game!", False, (0, 0, 255))
screen.blit(start_text,
            (pygame.display.Info().current_w // 2 - start_text.get_width() // 2,
             pygame.display.Info().current_h // 2 - start_text.get_height() // 2))
pygame.display.update()
time.sleep(Settings.seconds)
Utils.stop_music()
Sounds.bg_music.play()

bgImg = pygame.image.load(Settings.IMG_PREFIX + "bg.png").convert_alpha()

# def gameLoop():
while Settings.isRunning:
    if Settings.isGame:
        animationSwitcher += 1
        timer += 1
        if player1.boost < 99.9:
            player1.boost += 0.1
        if player2.boost < 99.9:
            player2.boost += 0.1
        clock.tick(Settings.FPS)
        # screen.blit(s, (0, 0))  # (0,0) are the top-left coordinates
        # screen.blit(s, (0, 0))  # (0,0) are the top-left coordinates
        pygame.display.set_caption(f'{clock.get_fps() :.1f} FPS ')
        booster = pygame.draw.rect(screen, Settings.BACKGROUND_COLOR, (boosterX, boosterY, 2, 2))
        booster2 = pygame.draw.rect(screen, Settings.BACKGROUND_COLOR, (booster2X, booster2Y, 2, 2))
        cursorImg = pygame.draw.circle(screen, (255, 0, 0), [pyautogui.position().x, pyautogui.position().y], 10)

        # RECT INITIALIZATION
        player1Rect = pygame.draw.rect(screen, Settings.BACKGROUND_COLOR,
                                       (player1.x, player1.y, player1.width, player1.height))
        player2Rect = pygame.draw.rect(screen, Settings.BACKGROUND_COLOR,
                                       (player2.x, player2.y, player2.width, player2.height))

        pebbleRect = pygame.draw.rect(screen, Settings.BACKGROUND_COLOR,
                                      (pebble.x, pebble.y, pebble.width, pebble.height))
        pebbleImg = pygame.image.load(pebble.image).convert_alpha()
        pebbleImg = pygame.transform.scale(pebbleImg, (pebble.width, pebble.height))

        powerupRect = pygame.draw.rect(screen, Settings.BACKGROUND_COLOR,
                                       (powerup.x, powerup.y, powerup.width, powerup.height))
        powerupImg = pygame.image.load(powerup.image).convert_alpha()
        powerupImg = pygame.transform.scale(powerupImg, (powerup.width, powerup.height))

        # LABELS
        fps_text = Settings.my_font.render(f'{clock.get_fps() : .1f} FPS', False, (0, 0, 0))
        player1_score = Settings.my_font.render(f'Player1: {int(player1.score)}', False, (255, 0, 255))
        player2_score = Settings.my_font.render(f'Player2: {int(player2.score)}', False, (0, 0, 255))
        player1_boost = Settings.small_font.render(f'Boost: {round(player1.boost, 2)}', False, (255, 0, 255))
        player2_boost = Settings.small_font.render(f'Boost: {round(player2.boost, 2)}', False, (0, 0, 255))

        # RENDER
        screen.blit(bgImg, (0, 0))
        screen.blit(player1_boost, (25, 80))
        screen.blit(player2_boost,
                    (pygame.display.Info().current_w - (player2_boost.get_width() + 25), 80))
        screen.blit(player1_score, (25, 30))
        screen.blit(player2_score, (pygame.display.Info().current_w - player2_score.get_width() - 25, 30))
        screen.blit(fps_text, (pygame.display.Info().current_w // 2 - fps_text.get_width() // 2, 10))
        # screen.blit(imgObject, (dogX, dogY))
        screen.blit(pebbleImg, (pebble.x, pebble.y))

        # pes = screen.blit(imgObject, (pyautogui.position().x, pyautogui.position().y))
        # screen.blit(player2Img, (player2X - player2Rect.width, player2Y - player2Rect.height))
        # screen.blit(mainCharacter, (player1.x, player1.y))

        if 0 <= timer <= 200:
            screen.blit(powerupImg, (powerup.x, powerup.y))
        elif timer >= 1000:
            powerup.x = random.randint(0, pygame.display.Info().current_w - powerup.width)
            powerup.y = random.randint(0, pygame.display.Info().current_h - powerup.height)
            collided = False
            timer = 0

        # PLAYER ANIMATION
        if 0 <= animationSwitcher <= 10:
            # player1Rect = pygame.draw.rect(screen, (0, 0, 255), (player1.x, player1.y, player1.width, player1.height))
            # foodRect = pygame.draw.rect(screen, (100, 100, 100), (foodX, foodY, 20, 20))

            player1Img = pygame.image.load("assets/player1Right.png").convert_alpha()
            player1Img = pygame.transform.flip(player1Img, player1.direction, False)
            player1Img = pygame.transform.scale(player1Img, (player1.width, player1.height))

            player2Img = pygame.image.load("assets/player2Right.png").convert_alpha()
            player2Img = pygame.transform.flip(player2Img, player2.direction, False)
            player2Img = pygame.transform.scale(player2Img, (player2.width, player2.height))
        elif 10 <= animationSwitcher <= 20:
            # player1Rect = pygame.draw.rect(screen, (255, 0, 0), (player1.x, player1.y, player1.width, player1.height))
            # foodRect = pygame.draw.rect(screen, (10, 255, 50), (foodX, foodY, 20, 20))

            player1Img = pygame.image.load("assets/player1Left.png").convert_alpha()
            player1Img = pygame.transform.flip(player1Img, player1.direction, False)
            player1Img = pygame.transform.scale(player1Img, (player1.width, player1.height))

            player2Img = pygame.image.load("assets/player2Left.png").convert_alpha()
            player2Img = pygame.transform.flip(player2Img, player2.direction, False)
            player2Img = pygame.transform.scale(player2Img, (player2.width, player2.height))
        elif 20 <= animationSwitcher <= 30:
            # player1Rect = pygame.draw.rect(screen, (0, 255, 255), (player1.x, player1.y, player1.width, player1.height))
            # foodRect = pygame.draw.rect(screen, (30, 55, 150), (foodX, foodY, 20, 20))

            player1Img = pygame.image.load("assets/player1Left.png").convert_alpha()
            player1Img = pygame.transform.flip(player1Img, player1.direction, False)
            player1Img = pygame.transform.scale(player1Img, (player1.width, player1.height))

            player2Img = pygame.image.load("assets/player2Left.png").convert_alpha()
            player2Img = pygame.transform.flip(player2Img, player2.direction, False)
            player2Img = pygame.transform.scale(player2Img, (player2.width, player2.height))
        elif 30 <= animationSwitcher <= 40:
            player1Img = pygame.image.load("assets/player1Right.png").convert_alpha()
            player1Img = pygame.transform.flip(player1Img, player1.direction, False)
            player1Img = pygame.transform.scale(player1Img, (player1.width, player1.height))

            player2Img = pygame.image.load("assets/player2Right.png").convert_alpha()
            player2Img = pygame.transform.flip(player2Img, player2.direction, False)
            player2Img = pygame.transform.scale(player2Img, (player2.width, player2.height))
        elif animationSwitcher >= 40:
            animationSwitcher = 0

        screen.blit(player1Img, (player1.x, player1.y))
        screen.blit(player2Img, (player2.x, player2.y))

        # KEY EVENTS
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Settings.isRunning = False

        keys = pygame.key.get_pressed()

        # PLAYER 1 HANDLING
        if keys[pygame.K_w] and player1.y > 0:
            player1.y -= player1.velocity
        if keys[pygame.K_s] and player1.y < pygame.display.Info().current_h - player1Rect.height:
            player1.y += player1.velocity
        if keys[pygame.K_a] and player1.x > 0:
            player1.direction = True
            player1.x -= player1.velocity
        if keys[pygame.K_d] and player1.x < pygame.display.Info().current_w - player1Rect.width:
            player1.x += player1.velocity
            player1.direction = False
        if keys[pygame.K_ESCAPE]:
            Settings.isRunning = False

        if keys[pygame.K_LSHIFT]:
            player1.isPressed = True
            if player1.boost >= 1:
                boosterX = player1.x
                boosterY = player1.y
            else:
                player1.boost = 0
            if player1.boost > 0:
                player1.boost -= 1
        else:
            player1.isPressed = False

        # PLAYER 2 HANDLING
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

        if keys[pygame.K_KP0] or keys[pygame.K_RSHIFT]:
            player2.isPressed = True
            if player2.boost >= 1:
                booster2X = player2.x
                booster2Y = player2.y
            else:
                player2.boost = 0
            if player2.boost > 0:
                player2.boost -= 1
        else:
            player2.isPressed = False

        # GAME RESET
        if keys[pygame.K_i]:
            screen.fill(Settings.BACKGROUND_COLOR)
            end_text = Settings.restart_font.render(f'Restarting the game!', False, Settings.BLACK)
            screen.blit(end_text, (pygame.display.Info().current_w // 2 - 350, pygame.display.Info().current_h // 2))
            pygame.display.update()
            time.sleep(Settings.seconds)

            timer = -100
            powerup.x = random.randint(0, pygame.display.Info().current_w)
            powerup.y = random.randint(0, pygame.display.Info().current_h)
            powerupRect = pygame.draw.rect(screen, Settings.BACKGROUND_COLOR,
                                           (powerup.x, powerup.y, powerup.width, powerup.height))
            player1.score = 0
            player1.boost = 100
            player1.x = 60
            player1.y = 120
            player2.score = 0
            player2.boost = 100
            player2.x = pygame.display.Info().current_w - 150
            player2.y = pygame.display.Info().current_h - 150
            pebble.x = random.randint(pebble.width, pygame.display.Info().current_w - pebble.width)
            pebble.y = random.randint(pebble.width, pygame.display.Info().current_h - pebble.height)

        # COLLISION
        if player1Rect.colliderect(booster) and player1.isPressed:
            player1.velocity = 15
        else:
            player1.velocity = 8

        if player2Rect.colliderect(booster2) and player2.isPressed:
            player2.velocity = 15
        else:
            player2.velocity = 8

        if player1Rect.colliderect(powerupRect) and not collided:
            collided = True
            timer = 200
            player1.boost = 100

        if player2Rect.colliderect(powerupRect) and not collided:
            collided = True
            timer = 200
            player2.boost = 100

        if player1Rect.colliderect(pebbleRect):
            player1.score += .5
            player1.score += .5
            Sounds.collect.play()
            pebble.x = random.randint(pebble.width, pygame.display.Info().current_w - pebble.width)
            pebble.y = random.randint(pebble.width, pygame.display.Info().current_h - pebble.height)

        if player2Rect.colliderect(pebbleRect):
            player2.score += 1
            player2.height += 1
            Sounds.collect.play()
            pebble.x = random.randint(pebble.width, pygame.display.Info().current_w - pebble.width)
            pebble.y = random.randint(pebble.width, pygame.display.Info().current_h - pebble.height)

        if is_player_collision:
            if test_vel >= 0:
                if not player1.direction:
                    player2.x += test_vel
                else:
                    player2.x += (test_vel * -1)
                test_vel -= .5
            else:
                is_player_collision = False
                test_vel = 8

        if player1Rect.colliderect(player2Rect):
            if player2.velocity == 8:
                is_player_collision = True

        pygame.display.update()
        screen.fill(Settings.BACKGROUND_COLOR)

        dogX = random.randint(10, pygame.display.Info().current_w)
        dogY = random.randint(10, pygame.display.Info().current_h)

        # END SCREEN
        if player1.score >= Player.MAX_SCORE or player2.score >= Player.MAX_SCORE or keyboard.is_pressed("ctrl+q"):
            if player1.score >= Player.MAX_SCORE or player1.score > player2.score:
                Sounds.bg_music.stop()
                Sounds.win.play(-1)
                end_text = Settings.my_font.render(f'Player1 wins with {int(player1.score)} score', False,
                                                   (255, 0, 255))
                screen.blit(end_text, (pygame.display.Info().current_w / 2 - 250, pygame.display.Info().current_h / 2))
            else:
                if player1.score == player2.score:
                    end_text = Settings.my_font.render(f'Tie!', False, Settings.BLACK)
                    screen.blit(end_text, (pygame.display.Info().current_w / 2, pygame.display.Info().current_h / 2))
                else:
                    Sounds.bg_music.stop()
                    Sounds.win.play(-1)
                    end_text = Settings.my_font.render(f'Player2 wins with {int(player2.score)} score', False,
                                                       (0, 0, 255))
                    screen.blit(end_text,
                                (pygame.display.Info().current_w / 2 - 250, pygame.display.Info().current_h / 2))
                # screen.blit(end_text, (pygame.display.Info().current_w / 2 - 250, pygame.display.Info().current_h / 2))
            pygame.display.update()
            time.sleep(Settings.seconds)
            screen.fill(Settings.BACKGROUND_COLOR)
            pygame.display.update()
            Settings.isGame = False
    elif not Settings.isGame:
        again_text = Settings.my_font.render(f'Again? (y / n)', False, Settings.BLACK)
        screen.blit(again_text,
                    (pygame.display.Info().current_w / 2 - 150, pygame.display.Info().current_h / 2))
        pygame.display.update()
        if keyboard.is_pressed("n"):
            screen.fill(Settings.BACKGROUND_COLOR)
            end_text = Settings.my_font.render(f'Ending the game', False, Settings.BLACK)
            screen.blit(end_text, (pygame.display.Info().current_w / 2 - 125, pygame.display.Info().current_h / 2))
            pygame.display.update()
            time.sleep(Settings.seconds)
            Settings.isRunning = False
            pygame.quit()
        elif keyboard.is_pressed("y"):
            Sounds.win.stop()
            Sounds.bg_music.play(-1)
            pygame.display.update()
            screen.fill(Settings.BACKGROUND_COLOR)
            end_text = Settings.restart_font.render(f'Restarting the game!', False, Settings.BLACK)
            screen.blit(end_text, (pygame.display.Info().current_w // 2 - 350, pygame.display.Info().current_h // 2))
            pygame.display.update()
            time.sleep(Settings.seconds)

            timer = -100
            powerup.x = random.randint(0, pygame.display.Info().current_w)
            powerup.y = random.randint(0, pygame.display.Info().current_h)
            powerupRect = pygame.draw.rect(screen, Settings.BACKGROUND_COLOR,
                                           (powerup.x, powerup.y, powerup.width, powerup.height))
            player1.score = 0
            player1.boost = 100
            player1.x = 60
            player1.y = 120
            player2.score = 0
            player2.boost = 100
            player2.x = pygame.display.Info().current_w - 150
            player2.y = pygame.display.Info().current_h - 150
            pebble.x = random.randint(pebble.width, pygame.display.Info().current_w - pebble.width)
            pebble.y = random.randint(pebble.width, pygame.display.Info().current_h - pebble.height)
            Settings.isGame = True

pygame.quit()


def initGame():
    pass


if __name__ == '__main__':
    # Game.run()
    initGame()
    # gameLoop()
