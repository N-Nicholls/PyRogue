from objects.occupier import Occupier
import pygame

class Player(Occupier):
    def __init__(self, game, tile, controls):
        self.controls = controls
        super(Player, self).__init__(game, tile, '@', (255,255,0))
        self.cool_down = 0
        self.cool_down_max = int(self.game.FRAME_RATE/4*0)

    def update(self):
        controls = pygame.key.get_pressed()
        # print(self.cool_down)
        
        # Helper function to check if any key in a list is pressed
        def is_action_pressed(action_keys):
            return any(controls[key] for key in action_keys if key < len(controls))
        
        if self.cool_down > 0:
            self.cool_down -= 1
        # Movement actions, checking each direction with potential multiple keys
        if self.cool_down == 0:
            if is_action_pressed(self.game.controls['left']) and self.used == False:
                self.move((self.tile.position[0]-1, self.tile.position[1]))
                self.cool_down = self.cool_down_max
            if is_action_pressed(self.game.controls['right']) and self.used == False: # repeater
                self.move((self.tile.position[0]+1, self.tile.position[1]))
                self.cool_down = self.cool_down_max
            if is_action_pressed(self.game.controls['up']) and self.used == False:
                self.move((self.tile.position[0], self.tile.position[1]-1))
                self.cool_down = self.cool_down_max
            if is_action_pressed(self.game.controls['down']) and self.used == False: # repeater
                self.move((self.tile.position[0], self.tile.position[1]+1))
                self.cool_down = self.cool_down_max
            if is_action_pressed(self.game.controls['upleft']) and self.used == False:
                self.move((self.tile.position[0]-1, self.tile.position[1]-1))
                self.cool_down = self.cool_down_max
            if is_action_pressed(self.game.controls['upright']) and self.used == False:
                self.move((self.tile.position[0]+1, self.tile.position[1]-1))
                self.cool_down = self.cool_down_max
            if is_action_pressed(self.game.controls['downleft']) and self.used == False: # repeater
                self.move((self.tile.position[0]-1, self.tile.position[1]+1))
                self.cool_down = self.cool_down_max
            if is_action_pressed(self.game.controls['downright']) and self.used == False: # repeater
                self.move((self.tile.position[0]+1, self.tile.position[1]+1))
                self.cool_down = self.cool_down_max

        super(Player, self).update()

    def return_sublcass(self):
        return "player"

