import pygame
# Метод init() инициализирует игру. Должен всегда идти в самом начале кода игры
pygame.init()
# Далее задаём параметры экрана
# с помощью параметра flags= можно убрать оконный режим
screen = pygame.display.set_mode((600, 300))#, flags=pygame.NOFRAME)
# Даём название нашему приложению
pygame.display.set_caption("GameDev у Кири и Вани")
# Задаём иконку для приложения
icon = pygame.image.load('images/flash.png')
pygame.display.set_icon(icon)
# бесконечный цикл обновляющий экран
running = True
while running:
    # Делаем фон цветным
    # screen.fill((187, 11, 41))
    # Так мы можем обновлять дисплей
    pygame.display.update()
    # Делаем цикл, перебирающий все события происходящие в pygame
    # С его помощью прописываем строки кода для закрытия программы из самой программы
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        # Учимся менять цвет задника нажатием клавиши
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                screen.fill((220, 91, 113))
            elif event.key == pygame.K_r:
                screen.fill((187, 11, 41))
            elif event.key == pygame.K_b:
                screen.fill((0, 188, 225))