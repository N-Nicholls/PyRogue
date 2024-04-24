import random
import math

# Gas class. Gas is a subclass of that takes in a tile, color, type and an amount
# Contains logic for movement and probability of movement
class Gas():
    def __init__(self, tile, type, color=(255, 0, 255), amt=0):
        self.tile = tile
        self.amount = amt
        self.move_buffer = [] # has to be a list to store multiple moves
        self.color = color # color of the gas used in tile render
        self.type = type # renaming of char. Note that gas doesn't ever render and thus might not need to be a textsprite
        self.steepness = 1 # steepness of the sigmoid function
        self.stay = 1  # probability of staying in place as a multiple of 10%

    # returns the subclass of the object
    def return_subclass(self):
        return "gas"
    
    # returns the type of gas
    def return_type(self):
        return self.type

    # TODO
    def turn_update(self):
        # dissipation
        if self.amount <= 1 and random.randint(1, 10) <= self.stay:
            self.amount = 0

        # Determine the probabilities for each direction
        probabilities = self.determine_probabilities()
        self.move_buffer = []
        for _ in range(self.amount):
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

    # updates the gas object. First checks dissipation, then determines probabilities for next movement.
    # NOTE: Functionality should eventually be moved to a turn_update() function
    def update(self):
        self.turn_update()
 
    # Determines the probability of moving to a given position based on sigmund function
    def probability(self, pos):
        if pos not in self.tile.tiles: # if the position is not in the tiles dictionary, make it (nearly) impossible to move there
            x = 90
        else:
            x = self.tile.tiles[pos].gas_total()
        y = self.tile.gas_total()
        if -self.steepness * (y - x) > 700: # to prevent overflow, sets probability to 0 if the value is too high
            return 0
        return 1 / (1 + math.exp(-self.steepness * (y - x)))

    # Determines the probabilities of moving to each adjacent tile
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

    # moves the gas object. Will return an error if no position given
    def move(self, new_positions=None):
        if new_positions is None:
            raise ValueError("No positions provided for movement.")

        for new_position in new_positions:
            if new_position in self.tile.tiles:  # Check if the position is within the grid
                new_tile = self.tile.tiles[new_position]
                if new_tile.has_occ():  # If the new tile has an occupier, don't move there
                    print(f"Can't Move to {new_position}! Already occupied.")
                else:
                    new_tile.add_gas(self.type, 1)
                    self.tile.remove_gas(self.type, 1)
            else:
                raise Exception(f"Invalid move: Position {new_position} does not exist.")

        self.move_buffer = None  # Reset the move buffer after moving for the current frame

