from objects.textsprite import TextSprite

class Object(TextSprite):
    def __init__(self, game, tile, char, color, font=None):
        self.tile = tile
        super(Object, self).__init__(game, char, color, font)
    
    def update(self):
        pass

    def return_subclass(self):
        return "object"