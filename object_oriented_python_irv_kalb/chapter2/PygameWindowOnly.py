# pygame демо 0 – только окно

#1 – Импортируем пакеты
import pygame
from pygame.locals import *
import sys

import random

#2 – Определяем константы
BLACK = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30
BALL_WIDTH_HEIGHT = 100
N_PIXELS_PER_FRAME = 3

#3 – Инициализируем окружение pygame
pygame.init()
window = pygame.display.set_mode(size=(WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

#4 – Загружаем элементы: изображения, звуки и т. д.
ballImage = pygame.image.load('object_oriented_python_irv_kalb/chapter2/images/ball.png')

#5 – Инициализируем переменные
ballRect = ballImage.get_rect()
MAX_WIDTH = WINDOW_WIDTH - ballRect.width
MAX_HEIGHT = WINDOW_HEIGHT - ballRect.height
ballRect.left = random.randrange(MAX_WIDTH)
ballRect.top = random.randrange(MAX_HEIGHT)
xSpeed = N_PIXELS_PER_FRAME
ySpeed = N_PIXELS_PER_FRAME

#6 – Бесконечный цикл
while True:
    #7 – Проверяем наличие событий и обрабатываем их
    for event in pygame.event.get():
        # Нажата кнопка "закрыть"? Выходим из pygame и завершаем программу
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #8 – Выполняем действия "в рамках фрейма"

    if (ballRect.left < 0) or (ballRect.right >= WINDOW_WIDTH):
        xSpeed = -xSpeed # обращаем направление Х

    if (ballRect.top < 0) or (ballRect.bottom >= WINDOW_HEIGHT):
        ySpeed = -ySpeed # обращаем направление Y

    # обновляем местоположение мяча, используя скорость в двух
    # направлениях
    
    ballRect.left = ballRect.left + xSpeed
    ballRect.top = ballRect.top + ySpeed

    #9 – Очищаем окно
    window.fill(BLACK)

    #10 – Рисуем все элементы окна
    window.blit(ballImage, ballRect)


    #11 – Обновляем окно
    pygame.display.update()

    #12 – Делаем паузу
    clock.tick(FRAMES_PER_SECOND)