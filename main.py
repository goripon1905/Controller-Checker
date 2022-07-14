# coding: utf-8
# coding=utf-8
# -*- coiding: utf-8 -*-

import pygame
from pygame.locals import *
import time

pygame.joystick.init()

try:
    joy = pygame.joystick.Joystick(0)
    joy.init()
    print('コントローラー名: ' + joy.get_name())
    print('ボタン数：' + str(joy.get_numbuttons()))
except pygame.error:
    print('コントローラーが見つかりません')

def main():
    mid_x = 500 / 2
    mid_y = 500 / 2
    pygame.init()
    screen = pygame.display.set_mode((500,500))
    pygame.display.set_caption('コントローラーチェッカー')
    pygame.display.flip()
    x0 = 0
    y0 = 0
    x1 = 0
    y1 = 0

    while True:
        pygame.display.update()
        pygame.time.wait(30)
        pygame.draw.circle(screen, (0, 200, 0), (int(mid_x), int(mid_y)), 5)
        for e in pygame.event.get():
            if e.type == KEYDOWN and e.key == K_ESCAPE:
                return
            if e.type == pygame.locals.JOYAXISMOTION:
                x1, y1 = joy.get_axis(0), joy.get_axis(1)
                break
            if x0 != 0 and y0 != 0:
                print("入力値：" + str(x0) + " " + str(y0))
                mid_x += x0
                mid_y += y0
            if x0 == 0 and y0 == 0:
                print("入力値c：" + str(x0) + " " + str(y0))
            if e.type == pygame.locals.JOYBALLMOTION:
                print('ball motion')
            elif e.type == pygame.locals.JOYHATMOTION:
                print('hat motion')
            elif e.type == pygame.locals.JOYBUTTONDOWN:
                print(str(e.button) + '番目のボタンが押されました')
            elif e.type == pygame.locals.JOYBUTTONUP:
                print(str(e.button) + '番目のボタンが離されました')
        if x0 == x1 and y0 == y1:
            mid_x += x0
            mid_y += y0
        else:
            x0 = x1
            y0 = y1


if __name__ == '__main__':
    main()