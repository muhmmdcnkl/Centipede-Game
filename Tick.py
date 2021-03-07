import os

import pygame, random, math

class Tick(pygame.sprite.Sprite):

    image = None

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        game_folder = os.path.dirname(__file__)
        img_folder = os.path.join(game_folder, "img")
        if Tick.image is None:
            Tick.image = pygame.image.load(os.path.join(img_folder,"tick.png"))
        self.image = Tick.image
        self.x = random.randint(0,24)
        self.y = 0
    
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x*25, self.y*25)
        
    def move(self,game_map):
       
        r = random.randint(0,2)
        self.y +=1
        self.rect.topleft = (self.x*25, self.y*25)

        if self.y == 27:
            return
        if r == 1 and self.y <26:
            game_map[self.y][self.x] = 1
        
            
    def dead(self):

        self.y = 100
        self.rect.topleft = (self.x*25, self.y*25)

        
    def offscreen(self):
        if self.y >28:
            return True
        else:
            return False
