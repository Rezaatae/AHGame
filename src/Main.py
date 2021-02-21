import pygame
import random
import math
from pygame import mixer

# Initialize the pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))

background = pygame.image.load("background.jpg")

mixer.music.load("ES_Scary Stairsteps - Stationary Sign.mp3")
mixer.music.play(-1)

# title and icon
pygame.display.set_caption("ToastVSGhosts")
icon = pygame.image.load("toaster.png")
pygame.display.set_icon(icon)

goosePointerImg = pygame.image.load("goosepoint.png")

# player
playerImg = pygame.image.load("toast.png")
playerX = 370
playerY = 480
playerX_change = 0
playerY_change = 0
# enemy
gooseImg = []
gooseX = []
gooseY = []
gooseX_change = []
gooseY_change = []

num_of_geese = 3
for i in range(num_of_geese):
    gooseImg.append(pygame.image.load("goose.png"))
    gooseX.append(random.randint(0, 735))
    gooseY.append(random.randint(50, 150))
    gooseX_change.append(0.3)
    gooseY_change.append(40)

# enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []

num_of_enemys = 6
for i in range(num_of_enemys):
    enemyImg.append(pygame.image.load("ghost (1).png"))
    enemyImg.append(pygame.image.load("ghost (2).png"))
    enemyImg.append(pygame.image.load("ghost (3).png"))
    enemyImg.append(pygame.image.load("ghost (4).png"))
    enemyImg.append(pygame.image.load("ghost (5).png"))
    enemyImg.append(pygame.image.load("ghost (6).png"))
    enemyX.append(random.randint(0, 735))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(0.3)
    enemyY_change.append(40)

# bullet
bulletImg = pygame.image.load("bullet.png")
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 2
bullet_state = "ready"

score = 0

font = pygame.font.Font("freesansbold.ttf", 24)
gameOverFont = pygame.font.Font("freesansbold.ttf", 64)
youWingFont = pygame.font.Font("freesansbold.ttf", 64)

textX = 10
textY = 10

gooseScore = 0

def showScore(x, y):
    score_Value = font.render("Score: " + str(score), True, (255,255,255))
    screen.blit(score_Value, (x, y))

def showYouWin():
    gameOver = youWingFont.render("YOU WIN!", True, (0, 225, 0))
    screen.blit(gameOver, (300, 300))

def showGameOver():
    gameOver = gameOverFont.render("GAME OVER!", True, (255, 0, 0))
    screen.blit(gameOver, (300, 300))

def showGoosePoints(x, y):
    gooseScore_Value = font.render(": "+str(gooseScore), True, (255,255,255))
    screen.blit(gooseScore_Value, (x + 67, y + 30))
    screen.blit(goosePointerImg, (x + 30, y + 30))

def player(x, y):
    screen.blit(playerImg, (x, y))

def goose(x, y, i):
    screen.blit(gooseImg[i], (x, y))

def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 20, y + 15))

def isCapture(gooseX, gooseY, playerX, playerY):
    distance = math.sqrt((math.pow(gooseX - playerX, 2)) + (math.pow(gooseY - playerY, 2)))
    if distance < 30:
        return True
    else:
        return False

def isToastGhost(playerX, playerY, enemyX, enemyY):
    distance = math.sqrt((math.pow(enemyX - playerX, 2)) + (math.pow(enemyY - playerY, 2)))
    if distance < 50:
        return True
    else:
        return False

def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY - bulletY, 2)))
    if distance < 20:
        return True
    else:
        return False

def isGooseDown(gooseX, gooseY, bulletX, bulletY):
    distance = math.sqrt((math.pow(gooseX - bulletX, 2)) + (math.pow(gooseY - bulletY, 2)))
    if distance < 25:
        return True
    else:
        return False
# Game loop
running = True
while running:

    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # check if key stroke presses is left or right
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.8
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.8
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bulletX = playerX
                    fire_bullet(playerX, playerY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerX_change = 0
                playerY_change = 0



    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736


    for i in range(num_of_geese):
        gooseX[i] += gooseX_change[i]
        if gooseX[i] <= 0:
            gooseX_change[i] = 0.5
            gooseY[i] += gooseY_change[i]
        elif gooseX[i] >= 736:
            gooseX_change[i] = -0.5
            gooseY[i] += gooseY_change[i]

        if isCapture(gooseX[i], gooseY[i], playerX, playerY):
            gooseScore += 1
            gooseX[i] = random.randint(0, 735)
            gooseY[i] = random.randint(50, 150)
        goose(gooseX[i], gooseY[i], i)

        if isGooseDown(gooseX[i], gooseY[i], bulletX, bulletY):
            for j in range(num_of_enemys):
                enemyY[j] = 2000
            for k in range(num_of_geese):
                gooseY[k] = 2000
            showGameOver()
            break
            bulletY = 480
            bullet_state = "ready"
            gooseScore -= 1
            gooseX[i] = random.randint(0, 735)
            gooseY[i] = random.randint(50, 150)
        goose(gooseX[i], gooseY[i], i)

        if gooseScore > 10:
            for j in range(num_of_enemys):
                enemyY[j] = -2000
            for k in range(num_of_geese):
                gooseY[k] = 2000
            showYouWin()
            break

    for i in range(num_of_enemys):
        if score > 50:
            for j in range(num_of_enemys):
                enemyY[j] = -2000
            for k in range(num_of_geese):
                gooseY[k] = 2000
            showYouWin()
            break
        if enemyY[i] >= playerY:
            for j in range(num_of_enemys):
                enemyY[j] = 2000
            for k in range(num_of_geese):
                gooseY[k] = 2000
            showGameOver()
            break

        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 0.7
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -0.7
            enemyY[i] += enemyY_change[i]

        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            bulletY = 480
            bullet_state = "ready"
            score += 1
            enemyX[i] = random.randint(0, 735)
            enemyY[i] = random.randint(50, 150)
        enemy(enemyX[i], enemyY[i], i)


    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"
    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change



    player(playerX, playerY)
    showScore(textX, textY)
    showGoosePoints(textX, textY)
    pygame.display.update()