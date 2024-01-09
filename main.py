import pygame as pg
from random import randrange

WINDOW = 1000
screen = pg.display.set_mode([WINDOW] * 2)
clock = pg.time.Clock()

#refreshes the screan 
while True:
    for event in pg.event.get():
        #if the user quits the game, it exits
        if event.type == pg.QUIT:
            exit()
    #otherwise fill screen
    screen.fill('black')
    pg.display.flip()
    clock.tick(60)