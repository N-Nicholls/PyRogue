from states.gamestate import GameState
from objects.textsprite import TextSprite
import pygame


class LevelState(GameState):

    def __init__(self, game, controls):
        super().__init__(game)

        self.game = game
        self.all_sprites = pygame.sprite.Group()
        self.controls = controls

        self.parseLevel()

    def parseLevel(self):
        # Example of creating text sprites
        # Position calculations here assume each character fits in a grid cell of size FONT_SIZE x FONT_SIZE
        symbols = [('@', (255, 0, 0), (50, 50)),  # Player
                ('#', (0, 255, 0), (70, 50)),  # Wall
                ('.', (0, 0, 255), (90, 50))]  # Floor

        for char, color, pos in symbols:
            sprite = TextSprite(self.game, char, color, pos)
            self.all_sprites.add(sprite)

    def handleEvents(self, events):
        pressed_keys = pygame.key.get_pressed()
        for event in events:
            pass

    def update(self):
        pressed_keys = pygame.key.get_pressed()
        pass

    def draw(self, surface):
        surface.fill((0, 0, 0))  # Clear screen with black
        self.all_sprites.draw(surface)  # Draw all sprites



        