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
        self.parseLevel("./levels/level1.txt")

    # pareses the given level file and creates the tiles, occupiers, and objects.
    # creates tile objects in a list and adds objects and occupiers to the tiles.
    # also adds occupiers and objects to their respective lists. This mirrors pygame group logic but
    # lets me call specific object updates, not necessarily all at once like group.update()
    # for gas it simply adds the amount of gas to the tile, but doesn't create a gas object.
    def parseLevel(self, levelFile):

        self.tiles = {}
        self.occupiers = []
        self.objects = []
        # self.player = []

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
                    if currentLayer == "object" and col != '.':
                        self.tiles[(i, j)].add_obj(Object(self.game, self.tiles[(i, j)], col, (0, 255, 0)))
                        self.objects.append(self.tiles[(i, j)].object)
                    if currentLayer == "occupier" and col != '.':
                        if col == '@':
                            self.tiles[(i, j)].add_occ(Player(self.game, self.tiles[(i, j)], self.controls))
                            # self.player.append(self.tiles[(i, j)].occupier)
                            self.occupiers.append(self.tiles[(i, j)].occupier)
                        else:
                            self.tiles[(i, j)].add_occ(Occupier(self.game, self.tiles[(i, j)], col, (0, 0, 255)))
                            self.occupiers.append(self.tiles[(i, j)].occupier)
                    if currentLayer == "gas" and col != '.':
                        if col == 'g':
                            self.tiles[(i, j)].add_gas(col, 30)
                        if col == 'r':
                            self.tiles[(i, j)].add_gas(col, 30)
                        if col == 'b':
                            self.tiles[(i, j)].add_gas(col, 30)
                    i += 1  # Move to the next block in the row
                j += 1  # Move to the next row

    # handles the events for the level state
    def handleEvents(self, events):
        pressed_keys = pygame.key.get_pressed()
        for event in events:
            pass

    # game turn independent tile updates
    # note that occupier is a member of tiles and could be called in the self.tiles.values() loop but 
    # I'm keeping it separate for clarity and to show their updates are independent.
    # This might increase overhead though.
    # Also, this will update all the gasses and then all the occupiers, which is good.
    def buffer_update(self):
        # occupier updates
        for occupier in self.occupiers:
            if occupier is not None:
                occupier.move(occupier.move_buffer) # passes move buffer because other things can call move function requiring a pos argument
        # gas updates
        for tile in self.tiles.values(): # will later handle lights, liquids, sprite animations, etc.
            for gas in tile.gasses:
                if gas.amount > 0:
                    gas.move(gas.move_buffer)

    # TODO game turn dependent tile updates
    def turn_update(self):
        for occupier in self.occupiers: # NOT PROPERLY IMPLEMENTED
            occupier.update()
        for tile in self.tiles.values(): # will later handle liquid updates and fire updates etc, maybe
            tile.update()

    # called once per frame, updates object turns and buffer updates
    # TODO: see turn_update()
    def update(self):
        pressed_keys = pygame.key.get_pressed()
        self.turn_update()
        self.buffer_update()
        

    # doesn't draw using groups, but by calling tiles internal render function
    def draw(self, surface):
        surface.fill((0, 0, 0))  # Clear screen with black
        for (i, j), tile in self.tiles.items():
            x, y = i * self.game.FONT_SIZE + self.game.offset, j * self.game.FONT_SIZE + self.game.offset # Calculate the position of the tile based on index, so resolution is independent from logic
            tile.render(surface, (x, y))



        