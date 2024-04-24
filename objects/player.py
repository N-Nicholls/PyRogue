from objects.occupier import Occupier
import pygame

# Player class that inherits from Occupier
class Player(Occupier):
    def __init__(self, game, tile, controls):
        self.controls = controls
        super(Player, self).__init__(game, tile, '@', (255,255,0))
        self.cool_down = 0
        self.cool_down_max = int(self.game.FRAME_RATE/4*0) # cooldown disabled for time being, kept as a reminder

    # Player turn function that gets movement and adds to movement buffer
    # Note: Should be the only function that handles turn dependent updates
    # Note: Currently all keybinds can't trigger movements for some reason.
    def turn_update(self):
        if not self.my_turn:
            return
        print("My turn!")
        controls = pygame.key.get_pressed()

        # Helper function to check if any key in a list is pressed
        def is_action_pressed(action_keys):
            return any(controls[key] for key in action_keys if key < len(controls))
        
        # Movement actions, checking each direction with potential multiple keys
        if is_action_pressed(self.game.controls['left']):
            self.move_buffer = (self.tile.position[0]-1, self.tile.position[1])
            self.game.state.increment_list()
        elif is_action_pressed(self.game.controls['right']): # repeater
            self.move_buffer = (self.tile.position[0]+1, self.tile.position[1])
            self.game.state.increment_list()
        elif is_action_pressed(self.game.controls['up']):
            self.move_buffer = (self.tile.position[0], self.tile.position[1]-1)
            self.game.state.increment_list()
        elif is_action_pressed(self.game.controls['down']): # repeater
            self.move_buffer = ((self.tile.position[0], self.tile.position[1]+1))
            self.game.state.increment_list()
        elif is_action_pressed(self.game.controls['upleft']):
            self.move_buffer = ((self.tile.position[0]-1, self.tile.position[1]-1))
            self.game.state.increment_list()
        elif is_action_pressed(self.game.controls['upright']):
            self.move_buffer = ((self.tile.position[0]+1, self.tile.position[1]-1))
            self.game.state.increment_list()
        elif is_action_pressed(self.game.controls['downleft']): # repeater
            self.move_buffer = ((self.tile.position[0]-1, self.tile.position[1]+1))
            self.game.state.increment_list()
        elif is_action_pressed(self.game.controls['downright']): # repeater
            self.move_buffer = ((self.tile.position[0]+1, self.tile.position[1]+1))
            self.game.state.increment_list()

        # super(Player, self).turn_update() # can't call right now because super just increments list

    # Player turn independent update function.
    def update(self):
        super(Player, self).update()
        

    # Returns the subclass of the object
    def return_sublcass(self):
        return "player"

