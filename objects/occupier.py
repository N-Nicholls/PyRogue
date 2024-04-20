from objects.textsprite import TextSprite

class Occupier(TextSprite):
    def __init__(self, game, char, color, font=None):
        super(Occupier, self).__init__(game, char, color, font)