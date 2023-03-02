import pygame as pg

from settings import *


class Wall(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        # init sprite
        self.groups = game.all_sprites, game.walls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game

        # draw wall
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()

        # set position
        self.x = x
        self.y = y
        self.rect.x = x*TILESIZE
        self.rect.y = y*TILESIZE

    def update(self):
        pass