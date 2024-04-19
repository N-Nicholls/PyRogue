from states.levelstate import LevelState
import pygame
import json

class Game():

    def __init__(self):

        ''' file_path = './core/config.json'

        with open(file_path, 'r') as json_file:
            config_data_loaded = json.load(json_file)'''

        self.SCREEN_WIDTH = 800
        self.SCREENHEIGHT = 600
        self.FONT_SIZE = 20 # sutiable size for grid cells
        self.FRAME_RATE = 60
        pygame.init()

        # Set up display
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREENHEIGHT))
        # Load a monospaced font
        self.font = pygame.font.SysFont('Courier', self.FONT_SIZE, bold=True)
        self.clock = pygame.time.Clock()
        self.controls = None
        self.state = LevelState(self, self.controls)
        self.running = True

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


