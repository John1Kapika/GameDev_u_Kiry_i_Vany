import pygame
# делаем задержку в анимации
clock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode((1280, 720))#, flags=pygame.NOFRAME)
pygame.display.set_caption("GameDev у Кири и Вани")
icon = pygame.image.load('images/flash.png')
pygame.display.set_icon(icon)
# Делаем задник
bg = pygame.image.load('images/zad.png')
# Делаем анимацию
walk_right = [
    pygame.image.load('images/player_right/player1.png'),
    pygame.image.load('images/player_right/player2.png'),
    pygame.image.load('images/player_right/player3.png'),
    pygame.image.load('images/player_right/player4.png'),
    pygame.image.load('images/player_right/player5.png'),
    pygame.image.load('images/player_right/player6.png'),
    pygame.image.load('images/player_right/player7.png'),
    pygame.image.load('images/player_right/player8.png')
]
walk_left = [
    pygame.image.load('images/player_left/player1.png'),
    pygame.image.load('images/player_left/player2.png'),
    pygame.image.load('images/player_left/player3.png'),
    pygame.image.load('images/player_left/player4.png'),
    pygame.image.load('images/player_left/player5.png'),
    pygame.image.load('images/player_left/player6.png'),
    pygame.image.load('images/player_left/player7.png'),
    pygame.image.load('images/player_left/player8.png')
]

player_anim_count = 0
# Делаем динамичный задний фон
bg_x = 0
# Делаем музыку на фоне
bg_sound = pygame.mixer.Sound('sounds/bluz.mp3')
bg_sound.play(-1)
running = True
while running:

    screen.blit(bg, (bg_x, 0))
    screen.blit(bg, (bg_x + 1280, 0))
    screen.blit(walk_right[player_anim_count], (100, 500))
    if player_anim_count == 7:
        player_anim_count = 0
    else:
        player_anim_count += 1
    # делаем динамичный задник
    bg_x -= 3
    # Делаем задник бесконечным
    if bg_x == -1280:
        bg_x = 0

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
    # слоу мо
    clock.tick(10)