from states.gamestate import GameState
from objects.tile import Tile
from objects.object import Object
from objects.occupier import Occupier
from objects.player import Player
import pygame
import heapq

# The LevelState class is a GameState that represents the state of the game when the player is playing a level.
# it contains game loop and level parsing logic
class LevelState(GameState):

    # initializes the LevelState with a reference to the game and the controls
    # also initializes the sprite groups for the tiles, occupiers, and objects
    def __init__(self, game, controls):
        super().__init__(game)

        self.game = game
        self.controls = controls
        self.all_sprites = pygame.sprite.Group()
        self.tile_sprites = pygame.sprite.Group()
        self.occupier_sprites = pygame.sprite.Group()
        self.object_sprites = pygame.sprite.Group()

        self.turn_queue = []
        self.turn_count = 0  # This will help in maintaining the stable ordering in the heap

        self.parseLevel("./levels/level1.txt")

    # pareses the given level file and creates the tiles, occupiers, and objects
    # adds tiles and relevant functions to the turn queue
    def parseLevel(self, levelFile):

        self.tiles = {}
        self.turn_queue = []
        i, j = 0, 0
        currentLayer = None

        with open(levelFile, 'r') as file:
            lines = file.readlines()
        for line in lines:
            line = line.strip()
            words = line.split()
            
            if not words:
                continue # Skip empty lines
            if words[0].lower() in ["tile", "occupier", "object", "gas"]:
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
                        self.turn_queue.append(self.tiles[(i, j)]) # adds tiles to turn queue
                    if currentLayer == "object" and col != '.':
                        self.tiles[(i, j)].add_obj(Object(self.game, self.tiles[(i, j)], col, (0, 255, 0)))
                    if currentLayer == "occupier" and col != '.':
                        if col == '@':
                            self.tiles[(i, j)].add_occ(Player(self.game, self.tiles[(i, j)], self.controls))
                            self.turn_queue.append(self.tiles[(i, j)].occupier) # adds player to turn queue
                        else:
                            self.tiles[(i, j)].add_occ(Occupier(self.game, self.tiles[(i, j)], col, (0, 0, 255)))
                    if currentLayer == "gas" and col != '.':
                        if col == 'g':
                            self.tiles[(i, j)].add_gas(col, 30)
                        if col == 'r':
                            self.tiles[(i, j)].add_gas(col, 30)
                        if col == 'b':
                            self.tiles[(i, j)].add_gas(col, 30)
                    i += 1  # Move to the next block in the row
                j += 1  # Move to the next row

    def handleEvents(self, events):
        pressed_keys = pygame.key.get_pressed()
        for event in events:
            pass

    def add_to_turn_queue(self, priority, action):
        self.turn_count += 1
        heapq.heappush(self.turn_queue, (priority, self.turn_count, action))

    def process_turns(self):
        if self.turn_queue:
            _, _, action = heapq.heappop(self.turn_queue)
            action()

    def update(self):
        pressed_keys = pygame.key.get_pressed()
        # turns
        self.process_turns() # processes one action per frame
        for tile in self.tiles.values():
            if tile.occupier:
                tile.occupier.update() # might modify state and re-add to queue


        # buffer updates
        for tile in self.tiles.values():
            if tile.occupier is not None:
                tile.occupier.move(tile.occupier.move_buffer) # passes move buffer because other things could move it
                tile.occupier.ac = tile.occupier.ac_max
            if tile.gas_total() > 0:
                for gas in tile.gasses:
                    if gas.amount > 0:
                        gas.move(gas.move_buffer)

    def draw(self, surface):
        surface.fill((0, 0, 0))  # Clear screen with black
        for (i, j), tile in self.tiles.items():
            x, y = i * self.game.FONT_SIZE + self.game.offset, j * self.game.FONT_SIZE + self.game.offset
            tile.render(surface, (x, y))



        