import pygame
from pygame.sprite import Group
from pygame.sprite import Sprite
from Game_WatchOut.ship import Ship
from Game_WatchOut.gift import Gift
import pygame.font

class GiftShow(Sprite):
    def __init__(self,screen,setting):
        super().__init__()
        self.image=pygame.image.load('images/dark2.bmp')
        self.screen=screen
        self.setting=setting
        self.rect=self.image.get_rect()

    def prep_gift(self):
        self.gifts=Group()
        for i in range(self.setting.gift_number):
            gifticon=Gift(self.screen,self.setting)
            gifticon.rect.x=10+1.2*gifticon.rect.width*i
            ship=Ship(gifticon.screen)
            gifticon.rect.y=25+ship.rect.height
            self.gifts.add(gifticon)

    def blitme(self):
        #self.screen.blit(self.image,self.rect)
        self.gifts.draw(self.screen)







