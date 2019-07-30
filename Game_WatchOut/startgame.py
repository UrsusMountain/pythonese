import pygame,time
from Game_WatchOut.setting import Setting
from pygame.sprite import Group
from Game_WatchOut.ship import Ship
from Game_WatchOut import game_functions as gf
from Game_WatchOut.score import Score
from Game_WatchOut.button import Button
from Game_WatchOut.gift_show import GiftShow


def run_game():
    pygame.init()
    setting=Setting()
    screen = pygame.display.set_mode((setting.screen_width, setting.screen_height),pygame.RESIZABLE)
    pygame.display.set_caption("Watch Out!")
    gameIcon=pygame.image.load('images/dark.bmp')
    pygame.display.set_icon(gameIcon)
    aliens=Group()
    hit_sound=pygame.mixer.Sound('sound/sound.wav')
    pygame.mixer.music.load('sound/bg.mp3')
    ship=Ship(screen)
    clock=pygame.time.Clock()
    gf.create_alien_fleet(aliens,screen,setting)
    score=Score(setting,screen)
    ships=Group()
    ships.add(ship)
    button=Button(setting,screen)
    gifts=Group()
    giftshow=GiftShow(screen,setting)
    #t=30
    while True:
        screen.fill(setting.bg_color)
        tstart=gf.check_play_button_clicked(ship, button, setting,score,aliens)
        gf.show_pause_button(button,setting,score)
        giftshow.prep_gift()
        if tstart:
            start=tstart[0]
            #t=tstart[1]
        if setting.active:
            pygame.mouse.set_visible(False)
            gf.gift(gifts, screen, setting, score, ships)
            gf.check_aliens_empty(aliens,screen,setting)
            gf.speed_up(setting,score)
            gf.update_aliens(aliens)
            gf.check_alien_disappear(aliens,setting)
            ship.update_pos(setting)
            t_passed=round((time.time()-start),2)
            score.score=t_passed
            score.prep_score()
            gf.check_best_score(score)
            gf.speed_up(setting,score)
        else:
            if not setting.pause:
                gf.show_button(setting, screen)
                pygame.mouse.set_visible(True)
        score.prep_ship()
        gf.check_alien_ship_collision(aliens,ships,score,setting,hit_sound)
        score.show()
        aliens.draw(screen)
        ships.draw(screen)
        gifts.draw(screen)
        giftshow.blitme()
        pygame.display.update()
        #t=gf.check_score(score,t)
        clock.tick(200)
        #print(t)
        print(setting.alien_speed)

run_game()
