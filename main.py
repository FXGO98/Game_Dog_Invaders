import pygame
import sys
import random
import math
from pygame import mixer

# initialize the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

# Background
background = pygame.image.load('background.jpg')

# Background Sound
mixer.music.load('Imperial_Borks.wav')

# Bullet Sound 
bullet_sound = mixer.Sound('Bruh.wav')

# Title and Icon
pygame.display.set_caption("Peepee Attack")
icon = pygame.image.load('moon.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 480
playerX_change = 0
playerY_change = 0
playerX_speed = 3
playerY_speed = 3


# Enemy Speed
speed_counter = 0
enemyX_speed = 3


# Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6
enemy_attacks = []

for i in range (num_of_enemies):
    enemyImg.append(pygame.image.load('enemy.png'))
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(enemyX_speed)
    enemyY_change.append(30)
    enemy_attacks.append(False)

# Bullet

# Ready - You can't see the bullet on the screen
# Fire - The bullet is currently moving
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
# bulletX_change = 0
bulletY_change = 4
bullet_state = "ready"


# Score
score_value = 0
counter = 0

font = pygame.font.Font('MICKEY.TTF', 32)

textX = 10
textY = 10


# Enemy Score
enemy_score = 0


winning_font = pygame.font.Font('MICKEY.TTF', 64)



over_font = pygame.font.Font('MICKEY.TTF', 64)


def show_score (x,y):
    score = font.render("Score: " + str(score_value), True, (255, 255, 255))
    e_score = font.render("World Domination: " + str(enemy_score), True, (255, 255, 255))
    screen.blit(score, (x,y))
    screen.blit(e_score, (400-x, y))

def winning_text(x, y):
    winning_font = font.render("YOU SAVED THIS PLANET", True, (255, 255, 255))
    score = font.render("Score: " + str(score_value), True, (255, 255, 255))
    screen.blit(winning_font, (x,y))
    screen.blit(score, (x+172, y+50))

def game_over_text(x, y):
    over_font = font.render("GAME OVER", True, (255, 255, 255))
    score = font.render("Score: " + str(score_value), True, (255, 255, 255))
    screen.blit(over_font, (x,y))
    screen.blit(score, (x+32, y+50))

def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))


def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX-bulletX, 2)) + (math.pow(enemyY-bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False

def Player_Collision(enemyX, enemyY, playerX, playerY):
    distance = math.sqrt((math.pow(enemyX-playerX, 2)) + (math.pow(enemyY-playerY, 2)))
    if distance < 55:
        return True
    else:
        return False

def main_menu():

    while True:

        # Background Image
        screen.blit(background,(0, 0))

        button_1 = pygame.Rect(307, 198, 186, 64)
        
        pygame.draw.rect(screen, (255, 0, 0), button_1)

        button_2 = pygame.Rect(310, 338, 186, 58)
        
        pygame.draw.rect(screen, (255, 0, 0), button_2)

        start_button = pygame.image.load('start_button.png').convert()

        screen.blit(start_button, (301, 191))

        start_button = pygame.image.load('quit_button.png').convert()

        screen.blit(start_button, (301, 331))


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if button_1.collidepoint(x, y):
                    game()

                if button_2.collidepoint(x, y):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


def game():

    global playerX, playerX_change, playerY, playerY_change, playerX_speed, playerY_speed
    global bulletX, bulletY, speed_counter, enemyX_speed, score_value, enemy_score 
    global bullet_state, bulletY_change, counter, num_of_enemies
    

    # Playing Background music
    mixer.music.play(-1)
        
    while True:

        """ # RGB - Red, Green, Blue
        screen.fill((100, 151, 177)) """

        # Background Image
        screen.blit(background,(0, 0))


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # if keystroke is pressed check whether its right or left
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    playerX_change = -playerX_speed
                        

                if event.key == pygame.K_RIGHT:
                    playerX_change = playerX_speed


                if event.key == pygame.K_UP:
                    playerY_change = -playerY_speed
                        

                if event.key == pygame.K_DOWN:
                    playerY_change = playerY_speed   


                if event.key == pygame.K_SPACE:
                    if bullet_state is "ready":
                        # Get the current x and y coordinates of the spaceship
                        bulletX = playerX
                        bulletY = playerY
                        bullet_sound.play()
                        fire_bullet(bulletX, bulletY)
            

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    playerX_change = 0

                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    playerY_change = 0


        # Player Movement
        playerX += playerX_change
        playerY += playerY_change


        # Player Boundaries
        if playerX <= 0:
            playerX = 0
            
        elif ((playerX >= 736) and (playerX < 1500)):
            playerX = 736

        elif playerX == 1500:
            playerX = 2000

        if playerY <= 0:
            playerY = 0
            
        elif ((playerY >= 536) and (playerY < 1500)):
            playerY = 536

        elif playerY == 1500:
            playerY = 2000


        # Enemy Movement
        for i in range (num_of_enemies):

            # Winning Game

            if (score_value >= 2) and (enemy_score == 0):
                game_winning()
                
                
            # Game Over

            player_enemy_collision = Player_Collision(enemyX[i] + 32 , enemyY[i] + 32, playerX + 32, playerY + 32)

            if (enemy_score==3):

                for j in range (num_of_enemies):
                    enemyY[j] = 2000
                playerX = 2000
                playerY = 2000
                game_over_text(300, 240)
                pygame.mixer.music.stop()
                bullet_sound.stop()
                break

            if (player_enemy_collision==True):

                for j in range (num_of_enemies):
                    enemyY[j] = 2000
                playerX = 2000
                playerY = 2000
                game_over_sound = mixer.Sound('Explosion.wav')
                game_over_sound.play()
                game_over_text(300, 240)
                pygame.mixer.music.stop()
                bullet_sound.stop()
                break


            enemyX[i] += enemyX_change[i]


            # Enemy Boundaries
            if enemyX[i] <= 0:
                enemyX_change[i] = enemyX_speed
                enemyY[i] += enemyY_change[i] 
                
            elif enemyX[i] >= 736:
                enemyX_change[i] = -enemyX_speed
                enemyY[i] += enemyY_change[i] 

            elif enemyY[i] <=30:
                enemyY_change[i] = - enemyY_change[i]

            elif ((enemyY[i] >=476) and (enemyY[i]<=506) and (enemy_attacks[i]==True)):
                enemy_attacks[i] = False

            elif enemyY[i] >= 506:
                enemyY_change[i] = - enemyY_change[i]
                if enemy_attacks[i] == False:
                    enemy_attacks[i] = True
                    enemy_score += 1

            # Collision
            collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
            
            if collision:
                explosion_sound = mixer.Sound('Dog_Dies.wav')
                explosion_sound.play()
                bulletY = 900
                bullet_state = "ready"
                score_value += 1
                speed_counter += 1
                    
                if enemy_score>0:
                    counter += 1

                if counter >= 20:
                    score_value -= 20
                    enemy_score -= 1
                    counter = 0
                    speed_counter = 0
                    bulletY_change -= 2
                    enemyX_speed -= 1.5
                    playerX_speed += 1.5
                    playerY_speed += 1.5

                if speed_counter == 10:
                    speed_counter = 0
                    bulletY_change += 2
                    enemyX_speed += 1.5
                    playerX_speed += 1.5
                    playerY_speed += 1.5


                enemyX[i] = random.randint(0, 736)
                enemyY[i] = random.randint(50, 150)

            enemy(enemyX[i], enemyY[i], i)

            
        # Bullet Movement
        if bulletY <= 0:
            bulletY = 900
            bullet_state = "ready"

        if bullet_state is "fire":
            fire_bullet(bulletX, bulletY)
            bulletY -= bulletY_change
            

        player(playerX, playerY)

        show_score(textX, textY)
            
        pygame.display.update()

        print(enemy_score)


#def game_over_domination():

#def game_over_collision():

def game_winning():

    global playerX, playerY, enemyX, enemyY, num_of_enemies

    while True:
        for j in range (num_of_enemies):
            enemyY[j] = 2000
        
        for j in range (num_of_enemies):
            enemy(enemyX[j], enemyY[j], j)
        playerX = 2000
        playerY = 2000
        winning_text(150, 240)
        pygame.mixer.music.stop()
        bullet_sound.stop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        player(playerX, playerY)



        pygame.display.update()

main_menu()
            
