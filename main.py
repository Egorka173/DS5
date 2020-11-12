import pygame
import random
import sys
import os
import time

os.environ['SDL_VIDEO_WINDOW_POS'] = '0,0'

pygame.init()

FPS = 60
clock = pygame.time.Clock()

Info = pygame.display.Info()
W, H = Info.current_w, Info.current_h

MAX_SNOW = 150
BG_COLOR = (143, 78, 157)


class Snow(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
# Определяем параметры снежинки
        self.speed = random.randint(1, 3)
        self.img_num = random.randint(1, 2)
        self.size = random.randint(32, 64)
        self.image_filename = f'snowflake{self.img_num}.png'
        self.image_orig = pygame.image.load(self.image_filename)
        self.image_orig = pygame.transform.scale(self.image_orig, (self.size, self.size))
        self.image = self.image_orig.copy()
        self.rect = self.image.get_rect(center=(x, y))

        self.rot = 0
        self.angle = random.randint(-1, 1)


def check_for_exit():
    for e in pygame.event.get():
        if e.type == pygame.QUIT or e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
            sys.exit(0)


'________________________________________MAIN_________________________________'
pygame.display.set_icon(pygame.image.load('snow.ico'))
pygame.display.set_caption('SNOW')
screen = pygame.display.set_mode((W, H))


def init_snow(max_snow):
    for _ in range(max_snow):
        snowgroup.add(Snow(random.randint(0, W), random.randint(0, H)))


snowgroup = pygame.sprite.Group()
init_snow(MAX_SNOW)


while True:
    check_for_exit()
    snowgroup.update()
    snowgroup.draw(screen)
    pygame.display.update()
    clock.tick(FPS)
