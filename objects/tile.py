from objects.textsprite import TextSprite
from objects.gas import Gas
import pygame

class Tile():

    def __init__(self, game, tiles, position, char):
        self.occupier = None
        self.object = None

        self.gasses = [Gas(self, "g", (0, 200, 0), 0)]
        self.gasses.append(Gas(self, "r", (200, 0, 0), 0))
        self.gasses.append(Gas(self, "b", (0, 0, 200), 0)) # will be a list later

        self.position = position
        self.game = game
        self.tiles = tiles
        self.floor = TextSprite(game, char, (255,255,255))

    def update(self): # will do more updates later maybe, currently handles gas updates
        for gas in self.gasses:
            gas.update()
            self.game.state.increment_current()

    def return_subclass(self):
        return "tile"

    
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

    def gas_total(self):
        temp = 0
        for gas in self.gasses:
            temp += gas.amount
        return temp  

    def add_gas(self, type, amt=1):
        for gas in self.gasses:
            if gas.type == type:
                gas.amount += amt
    
    def remove_gas(self, type, amt=1):
        for gas in self.gasses:
            if gas.type == type:
                gas.amount -= amt
                return
        print("No gas of type " + type + " found")

    def add_obj(self, object):
        if self.object is None:
            self.object = object
        else:
            print("Tile already contains object")

    def remove_obj(self):
        if self.object is None:
            print("No object")
            return 
        temp = self.object
        self.object = None
        return temp
    
    def add_occ(self, occupier):
        if self.occupier is None:
            self.occupier = occupier
        else:
            print("Tile already occupied")
    
    def remove_occ(self):
        if self.occupier is None:
            print("No occupier")
            return
        temp = self.occupier
        self.occupier = None
        return temp
    
    def has_obj(self):
        if self.object is None:
            return False
        else:
            return True
        
    def has_occ(self):
        if self.occupier is None:
            return False
        else:
            return True       
