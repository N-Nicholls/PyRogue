from objects.occupier import Occupier
import pygame

class Player(Occupier):
    def __init__(self, game, tile, controls):
        self.controls = controls
        super(Player, self).__init__(game, tile, '@', (255,255,0))
        self.cool_down = 0
        self.cool_down_max = int(self.game.FRAME_RATE/4*0) # cooldown disabled for time being

    def take_turn(self):
        controls = pygame.key.get_pressed()

        # Helper function to check if any key in a list is pressed
        def is_action_pressed(action_keys):
            return any(controls[key] for key in action_keys if key < len(controls))
        
        # Movement actions, checking each direction with potential multiple keys
        if is_action_pressed(self.game.controls['left']):
            self.move_buffer = (self.tile.position[0]-1, self.tile.position[1])
            self.ac -= 1
        elif is_action_pressed(self.game.controls['right']): # repeater
            self.move_buffer = (self.tile.position[0]+1, self.tile.position[1])
            self.ac -= 1
        elif is_action_pressed(self.game.controls['up']):
            self.move_buffer = (self.tile.position[0], self.tile.position[1]-1)
            self.ac -= 1
        elif is_action_pressed(self.game.controls['down']): # repeater
            self.move_buffer = ((self.tile.position[0], self.tile.position[1]+1))
            self.ac -= 1
        elif is_action_pressed(self.game.controls['upleft']):
            self.move_buffer = ((self.tile.position[0]-1, self.tile.position[1]-1))
            self.ac -= 1
        elif is_action_pressed(self.game.controls['upright']):
            self.move_buffer = ((self.tile.position[0]+1, self.tile.position[1]-1))
            self.ac -= 1
        elif is_action_pressed(self.game.controls['downleft']): # repeater
            self.move_buffer = ((self.tile.position[0]-1, self.tile.position[1]+1))
            self.ac -= 1
        elif is_action_pressed(self.game.controls['downright']): # repeater
            self.move_buffer = ((self.tile.position[0]+1, self.tile.position[1]+1))
            self.ac -= 1

    def update(self):
        super(Player, self).update()
        if self.ac > 0:
            self.take_turn()
        else:
            self.game.state.increment_current()

    def return_sublcass(self):
        return "player"

