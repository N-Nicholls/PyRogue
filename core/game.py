from states.levelstate import LevelState
import pygame
import json

class Game():

    def __init__(self):

        file_path = './core/config.json'

        with open(file_path, 'r') as json_file:
            config_data_loaded = json.load(json_file)
        self.controls = self.load_controls(config_data_loaded["controls"])
        
        self.FONT_SIZE = 20 # sutiable size for grid cells
        self.SCREEN_WIDTH = self.FONT_SIZE * 80
        self.SCREENHEIGHT = self.FONT_SIZE * 25
        self.offset = self.FONT_SIZE/8
        self.FRAME_RATE = 10
        pygame.init()

        # Set up display
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREENHEIGHT), pygame.RESIZABLE | pygame.HWACCEL)
        # Load a monospaced font
        self.font = pygame.font.SysFont('Courier', self.FONT_SIZE, bold=True)
        self.clock = pygame.time.Clock()
        self.state = LevelState(self, self.controls)
        self.running = True

    def load_controls(self, controls_config):
        controls = {
            'left': [pygame.K_KP4, pygame.K_LEFT, pygame.K_h],  # Adding list of keys
            'right': [pygame.K_KP6, pygame.K_RIGHT, pygame.K_l],
            'up': [pygame.K_KP8, pygame.K_UP, pygame.K_k],
            'down': [pygame.K_KP2, pygame.K_DOWN, pygame.K_j],
            'upleft': [pygame.K_KP7, pygame.K_y],
            'upright': [pygame.K_KP9, pygame.K_u],
            'downleft': [pygame.K_KP1, pygame.K_b],
            'downright': [pygame.K_KP3, pygame.K_n]
            }

        '''for action, keys in controls_config.items():
            if isinstance(keys, list) and all(isinstance(key, str) for key in keys):
                resolved_keys = []
                for key_name in keys:
                    if hasattr(pygame, key_name):
                        resolved_keys.append(getattr(pygame, key_name))
                    else:
                        print(f"Warning: Key name {key_name} is not recognized by pygame")
                if resolved_keys:
                    controls[action] = resolved_keys
                else:
                    print(f"No valid keys found for action '{action}'. Using defaults.")
            else:
                print(f"Invalid key configuration for '{action}'. Expected a list of keys.")'''

        return controls

    def run(self):
        while self.running:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.running = False

            self.state.draw(self.screen)
            self.state.handleEvents(events)
            self.state.update()

            pygame.display.flip()
            self.clock.tick(self.FRAME_RATE)

    def changeState(self, state):
        self.state = state

    def quit(self):
        pygame.quit() 


