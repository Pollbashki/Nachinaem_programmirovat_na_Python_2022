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
MAX_WIDTH = WINDOW_WIDTH - BALL_WIDTH_HEIGHT
MAX_HEIGHT = WINDOW_HEIGHT - BALL_WIDTH_HEIGHT
TARGET_X = 400
TARGET_Y = 320
TARGET_WIDTH_HEIGHT = 120
N_PIXELS_TO_MOVE = 3

#3 – Инициализируем окружение pygame
pygame.init()
window = pygame.display.set_mode(size=(WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

#4 – Загружаем элементы: изображения, звуки и т. д.
ballImage = pygame.image.load('object_oriented_python_irv_kalb/chapter2/images/ball.png')
targetImage = pygame.image.load('object_oriented_python_irv_kalb/chapter2/images/target.jpg')

#5 – Инициализируем переменные
ballX = random.randrange(MAX_WIDTH)
ballY = random.randrange(MAX_HEIGHT)
ballRect = pygame.Rect(ballX, ballX, BALL_WIDTH_HEIGHT, BALL_WIDTH_HEIGHT)
targetRect = pygame.Rect(TARGET_X, TARGET_Y, TARGET_WIDTH_HEIGHT, TARGET_WIDTH_HEIGHT)

#6 – Бесконечный цикл
while True:
    #7 – Проверяем наличие событий и обрабатываем их
    for event in pygame.event.get():
        # Нажата кнопка "закрыть"? Выходим из pygame и завершаем программу
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #8 – Выполняем действия "в рамках фрейма"
    # Проверяем нажатия клавиш пользователем
    keyPressedTuple = pygame.key.get_pressed()

    if keyPressedTuple[pygame.K_LEFT]: # перемещаемся влево
        ballX = ballX - N_PIXELS_TO_MOVE

    if keyPressedTuple[pygame.K_RIGHT]: # перемещаемся вправо
        ballX = ballX + N_PIXELS_TO_MOVE

    if keyPressedTuple[pygame.K_UP]: # перемещаемся вверх
        ballY = ballY - N_PIXELS_TO_MOVE

    if keyPressedTuple[pygame.K_DOWN]: # перемещаемся вниз
        ballY = ballY + N_PIXELS_TO_MOVE
    
    # определяем, перекрывает ли мяч целевое изображение
    ballRect = pygame.Rect(ballX, ballY, BALL_WIDTH_HEIGHT, BALL_WIDTH_HEIGHT)

    if ballRect.colliderect(targetRect):
        print('Ball is touching the target')

    #9 – Очищаем окно
    window.fill(BLACK)

    #10 – Рисуем все элементы окна
    window.blit(targetImage, (TARGET_X, TARGET_Y))
    window.blit(source=ballImage, dest=(ballX, ballY))


    #11 – Обновляем окно
    pygame.display.update()

    #12 – Делаем паузу
    clock.tick(FRAMES_PER_SECOND)