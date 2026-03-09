import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, LINE_WIDTH, PLAYER_RADIUS
from logger import log_state
from player import Player


def main():
    print("Starting Asteroids with pygame version: VERSION")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player1 = Player((SCREEN_WIDTH / 2),(SCREEN_HEIGHT / 2),PLAYER_RADIUS)

    while True:
        log_state()
        dt = clock.tick() / 1000
        clock.tick(60)
        for event in pygame.event.get():
            screen.fill("black")
            player1.draw(screen)
            if event.type == pygame.QUIT:
                return
            pygame.display.flip()
    

if __name__ == "__main__":
    main()
