import pygame
import time
import os
import random

pygame.font.init()

WIDTH = 1920
HEIGHT = 1080

NAMSO_RIGHT = [pygame.transform.scale2x(pygame.image.load('imgs/Namso/Right' + str(x) + '.png')) for x in range(1,9)]
NAMSO_LEFT = [pygame.transform.scale2x(pygame.image.load('imgs/Namso/Left' + str(x) + '.png')) for x in range(1,9)]

ORC_LEFT = [pygame.transform.scale2x(pygame.image.load('imgs/Orc/Left' + str(x) + '.png')) for x in range(1,9)]

BACKG = pygame.image.load('imgs/BG.jpg')
CASTLE = pygame.transform.scale2x(pygame.image.load('imgs/Castle.png'))

STAT_FONT = pygame.font.SysFont('comicsans', 75)
HS_FONT = pygame.font.SysFont('comicsans', 40)

#Defining the heroic attributes of this games main hero
class Namso:

    #Defining visual attributes
    SPRITE_RIGHT = NAMSO_RIGHT
    SPRITE_LEFT = NAMSO_LEFT

    #Defining other necessary parameters
    IMG_CLOCK = 2
    img_frame = 0

    #The heros position and appearance in the game
    def __init__(self):
        self.img = self.SPRITE_RIGHT[0]
        self.right = True
        self.img_frame = 0

    def draw(self, win, right_key, x, y):

        self.img_frame += 1
    
        if right_key == True:
            if self.img_frame < self.IMG_CLOCK:
                self.img = self.SPRITE_RIGHT[0]
            elif self.img_frame < self.IMG_CLOCK*2:
                self.img = self.SPRITE_RIGHT[1]
            elif self.img_frame < self.IMG_CLOCK*3:
                self.img = self.SPRITE_RIGHT[2]
            elif self.img_frame < self.IMG_CLOCK*4:
                self.img = self.SPRITE_RIGHT[3]
            elif self.img_frame < self.IMG_CLOCK*5:
                self.img = self.SPRITE_RIGHT[4]
            elif self.img_frame < self.IMG_CLOCK*6:
                self.img = self.SPRITE_RIGHT[5]
            elif self.img_frame < self.IMG_CLOCK*7:
                self.img = self.SPRITE_RIGHT[6]
            elif self.img_frame < self.IMG_CLOCK*8:
                self.img = self.SPRITE_RIGHT[7]
            elif self.img_frame < self.IMG_CLOCK*8 + 1:
                self.img = self.SPRITE_RIGHT[0]
                self.img_frame = 0
        
        if right_key == False:
            if self.img_frame < self.IMG_CLOCK:
                self.img = self.SPRITE_LEFT[0]
            elif self.img_frame < self.IMG_CLOCK*2:
                self.img = self.SPRITE_LEFT[1]
            elif self.img_frame < self.IMG_CLOCK*3:
                self.img = self.SPRITE_LEFT[2]
            elif self.img_frame < self.IMG_CLOCK*4:
                self.img = self.SPRITE_LEFT[3]
            elif self.img_frame < self.IMG_CLOCK*5:
                self.img = self.SPRITE_LEFT[4]
            elif self.img_frame < self.IMG_CLOCK*6:
                self.img = self.SPRITE_LEFT[5]
            elif self.img_frame < self.IMG_CLOCK*7:
                self.img = self.SPRITE_LEFT[6]
            elif self.img_frame < self.IMG_CLOCK*8:
                self.img = self.SPRITE_LEFT[7]
            elif self.img_frame < self.IMG_CLOCK*8 + 1:
                self.img = self.SPRITE_LEFT[0]
                self.img_frame = 0

        win.blit(self.img, (x, y))

#Defining the vile attributes of this games evil villain
class Orc:

    #Defining visual attributes
    SPRITE_LEFT = ORC_LEFT

    #Defining other necessary parameters
    IMG_CLOCK = 2
    img_frame = 0
    SPEED = 10

    #The heros position and appearance in the game
    def __init__(self, x):
        self.img = self.SPRITE_LEFT[0]
        self.x = x
        self.y = 800
        self.img_frame = 0

    def draw(self, win):
        self.x -= self.SPEED

        self.img_frame += 1

        if self.img_frame < self.IMG_CLOCK:
            self.img = self.SPRITE_LEFT[0]
        elif self.img_frame < self.IMG_CLOCK*2:
            self.img = self.SPRITE_LEFT[1]
        elif self.img_frame < self.IMG_CLOCK*3:
            self.img = self.SPRITE_LEFT[2]
        elif self.img_frame < self.IMG_CLOCK*4:
            self.img = self.SPRITE_LEFT[3]
        elif self.img_frame < self.IMG_CLOCK*5:
            self.img = self.SPRITE_LEFT[4]
        elif self.img_frame < self.IMG_CLOCK*6:
            self.img = self.SPRITE_LEFT[5]
        elif self.img_frame < self.IMG_CLOCK*7:
            self.img = self.SPRITE_LEFT[6]
        elif self.img_frame < self.IMG_CLOCK*8:
            self.img = self.SPRITE_LEFT[7]
        elif self.img_frame < self.IMG_CLOCK*8 + 1:
            self.img = self.SPRITE_LEFT[0]
            self.img_frame = 0

        win.blit(self.img, (self.x, self.y))

#Drawing and updating the game window and state
def draw_window(win, namso, score, right_key, namsoX, namsoY, orcs, lives, highscore, gamestart):
    win.blit(BACKG, (0,0))
    win.blit(CASTLE, (-30, 620))
    namso.draw(win, right_key, namsoX, namsoY)
    score_text = STAT_FONT.render('Score: ' + str(score), 1, (255, 255, 255))
    hs_text = HS_FONT.render('High Score: ' + str(highscore), 1, (255, 255, 255))
    lives_text = STAT_FONT.render('Lives: ' + str(lives), 1, (255, 255, 255))
    title_text = STAT_FONT.render('Namso Jumper!', 1, (255, 255, 255))
    info_text = HS_FONT.render('Use the arrow keys to jump and change direction!', 1, (255, 255, 255))
    start_text = HS_FONT.render('PRESS SPACE TO START!', 1, (255, 255, 255))
    win.blit(score_text, (25, 25))
    win.blit(hs_text, (25, 90))
    win.blit(lives_text, (WIDTH-250, 25))
    win.blit(title_text, (750, 50))

    if gamestart == False:
        win.blit(info_text, (640, 250))
        win.blit(start_text, (780, 300))

    for orc in orcs:
        orc.draw(win)

    pygame.display.update()

#The main method for this game
def main():
    win = pygame.display.set_mode((WIDTH, HEIGHT))
    run = True
    score = 0
    lives = 3
    gamestart = False

    orcs = []

    #Initializing orc spawn timer
    orc_ticker = time.time()
    orc_spawn_trigger = 2

    charX = 960
    charY = 780
    charJump = False
    vert_vel = 4
    highscore = 0

    physTime = 0

    right_key = True

    namso = Namso()

    while run:

        #Check for game exit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    right_key = True
                if event.key == pygame.K_LEFT:
                    right_key = False
                if event.key == pygame.K_UP:
                    charJump = True
                if event.key == pygame.K_SPACE:
                    gamestart = True


        #Keeping track of the highscore
        hisc = open('highscore.txt', 'r')
        highscore = hisc.read()
        highscore_int = int(highscore)

        if score > highscore_int:
            hisc = open('highscore.txt', 'w+')
            hisc.write(str(score))

        hisc.close()


        if gamestart == True: 
        
            #Handling horizontal character movement
            move_ticker = 0

            if right_key == True:
                if move_ticker == 0:
                    move_ticker = 60
                    charX += 16
                    if charX >= 1875:
                        charX = 1875

            if right_key == False:
                if move_ticker == 0:
                    move_ticker = 60
                    charX -= 16
                    if charX <= 225:
                        lives -= 1
                        charX = 225
            
            if move_ticker > 0:
                move_ticker -= 1

            #Handling vertical character movement
            if charJump == True:
                physTime += 1.0
            
            charY = charY - vert_vel*physTime + 0.25*physTime**2
        
            if charY > 780:
                charJump = False
                physTime = 0
                charY = 780
            
            spawn_delay = time.time() - orc_ticker

            #Handling the spawning of orcs
            if spawn_delay >= orc_spawn_trigger:
                orcs.append(Orc(1920))
                orc_ticker = time.time()
                orc_spawn_trigger = random.randrange(1,3)

                if score > 20:
                    orc_spawn_trigger = orc_spawn_trigger/1.2
                if score > 40:
                    orc_spawn_trigger = orc_spawn_trigger/1.2
                if score > 60:
                    orc_spawn_trigger = orc_spawn_trigger/1.2
                if score > 80:
                    orc_spawn_trigger = orc_spawn_trigger/1.2
                if score > 100:
                    orc_spawn_trigger = orc_spawn_trigger/1.2

            for orc in orcs:
                if orc.x >= charX - 15 and orc.x <= charX + 15 and charY >= 700:
                    lives -= 1
                    orcs.remove(orc)

                if orc.x <= 115:
                    orcs.remove(orc)
                    score += 1
    

        #Drawing the resulting actions
        if lives > 0:
            draw_window(win, namso, score, right_key, charX, charY, orcs, lives, highscore, gamestart)
        else:
            gamestart = False
            main()


    pygame.quit()
    quit()

main()