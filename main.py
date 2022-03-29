import pygame
import random
import math


# adding a screen
screen = pygame.display.set_mode((800, 600))

# background
background = pygame.image.load("bg.png")
# game ko naam
pygame.display.set_caption("Dodge")
# game icon
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)

# player
playerImg = pygame.image.load("spaceship.png")
playerx = 350
playery = 550
play_mov = 0
play_mov1 = 0

# enemy1
enemyImg = pygame.image.load("enemy.png")
enemyx = random.randint(10, 756)
enemyy = 50
enemy_mov1 = 1

# enemy2
enemy2Img = pygame.image.load("venus.png")
enemy2x = random.randint(10, 756)
enemy2y = 50
enemy_mov2 = 1

# enemy3
enemy3Img = pygame.image.load("red.png")
enemy3x = random.randint(10, 756)
enemy3y = 50
enemy_mov3 = 1

# star
startImg = pygame.image.load("star.png")
starx = random.randint(10, 756)
stary = 50
star_mov = 0.75

# star2
start2Img = pygame.image.load("star.png")
star2x = random.randint(10, 756)
star2y = 50
star_mov2 = 0.75

# score
scoreImg = pygame.image.load("cup.png")
scorex = 100
scorey = 0

# clock
clockImg = pygame.image.load("clock.png")
clockx = 600
clocky = 0

n = 0.001
p = 0.001
p2 = 0.001

#points
points = 0


def player():
    screen.blit(playerImg, (playerx, playery))


def enemy():
    screen.blit(enemyImg, (enemyx, enemyy))


def enemy2():
    screen.blit(enemy2Img, (enemy2x, enemy2y))


def enemy3():
    screen.blit(enemy3Img, (enemy3x, enemy3y))


def star():
    screen.blit(startImg, (starx, stary))


def star2():
    screen.blit(startImg, (star2x, star2y))


def score():
    screen.blit(scoreImg, (scorex, scorey))


def clock():
    screen.blit(clockImg, (clockx, clocky))


def is_collision(playerx, playery, enemyx, enemyX):
    distance = math.sqrt(math.pow(playerx - enemyx, 2) + math.pow(playery - enemyy, 2))
    if distance < 20:
        return True
    else:
        return False


def is_collision2(playerx, playery, enemy2x, enemy2X):
    distance = math.sqrt(math.pow(playerx - enemy2x, 2) + math.pow(playery - enemy2y, 2))
    if distance < 20:
        return True
    else:
        return False


def is_collision3(playerx, playery, enemy3x, enemy3X):
    distance = math.sqrt(math.pow(playerx - enemy3x, 2) + math.pow(playery - enemy3y, 2))
    if distance < 20:
        return True
    else:
        return False


def is_collision4(playerx, playery, starx, syary):
    distance = math.sqrt(math.pow(playerx - starx, 2) + math.pow(playery - stary, 2))
    if distance < 20:
        return True
    else:
        return False


def is_collision5(playerx, playery, star2x, syar2y):
    distance = math.sqrt(math.pow(playerx - star2x, 2) + math.pow(playery - star2y, 2))
    if distance < 20:
        return True
    else:
        return False


# main loop
run = True
while run:
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                play_mov += 4
            if event.key == pygame.K_LEFT:
                play_mov -= 4
            if event.key == pygame.K_UP:
                play_mov1 -= 4
            if event.key == pygame.K_DOWN:
                play_mov1 += 4
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                play_mov = 0
            elif event.key == pygame.K_LEFT:
                play_mov = 0
            elif event.key == pygame.K_UP:
                play_mov1 = 0
            elif event.key == pygame.K_DOWN:
                play_mov1 = 0

    playerx += play_mov
    if playerx <= 0:
        playerx = 0
    elif playerx >= 756:
        playerx = 756
    playery += play_mov1
    if playery <= 0:
        playery = 0
    elif playery >= 556:
        playery = 556

    enemy_mov1 += n

    enemyy += enemy_mov1
    if enemyy <= 0:
        enemyy = 0
    elif enemyy >= 746:
        enemyx = random.randint(10, 756)
        enemyy = 0

    enemy_mov2 += n

    enemy2y += enemy_mov2
    if enemy2y <= 0:
        enemy2y = 0
    elif enemy2y >= 746:
        enemy2x = random.randint(10, 756)
        enemy2y = 0

    enemy_mov3 += n

    enemy3y += enemy_mov3
    if enemy3y <= 0:
        enemy3y = 0
    elif enemy3y >= 746:
        enemy3x = random.randint(10, 756)
        enemy3y = 0

    

    stary += star_mov
    if stary <= 0:
        stary = 0
    elif stary >= 746:
        stary = random.randint(10, 746)
        stary = 10

    

    star2y += star_mov2
    if star2y <= 0:
        star2y = 0
    elif star2y >= 746:
        star2y = random.randint(10, 746)
        star2y = 0

    collision = is_collision(playerx, playery, enemyx, enemyy)

    if collision:
        import gameover

        break

    collision = is_collision2(playerx, playery, enemy2x, enemy2y)

    if collision:
        import gameover

        break

    collision = is_collision3(playerx, playery, enemy3x, enemy3y)

    if collision:
        import gameover

        break

    collision = is_collision4(playerx, playery, starx, stary)

    if collision:
        points += 1
        star_mov += p
        print(points)
        stary = 0
        starx = random.randint(10, 756)

    collision = is_collision5(playerx, playery, star2x, star2y)

    if collision:
        points += 1
        star_mov2 += p
        print(points)
        star2y = 0
        star2x = random.randint(10, 756)

    player()
    enemy()
    enemy2()
    enemy3()
    star()
    star2()
    clock()
    pygame.display.update()
