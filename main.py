import pygame as pg
from constants import *

black = (0,0,0)


def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pg.init()
    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # infinite game loop:
    while(True):

        # check if user has quit
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
        
        # otherwise update screen
        screen.fill(black)
        pg.display.flip()



if __name__ == "__main__":
    main()
