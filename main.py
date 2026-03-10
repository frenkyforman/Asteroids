
import pygame
import sys
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_RADIUS
from logger import log_state
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from logger import log_event
from circleshape import CircleShape


def main():
    print("Starting Asteroids with pygame version: VERSION")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    # Zorgt dat elke nieuwe Instance Object automatisch in deze groups komt
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)

    # Instances (wordt automatisch toegevoegd aan beide groups)
    player1 = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)
    asteroids_field = AsteroidField()

    dt = 0
    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        dt = clock.tick(60) / 1000

        # Update alle updatables
        updatable.update(dt)

        # collision check
        for obj in asteroids:
            if obj.collides_with(player1):
                log_event("player_hit")
                print ("Game over!")
                sys.exit()

        # Draw alle drawables
        screen.fill("black")
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()


if __name__ == "__main__":
    main()
