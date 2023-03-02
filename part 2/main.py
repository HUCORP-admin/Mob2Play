"""
MOB2PLAY

Description: A Tile-based 2 player shooter created in Pygame
Author: HUCORP
"""

import pygame as pg
import sys

from os import path

from player import Player
from obstacles import Wall
from tilemap import Map
from settings import *


class Game:
    def __init__(self):
        # initialize pygame
        pg.init()

        # set the screen
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)

        # game control
        self.clock = pg.time.Clock()
        pg.key.set_repeat(500, 10)

        self.load()

    def load(self):
        game_dir = path.dirname(__file__)
        self.map = Map(path.join(game_dir, 'map.txt'))

    def new_instance(self):
        # create a new game
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()

        # create sprites
        for row, tiles in enumerate(self.map.data):
            for col, tile in enumerate(tiles):
                if tile == '*':
                    Wall(self, col, row)
                elif tile == 'P':
                    self.player = Player(self, col, row)

    def run(self):
        # game loop
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS)/1000
            self.events()
            self.update()
            self.draw()

    def quit(self):
        pg.quit()
        sys.exit()

    def update(self):
        # update items in game loop
        self.all_sprites.update()

    def events(self):
        # handle events in game loop
        for e in pg.event.get():
            if e.type == pg.QUIT:
                self.quit()
            if e.type == pg.KEYDOWN:
                if e.key == pg.K_LEFT:
                    self.player.move(dx=-1)
                if e.key == pg.K_RIGHT:
                    self.player.move(dx=1)
                if e.key == pg.K_DOWN:
                    self.player.move(dy=1)
                if e.key == pg.K_UP:
                    self.player.move(dy=-1)

    def draw_grid(self):
        for x in range(0, WIDTH, TILESIZE):
            pg.draw.line(self.screen, BLACK, (x,0), (x,HEIGHT))

        for y in range(0, HEIGHT, TILESIZE):
            pg.draw.line(self.screen, BLACK, (0,y), (WIDTH, y))

    def draw(self):
        # draw items in game loop
        self.screen.fill(TAN)
        self.draw_grid()
        self.all_sprites.draw(self.screen)


        # flip display after drawing
        pg.display.flip()


if __name__ == "__main__":
    g = Game()

    while True:
        g.new_instance()
        g.run()