import random
import math

class Gas():
    def __init__(self, tile, type, color=(255, 0, 255), amt=0):
        self.tile = tile
        self.amount = amt
        self.move_buffer = []
        self.color = color
        self.type = type # renaming of char. Note that gas doesn't ever render and thus might not need to be a textsprite
        self.steepness = 1

    def return_subclass(self):
        return "gas"
    
    def return_type(self):
        return self.type

    def update(self):
        if self.tile.gas_total() == 0:
            return
        # Determine the probabilities for each direction
        probabilities = self.determine_probabilities()
        self.move_buffer = []

        for _ in range(self.tile.gas_total()):
            # Create a list of cumulative probabilities
            cumulative_probabilities = []
            cumulative = 0
            for direction, prob in probabilities.items():
                cumulative += prob
                cumulative_probabilities.append((cumulative, direction))

            # Generate a random number between 0 and the sum of all probabilities
            rand = random.uniform(0, cumulative_probabilities[-1][0])

            # Determine movement based on the random number
            for (cutoff, direction) in cumulative_probabilities:
                if rand <= cutoff:
                    self.move_buffer.append(direction)
                    break

    def probability(self, pos):
        if pos not in self.tile.tiles: # if the position is not in the tiles dictionary, make it impossible to move there
            x = 90
        else:
            x = self.tile.tiles[pos].gas_total()
        y = self.tile.gas_total()
        if -self.steepness * (y - x) > 700:
            return 0
        return 1 / (1 + math.exp(-self.steepness * (y - x)))

    def determine_probabilities(self):
        probalities = {
            (self.tile.position[0]-1, self.tile.position[1]) : 0, # left
            (self.tile.position[0]+1, self.tile.position[1]) : 0, # right
            (self.tile.position[0], self.tile.position[1]-1) : 0, # up
            (self.tile.position[0], self.tile.position[1]+1) : 0, # down
            (self.tile.position[0]-1, self.tile.position[1]-1) : 0, # upleft
            (self.tile.position[0]+1, self.tile.position[1]-1) : 0, # upright
            (self.tile.position[0]-1, self.tile.position[1]+1) : 0, # downleft
            (self.tile.position[0]+1, self.tile.position[1]+1) : 0, # downright
            (self.tile.position[0], self.tile.position[1]) : 0 # stay
            }
        for pos in probalities:
            probalities[pos] = self.probability(pos)   

        return probalities 


    def move(self, new_positions = None):
        if new_positions is not None:
            for new_position in new_positions:
                if new_position is not None:    
                    # Check if the new_position is within the grid boundaries and exists in the tiles dictionary
                    if new_position in self.tile.tiles:
                        new_tile = self.tile.tiles[new_position]
                        if new_tile.has_occ(): # if the new tile has an occupier, don't move there. Will eventually have more thorough checks
                            print("Can't Move there! Already occupied.")
                        else:
                            print("Moved to", new_position, " Gas amount: ", self.amount)
                            new_tile.add_gas(self.type) # passes color incase it has to make a new gas object
                            self.tile.remove_gas(self.type)

                    else:
                        print(f"Invalid move: Position {new_position} does not exist.")
                    self.move_buffer = None