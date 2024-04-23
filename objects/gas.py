import random
import math

class Gas():
    def __init__(self, game, tile, type, color, amt):
        self.tile = tile
        self.amount = amt
        self.move_buffer = None
        self.color = color
        self.type = type # renaming of char. Note that gas doesn't ever render and thus might not need to be a textsprite
        self.steepness = 1

    def return_subclass(self):
        return "gas"
    
    
    def update(self):
        movement = random.randint(1, 9)
        match movement:
            case 1: # left
                if self.canMove((self.tile.position[0]-1, self.tile.position[1])):
                    self.move_buffer = (self.tile.position[0]-1, self.tile.position[1])
            case 2: # right
                if self.canMove((self.tile.position[0]+1, self.tile.position[1])):
                    self.move_buffer = (self.tile.position[0]+1, self.tile.position[1])
            case 3: # up
                if self.canMove((self.tile.position[0], self.tile.position[1]-1)):
                    self.move_buffer = (self.tile.position[0]-1, self.tile.position[1]-1)
            case 4: # down
                if self.canMove((self.tile.position[0], self.tile.position[1]+1)):
                    self.move_buffer = (self.tile.position[0]-1, self.tile.position[1]+1)
            case 5: # upleft
                if self.canMove((self.tile.position[0]-1, self.tile.position[1]-1)):
                    self.move_buffer = (self.tile.position[0]-1, self.tile.position[1]-1)
            case 6: # upright
                if self.canMove((self.tile.position[0]+1, self.tile.position[1]-1)):
                    self.move_buffer = (self.tile.position[0]+1, self.tile.position[1]-1)
            case 7: # downleft
                if self.canMove((self.tile.position[0]-1, self.tile.position[1]+1)):
                    self.move_buffer = (self.tile.position[0]-1, self.tile.position[1]+1)
            case 8: # downright
                if self.canMove((self.tile.position[0]+1, self.tile.position[1]+1)):
                    self.move_buffer = (self.tile.position[0]+1, self.tile.position[1]+1)
            case 9: # stay
                if self.canMove((self.tile.position[0], self.tile.position[1])):
                    pass

    def total_amt(self):
        temp = 0
        for gas in self.tile.gasses:
            temp += gas.amount
        return temp

    '''def probability(self, pos):
        return 1 / (1 + math.exp(-self.steepness * (self.tile.gasses[] - X)))'''

    '''def determine_probabilities(self):
        for pos in [
            {(self.tile.position[0]-1, self.tile.position[1]) : 0}, # left
            {(self.tile.position[0]+1, self.tile.position[1]) : 0}, # right
            {(self.tile.position[0], self.tile.position[1]-1) : 0}, # up
            {(self.tile.position[0], self.tile.position[1]+1) : 0}, # down
            {(self.tile.position[0]-1, self.tile.position[1]-1) : 0}, # upleft
            {(self.tile.position[0]+1, self.tile.position[1]+1) : 0}, # upright
            {(self.tile.position[0]-1, self.tile.position[1]+1) : 0}, # downleft
            {(self.tile.position[0]+1, self.tile.position[1]+1) : 0}, # downright
            {(self.tile.position[0], self.tile.position[1]) : 0} # stay
            ]:'''
            
