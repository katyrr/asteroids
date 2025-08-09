import pygame as pg
from constants import *
from player import Player

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pg.init()
    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pg.time.Clock()
    dt = 0

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    # infinite game loop:
    while(True):

        # check if user has closed the window
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
        
        # update game
        player.update(dt)

        # update screen
        screen.fill(BLACK)
        player.draw(screen)

        pg.display.flip()

        # update the clock (60 fps)
        dt = clock.tick(60) # milliseconds
        dt /= 1000 # seconds



if __name__ == "__main__":
    main()
