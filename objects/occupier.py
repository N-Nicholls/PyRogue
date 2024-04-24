from objects.textsprite import TextSprite

# Occupier class that inherits from TextSprite
# Contains general move function
class Occupier(TextSprite):
    def __init__(self, game, tile, char, color, font=None):
        self.tile = tile
        self.move_buffer = None
        super(Occupier, self).__init__(game, char, color, font)

    # Move function that takes a new_position as an argument. '''Will return an error if no position given'''
    # Checks if pos is within boundary and unoccupied, then moves the occupier to the new position
    # Updates the occupier's tile reference to the new tile, and removes the occupier from the old tile
    def move(self, new_position=None):
        if new_position:    
            # Check if the new_position is within the grid boundaries and exists in the tiles dictionary
            if new_position in self.tile.tiles:
                new_tile = self.tile.tiles[new_position]
                if new_tile.has_occ():
                    print("Can't Move there! Already occupied.")
                else:
                    print("Moved to", new_position)
                    # Remove occupier from current tile and add to the new tile
                    self.tile.remove_occ()
                    new_tile.add_occ(self) # Note: only changes the reference, not the actual object
                    # Update the occupier's tile reference to the new tile
                    self.tile = new_tile
            else:
                print(f"Invalid move: Position {new_position} does not exist.")
            self.move_buffer = None
        '''else:
            raise Exception("No new position given to move function")'''

    def update(self):
        pass

    def return_subclass(self):
        return "occupier"
    
