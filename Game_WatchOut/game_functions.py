import pygame,random,sys,time
from Game_WatchOut.alien import Alien
from Game_WatchOut.button import Button
from Game_WatchOut.gift import Gift

def check_key_down_events(event,ship,setting,score):
    if event.key == pygame.K_LEFT:
        ship.moving_left=True
    if event.key == pygame.K_RIGHT:
        ship.moving_right=True
    if event.key == pygame.K_UP:
        ship.moving_up = True
    if event.key == pygame.K_DOWN:
        ship.moving_down = True
    if event.key == pygame.K_q:
        pygame.quit()
    if event.key == pygame.K_1 and setting.pause==False and score.life_number >=1:
        pause_music()
        pygame.mouse.set_visible(True)
        setting.active=False
        setting.pause=True
    elif event.key == pygame.K_1 and setting.pause==True and score.life_number >=1:
        unpause_music()
        pygame.mouse.set_visible(False)
        setting.active=True
        setting.pause = False
    if event.key == pygame.K_SPACE:
        setting.start=True


def check_key_up_events(event,ship):
    if event.key == pygame.K_LEFT:
        ship.moving_left=False
    if event.key == pygame.K_RIGHT:
        ship.moving_right=False
    if event.key == pygame.K_UP:
        ship.moving_up = False
    if event.key == pygame.K_DOWN:
        ship.moving_down = False

def check_keyboard_events(ship,button,setting,score):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYUP:
            check_key_up_events(event,ship)
        if event.type==pygame.MOUSEBUTTONDOWN:
            button.mouse_x,button.mouse_y=pygame.mouse.get_pos()
        if event.type == pygame.KEYDOWN:
            check_key_down_events(event, ship, setting,score)


def reset_alien_pos(alien,setting):
    alien.rect.y = 0
    alien.rect.x=random.randint(0,setting.screen_width-alien.rect.width)

def check_alien_disappear(aliens,setting):
    for alien in aliens:
        if alien.rect.top >= setting.screen_height:
           reset_alien_pos(alien,setting)

def number_of_alien(setting,screen):
    alien=Alien(screen,setting)
    number=round((setting.screen_width-10)/(1.3*alien.rect.width))
    return number

def check_alien_ship_collision(aliens,ships,score,setting,hit_sound):
    collision=pygame.sprite.groupcollide(ships,aliens,False,True)
    if collision:
        play_sound(hit_sound)
        if score.life_number >1:
            score.life_number-=1
            score.prep_ship()
        elif score.life_number==1:
            score.life_number -= 1
            setting.active=False
            setting.start=False
            stop_music()

def create_alien_fleet(aliens,screen,setting):
    for number in range(number_of_alien(setting,screen)):
        alien=Alien(screen,setting)
        alien.rect.x=round(1.2*alien.rect.width*number)
        alien.rect.y=-(random.randint(1,35)*alien.height)
        aliens.add(alien)

def show_button(setting,screen):
    button=Button(setting,screen)
    button.draw_button()

def show_pause_button(button,setting,score):
    if setting.active==False and setting.pause==True and score.life_number >=1:
        button.draw_pause_button()

def check_play_button_clicked(ship,button,setting,score,aliens):
    check_keyboard_events(ship, button, setting, score)
    play=(setting.start and setting.active==False and setting.pause==False)
    if play or button.rect.collidepoint(button.mouse_x,button.mouse_y):
        play_music()
        setting.active=True
        setting.gift_number=0
        tstart=time.time()
        reset(score,ship,aliens,setting)
        button.mouse_x, button.mouse_y = 0, 0
        return tstart,30

def update_aliens(aliens):
    for alien in aliens:
        alien.move()

def score(tstart,score):
    t_now=time.time()
    t_passed=t_now-tstart
    score.score=t_passed
    score.prep_score()
    score.prep_best_score()

def create_gift(gifts,screen,setting,score):
    if score.score >25 and setting.active==True and score.life_number >=1 and random.randint(0,80) > 77:
        gift=Gift(screen,setting)
        gifts.add(gift)


def gift(gifts, screen, setting, score,ships):
    create_gift(gifts, screen, setting, score)
    gifts.update()
    check_gift_ship_collision(gifts, ships, setting,score)
    check_gift_disappear(gifts)
    life_increase(score, setting)
    clear_gift(setting)

def check_gift_disappear(gifts):
    for gift in gifts.copy():
        if gift.rect.top > gift.screen_rect.bottom:
            gifts.remove(gift)

def check_gift_ship_collision(gifts,ships,setting,score):
    collision=pygame.sprite.groupcollide(ships,gifts,False,True)
    if collision and score.life_number >0 and setting.active==True:
        setting.gift_number+=1


def life_increase(score,setting):
    if setting.gift_number>=5 and 8 > score.life_number > 0:
        score.life_number+=1
    elif setting.gift_number>=5 and score.life_number > 8:
        score.score+=10

def clear_gift(setting):
    if setting.gift_number>=5:
        setting.gift_number=0

def check_best_score(score):
    if score.best_score < score.score:
        score.best_score=score.score
        score.prep_best_score()

def reset(score,ship,aliens,setting):
    score.life_number=setting.life
    ship.rect.bottom = ship.screen_rect.bottom - 10
    ship.rect.centerx = ship.screen_rect.centerx
    score.score=0
    aliens.empty()
    setting.alien_speed=15

def check_score(score,t):
    if t is not None:
        if score.score >=120 and score.score in list(range(0,500,10)):
            t+=0.25
            return t
        else:
            return t
    else:
        return 30

def play_music():
    pygame.mixer.music.play(-1)

def stop_music():
    pygame.mixer.music.stop()

def pause_music():
    pygame.mixer.music.pause()

def unpause_music():
    pygame.mixer.music.unpause()

def play_sound(hit_sound):
    pygame.mixer.Sound.play(hit_sound)


def speed_up(setting,score):
    list_=list(range(0,1000,15))+[12,21,31,55]
    if score.score > 0 and score.score in list_:
        setting.alien_speed+=1

def check_aliens_empty(aliens,screen,setting):
    if len(aliens)==0:
        create_alien_fleet(aliens, screen, setting)


