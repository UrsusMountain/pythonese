from pygame.sprite import Sprite
import pygame

class Alien(Sprite):
    def __init__(self,screen,setting):
        super().__init__()
        self.setting=setting
        self.image=pygame.image.load('images/alien.bmp')
        self.rect=self.image.get_rect()
        self.screen=screen
        self.rect.x=self.rect.width
        self.rect.y=0
        self.height=self.rect.height
        self.width=self.rect.width

    def blitme(self):
        self.screen.blit(self.image,self.rect)

    def update_pos(self,setting):
        self.rect.y+=setting.alien_speed

    def move(self):
        self.rect.y+=self.setting.alien_speed


