from core.game import Game
import pygame


if __name__ == "__main__":
    pyrogue = Game()
    pyrogue.run()
    pyrogue.quit()

    for str in pygame.font.get_fonts():
        print(str)