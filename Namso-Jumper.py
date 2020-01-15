import pygame
import time
import os
import random

pygame.font.init()

WIDTH = 1920
HEIGHT = 1080

NAMSO_RIGHT = [pygame.transform.scale2x(pygame.image.load('imgs/Namso/Right' + str(x) + '.png')) for x in range(1,9)]
NAMSO_LEFT = [pygame.transform.scale2x(pygame.image.load('imgs/Namso/Left' + str(x) + '.png')) for x in range(1,9)]
BACKG = pygame.image.load('imgs/BG.jpg')

SCORE_FONT = pygame.font.SysFont('comicsans', 75)

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


#Drawing and updating the game window and state
def draw_window(win, namso, score, right_key, namsoX, namsoY):
    win.blit(BACKG, (0,0))
    namso.draw(win, right_key, namsoX, namsoY)
    text = SCORE_FONT.render('Score: ' + str(score), 1, (255, 255, 255))
    win.blit(text, (25, 25))

    pygame.display.update()

#The main method for this game
def main():
    win = pygame.display.set_mode((WIDTH, HEIGHT))
    run = True
    score = 0

    charX = 960
    charY = 780
    charJump = False
    vert_vel = 4

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

            
        #Handling horizontal character movement
        move_ticker = 0

        if right_key == True:
            if move_ticker == 0:
                move_ticker = 60
                charX += 10
                if charX >= 1875:
                    charX = 1875

        if right_key == False:
            if move_ticker == 0:
                move_ticker = 60
                charX -= 10
                if charX <= 0:
                    charX = 0
        
        if move_ticker > 0:
            move_ticker -= 1

        #Handling vertical character movement
        if charJump == True:
            physTime += 1.0
        
        charY = charY - vert_vel*physTime + 0.3*physTime**2
    
        if charY > 780:
            charJump = False
            physTime = 0
            charY = 780


        #Drawing the resulting actions
        draw_window(win, namso, score, right_key, charX, charY)

    pygame.quit()
    quit()

main()