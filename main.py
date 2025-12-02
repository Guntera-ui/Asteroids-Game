import pygame

from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state
from player import Player


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    x = SCREEN_WIDTH // 2
    y = SCREEN_HEIGHT // 2
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    player = Player(x, y)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        log_state()
        updatable.update(dt)
        
        screen.fill("black")
        
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()
        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
