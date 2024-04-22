from objects.textsprite import TextSprite

class Occupier(TextSprite):
    def __init__(self, game, tile, char, color, font=None):
        self.tile = tile
        # Used to check if the occupier has already moved in the current board update
        super(Occupier, self).__init__(game, char, color, font)

    def move(self, new_position):
        if self.used == False:    
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
                    self.used = True
                    for element in self.tile.tiles.values():
                        element.update()
            else:
                print(f"Invalid move: Position {new_position} does not exist.")

    def update(self):
        pass

    def return_subclass(self):
        return "occupier"
