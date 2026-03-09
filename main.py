import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state


def main():
    print("Starting Asteroids with pygame version: VERSION")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        log_state()
        dt = clock.tick() / 1000
        clock.tick(60)
        for event in pygame.event.get():
            screen.fill("black")
            if event.type == pygame.QUIT:
                return
            pygame.display.flip()

if __name__ == "__main__":
    main()
