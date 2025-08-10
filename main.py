import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from astroid_field import AsteroidField
from shot import Shot

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Player.containers = (updatables, drawables)
    Asteroid.containers = (asteroids, updatables, drawables)
    AsteroidField.containers = (updatables)
    Shot.containers = (shots, updatables, drawables)

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()

    # infinite game loop:
    while(True):

        # check if user has closed the window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # update game
        updatables.update(dt)

        for a in asteroids:
            if a.is_colliding_with(player):
                print("Game over!")
                return
            
            for s in shots:
                if a.is_colliding_with(s):
                    a.split()
                    s.kill()
            

        # update screen
        screen.fill(BLACK)
        for d in drawables:
            d.draw(screen)

        pygame.display.flip()

        # update the clock (60 fps)
        dt = clock.tick(60) # milliseconds
        dt /= 1000 # seconds



if __name__ == "__main__":
    main()
