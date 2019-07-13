import pygame
import pygame.font
class Button:
    def __init__(self,setting,screen):
        self.screen=screen
        self.screen_rect=self.screen.get_rect()
        self.setting=setting
        self.rect=pygame.Rect(0,0,self.setting.button_width,self.setting.button_height)
        self.color=(0,50,50)
        self.rect.center=self.screen_rect.center
        self.font=pygame.font.SysFont(None,30)
        self.text_color = (230, 100, 100)
        self.prep_button_text()
        self.mouse_x=0
        self.mouse_y=0

    def draw_button(self):
        self.screen.fill(self.color,self.rect)
        self.screen.blit(self.image,self.image_rect)

    def prep_button_text(self):
        self.image=self.font.render("Play",True,self.text_color,self.color)
        self.image_rect=self.image.get_rect()
        self.image_rect.center=self.rect.center
        self.image_pause=self.font.render('Pause',True,self.text_color,self.color)
        self.image_pause_rect=self.image_pause.get_rect()
        self.image_pause_rect.center=self.rect.center

    def draw_pause_button(self):
        self.screen.fill(self.color,self.rect)
        self.screen.blit(self.image_pause,self.image_pause_rect)

