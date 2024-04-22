import pygame
import pygame.font

class TextSprite(pygame.sprite.Sprite):
    def __init__(self, game, char, color, font=None):
        super().__init__()
        self.game = game
        self.used = False # ideally each thing with a textsprite should have a used if its attached to a tile
        if font is None:
            self.font = game.font
        else:
            self.font = font
        self.image = self.font.render(char, True, color)
        self.rect = self.image.get_rect()

    def set_position(self, position):
        self.rect.topleft = position

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    
