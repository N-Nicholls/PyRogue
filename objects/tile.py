from objects.textsprite import TextSprite
from objects.gas import Gas
import pygame

# Tile class that contains a floor, occupier, object, and gas list
# Contains methods to modify itself for things relating to tile, though the actual movement is handled
# by the object moving. The tile only has methods responsible for directly manipulating its own data.
# Note that for a gas to work it must be added to the tile at runtime. New gasses can't be added dynamically it's way too performance heavy
class Tile():

    # initializes the tile with a game reference, a tile list reference, a position, and a character
    # Note that the gas list must be initialized at runtime
    def __init__(self, game, tiles, position, char):
        self.occupier = None
        self.object = None

        self.gasses = [Gas(self, "g", (0, 200, 0), 0)]
        self.gasses.append(Gas(self, "r", (200, 0, 0), 0))
        self.gasses.append(Gas(self, "b", (0, 0, 200), 0))

        self.position = position
        self.game = game
        self.tiles = tiles
        self.floor = TextSprite(game, char, (255,255,255))

    # updates the gas objects in the tile. Will later handle liqud and other updates
    # NOTE: when turns are properly implemented, update should NOT handle turn dependent updates
    def update(self): # will do more updates later maybe, currently handles gas updates
        for gas in self.gasses:
            gas.update()

    # will later be for turn updates
    def turn_update(self):
        pass

    # returns the subclass of the object
    def return_subclass(self):
        return "tile"
  
    # renders the tile to the screen.
    # This renders only one surface according to a heirarchy with a gas overlay
    def render(self, surface, position):
        # Start with the base floor tile image
        rendered = False
        to_render = pygame.surface.Surface((self.game.FONT_SIZE, self.game.FONT_SIZE))

        # Add 20% of each gas color to the background of the to_render surface
        for gas in self.gasses:
            if gas.amount > 0:
                # Calculate the semi-transparent overlay color based on the gas amount
                overlay_color = tuple(min(255, int(c + 0.2 * gas.amount * gc)) for c, gc in zip((10, 10, 10), gas.color))
                
                # Create a semi-transparent surface with the gas color
                gas_overlay = pygame.Surface(to_render.get_size(), pygame.SRCALPHA)
                gas_overlay.fill(overlay_color + (int(255 * 0.2),))  # (R, G, B, A)

                # Blit the gas color onto the to_render surface
                to_render.blit(gas_overlay, (0, 0), special_flags=pygame.BLEND_RGBA_ADD)
    
        # Add the occupier or object image or tile image to the to_render surface
        if self.occupier is not None:
            to_render.blit(self.occupier.image, (0, 0))  # Assuming occupier also has an 'image' attribute
            rendered = True
        if self.object is not None and not rendered:
            to_render.blit(self.object.image, (0, 0))  # Assuming object also has an 'image' attribute
            rendered = True
        if not rendered:
            to_render.blit(self.floor.image, (0, 0))  # Assuming floor also has an 'image' attribute
           
        # Set position and draw the final composed surface onto the main surface
        self.floor.set_position(position)  # Assumes set_position is adjusting the internal state for drawing
        surface.blit(to_render, position)

    # returns the total amount of gas in the tile
    def gas_total(self):
        temp = 0
        for gas in self.gasses:
            temp += gas.amount
        return temp  

    # adds gas to the tile. Assumes gas is already in the tile's gas list
    def add_gas(self, type, amt):
        for gas in self.gasses:
            if gas.type == type:
                gas.amount += amt
                return
        raise Exception("No gas of type " + type + " found")

    # removes gas from the tile. Assumes gas is already in the tile's gas list
    def remove_gas(self, type, amt):
        for gas in self.gasses:
            if gas.type == type:
                gas.amount -= amt
                return
        raise Exception("No gas of type " + type + " found")

    # adds an object to the tile. Assumes function won't be passed to an occupied tile
    def add_obj(self, object):
        if self.object is None:
            self.object = object
            return
        raise Exception("Tile already contains object")

    # removes an object from the tile and returns it. Assumes function won't be passed to an empty tile
    def remove_obj(self):
        if self.object is None:
            raise Exception("No object") 
        temp = self.object
        self.object = None
        return temp
    
    # adds an occupier to the tile. Assumes function won't be passed to an occupied tile
    def add_occ(self, occupier):
        if self.occupier is None:
            self.occupier = occupier
            return
        raise Exception("Tile already occupied")
    
    # removes an occupier from the tile and returns it. Assumes function won't be passed to an empty tile
    def remove_occ(self):
        if self.occupier is None:
            raise Exception("No occupier")
        temp = self.occupier
        self.occupier = None
        return temp

    # checks if the tile has an object
    def has_obj(self):
        if self.object:
            return True
        return False

    # checks if the tile has an occupier    
    def has_occ(self):
        if self.occupier:
            return True
        return False      
