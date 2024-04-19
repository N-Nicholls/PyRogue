import pygame

class TextSprite(pygame.sprite.Sprite):
    def __init__(self, game, char, color, position):
        super().__init__()
        self.image = game.font.render(char, True, color)
        self.rect = self.image.get_rect(topleft=position)
