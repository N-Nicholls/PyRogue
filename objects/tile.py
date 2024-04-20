from objects.textsprite import TextSprite

class Tile():

    def __init__(self, game, position, char):
        self.occupier = None
        self.object = None
        self.position = position
        self.game = game
        self.tile = TextSprite(game, char, (255,255,255))

    def render(self, surface, position):
        to_render = self.tile
        if self.object is not None:
            to_render = self.object
        if self.occupier is not None:
            to_render = self.occupier
            
        to_render.set_position(position)
        to_render.draw(surface)
        
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
    
    def hasObj(self):
        if self.object is None:
            return False
        else:
            return True
        
    def hasOcc(self):
        if self.occupier is None:
            return False
        else:
            return True
