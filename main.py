import pygame
import player

from constants import SCREEN_HEIGHT, SCREEN_WIDTH 
from logger import log_state
from player import Player

def main():
    print("Starting Asteroids with pygame version: VERSION")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    fps = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            pass
        screen.fill("black")
        player.update(dt)
        player.draw(screen)
        pygame.display.flip()
        tick_value = fps.tick(60)
        dt = tick_value / 1000
        
        


if __name__ == "__main__":
    main()
