import pygame,random,sys


def run_game():
    pygame.init()
    screen = pygame.display.set_mode((1000, 800))
    alien_image = pygame.image.load('/Users/zhoujessie/Desktop/Jie-sPython/lib/GameMaker/images/alien.bmp')
    alien_image_rect = alien_image.get_rect()
    screen_rect = screen.get_rect()
    alien_width=alien_image_rect.width
    def car(x, y):
        screen.blit(alien_image, (x, y))

    alien_max_x = 1000 - alien_image_rect.width
    y = -alien_image_rect.height
    bg_color=(230,230,230)
    speed=12

    def move_car(y):
        y+=speed
        return y

    clock=pygame.time.Clock()
    while True:
        screen.fill(bg_color)
        y=move_car(y)
        car(alien_width,y)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        pygame.display.update()
        clock.tick(22)
run_game()
