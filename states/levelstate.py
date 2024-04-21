from states.gamestate import GameState
from objects.tile import Tile
from objects.object import Object
from objects.occupier import Occupier
from objects.player import Player
import pygame


class LevelState(GameState):

    def __init__(self, game, controls):
        super().__init__(game)

        self.game = game
        self.controls = controls
        self.all_sprites = pygame.sprite.Group()
        self.tile_sprites = pygame.sprite.Group()
        self.occupier_sprites = pygame.sprite.Group()
        self.object_sprites = pygame.sprite.Group()

        self.parseLevel("./levels/level1.txt")

    def parseLevel(self, levelFile):

        self.tiles = {}
        i, j = 0, 0
        currentLayer = None

        with open(levelFile, 'r') as file:
            lines = file.readlines()
        for line in lines:
            line = line.strip()
            words = line.split()
            
            if not words:
                continue # Skip empty lines
            if words[0].lower() in ["tile", "occupier", "object"]:
                currentLayer = words[0].lower()
                i, j = 0, 0
                continue
            elif words[0].lower() == "end":
                break

            if currentLayer:
                i = 0
                for col in line:
                    if currentLayer == "tile":
                        self.tiles[(i, j)] = Tile(self.game, self.tiles, (i, j), col)
                    if currentLayer == "object" and col != '.':
                        self.tiles[(i, j)].add_obj(Object(self.game, self.tiles[(i, j)], col, (0, 255, 0)))
                    if currentLayer == "occupier" and col != '.':
                        if col == '@':
                            self.tiles[(i, j)].add_occ(Player(self.game, self.tiles[(i, j)], self.controls))
                        else:
                            self.tiles[(i, j)].add_occ(Occupier(self.game, self.tiles[(i, j)], col, (0, 0, 255)))
                    i += 1  # Move to the next block in the row
                j += 1  # Move to the next row


    def handleEvents(self, events):
        # pressed_keys = pygame.key.get_pressed()
        for event in events:
            pass

    def update(self):
        # pressed_keys = pygame.key.get_pressed()
        for tile in self.tiles.values():
            if tile.occupier is not None:
                tile.occupier.update()
        # updates secondary buffer?
        for tile in self.tiles.values():
            if tile.occupier is not None:
                tile.occupier.used = False
        for tile in self.tiles.values():
            if tile.object is not None:
                tile.object.update()
        for tile in self.tiles.values():
                    tile.update()

    def draw(self, surface):
        surface.fill((0, 0, 0))  # Clear screen with black
        for (i, j), tile in self.tiles.items():
            x, y = i * self.game.FONT_SIZE + self.game.offset, j * self.game.FONT_SIZE + self.game.offset
            tile.render(surface, (x, y))



        