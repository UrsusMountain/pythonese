from pygame.sprite import Sprite
import pygame,random

class Gift(Sprite):
    def __init__(self,screen,setting):
        super().__init__()
        self.screen=screen
        self.screen_rect=screen.get_rect()
        self.setting=setting
        self.image=pygame.image.load('images/dark2.bmp')
        self.rect=self.image.get_rect()
        self.rect.y=-2
        self.width=self.rect.width
        self.height=self.rect.height
        self.rect.x=random.randint(0,round(setting.screen_width-self.width))

    def update(self):
        self.rect.y+=self.setting.gift_speed


    def blitme(self):
        self.screen.blit(self.image,self.rect)






