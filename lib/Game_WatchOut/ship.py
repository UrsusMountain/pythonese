import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    def __init__(self,screen):
        super().__init__()
        self.screen=screen
        self.screen_rect=screen.get_rect()
        self.image=pygame.image.load('images/dark.bmp')
        self.rect=self.image.get_rect()
        self.rect.bottom=self.screen_rect.bottom-10
        self.rect.centerx=self.screen_rect.centerx
        self.moving_left=False
        self.moving_right = False
        self.moving_up = False
        self.moving_down = False

    def update_pos(self,setting):
        if self.moving_left and self.rect.x > 0:
            self.rect.x-=setting.ship_speed
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x+=setting.ship_speed
        if self.moving_up and self.rect.top > 0:
            self.rect.y-=setting.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.y+=setting.ship_speed

    def blitme(self):
        self.screen.blit(self.image,self.rect)
