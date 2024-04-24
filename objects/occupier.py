from objects.textsprite import TextSprite

class Occupier(TextSprite):
    def __init__(self, game, tile, char, color, font=None):
        self.tile = tile
        self.move_buffer = None
        self.ac = 1
        self.ac_max = 1
        super(Occupier, self).__init__(game, char, color, font)

    def move(self, new_position = None):
        if self.move_buffer is not None:    
            # Check if the new_position is within the grid boundaries and exists in the tiles dictionary
            if new_position in self.tile.tiles:
                new_tile = self.tile.tiles[new_position]
                if new_tile.has_occ():
                    print("Can't Move there! Already occupied.")
                else:
                    print("Moved to", new_position)
                    # Remove occupier from current tile and add to the new tile
                    self.tile.remove_occ()
                    new_tile.add_occ(self)
                    # Update the occupier's tile reference to the new tile
                    self.tile = new_tile
            else:
                print(f"Invalid move: Position {new_position} does not exist.")
            self.move_buffer = None

    def update(self):
        pass

    def return_subclass(self):
        return "occupier"
    
