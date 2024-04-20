from objects.textsprite import TextSprite

class Object(TextSprite):
    def __init__(self, game, char, color, font=None):
        super(Object, self).__init__(game, char, color, font)