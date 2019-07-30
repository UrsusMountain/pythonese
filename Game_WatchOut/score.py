import pygame
import time
from pygame.sprite import Group
from pygame.sprite import Sprite
import pygame.font
from Game_WatchOut.ship import Ship
class Score(Sprite):
    def __init__(self,setting,screen):
        super().__init__()
        self.setting=setting
        self.screen=screen
        self.screen_rect=self.screen.get_rect()
        self.life_number=setting.life
        self.score=0
        self.best_score=0
        self.font=pygame.font.SysFont(None,40)
        self.text_color=(0,0,0)
        self.bg_color=setting.bg_color
        self.best_score=0
        self.prep_score()
        self.prep_best_score()

    def time_now(self):
        t=time.time()
        return t

    def prep_score(self):
        score_str=str(round(self.score))
        self.score_image=self.font.render('Score '+score_str,True,self.text_color,self.bg_color)
        self.score_rect=self.score_image.get_rect()
        self.score_rect.y=20
        self.score_rect.x=self.setting.screen_width-self.score_rect.width-20

    def prep_best_score(self):
        best_score_str=str(round(self.best_score))
        self.best_score_image=self.font.render('Best Score '+best_score_str,True,self.text_color,self.bg_color)
        self.best_score_rect=self.best_score_image.get_rect()
        self.best_score_rect.top=self.screen_rect.top+5
        self.best_score_rect.centerx=self.screen_rect.centerx

    def prep_ship(self):
        self.ships=Group()
        for life in range(self.life_number):
            ship=Ship(self.screen)
            ship.rect.y=20
            ship.rect.x=10+1.2*ship.rect.width*life
            self.ships.add(ship)

    def show(self):
        self.screen.blit(self.score_image,self.score_rect)
        self.ships.draw(self.screen)
        self.screen.blit(self.best_score_image,self.best_score_rect)
