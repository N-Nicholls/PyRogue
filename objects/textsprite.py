import pygame
import pygame.font

# TextSprite class that inherits from pygame.sprite.Sprite
# Contains a font, image, and rect attribute. No font given will default to game font
class TextSprite(pygame.sprite.Sprite):
    def __init__(self, game, char, color, font=None):
        super().__init__()
        self.game = game
        if font is None:
            self.font = game.font
        else:
            self.font = font
        self.image = self.font.render(char, True, color)
        self.rect = self.image.get_rect()

    # Set position function that takes a position as an argument. Useful because resolution can change
    def set_position(self, position):
        self.rect.topleft = position

    # Draw function that takes a surface as an argument. Blits the image onto the surface
    def draw(self, surface):
        surface.blit(self.image, self.rect)

    
