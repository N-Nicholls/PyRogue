# default gamestate class, maybe add more later
class GameState():
    def __init__(self, game):
        self.game = game
    
    def handleEvents(self):
        raise NotImplementedError
    
    def update(self):
        raise NotImplementedError

    def draw(self, screen): # doesn't always need screen, but I'll pass it regardless
        raise NotImplementedError