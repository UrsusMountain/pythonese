import pygame
from GameMaker.settings import Settings
from GameMaker.ship import Ship
from GameMaker import game_functions as gf
from pygame.sprite import Group
from GameMaker.game_stats import Gamestats
from GameMaker.button import Button
from GameMaker.scoreboard import Scoreboard


def run_game():
    #初始化游戏并传建一个屏幕对象
    pygame.init()
    ai_settings=Settings()
    bullets=Group()
    aliens=Group()
    screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    ship = Ship(ai_settings,screen)
    gf.create_fleet(ai_settings,screen,ship,aliens)
    pygame.display.set_caption('Alien Invasion')
    play_button=Button(ai_settings,screen,'Play')
    stats=Gamestats(ai_settings)
    sb=Scoreboard(ai_settings,screen,stats)
    #开始游戏的主循环
    while True:
        #监视键盘和鼠标事件
        gf.check_events(ai_settings,screen,ship,bullets,stats,play_button,aliens,sb)
        if stats.game_active:
            ship.update()
            gf.update_bullets(aliens,bullets,ai_settings,screen,ship,stats,sb)
            gf.update_aliens(ai_settings,aliens,ship,screen,stats,bullets,sb)
        gf.update_screen(ai_settings,screen,ship,bullets,aliens,play_button,stats,sb)


run_game()