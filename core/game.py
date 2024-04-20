from states.levelstate import LevelState
import pygame
import json

class Game():

    def __init__(self):

        ''' file_path = './core/config.json'

        with open(file_path, 'r') as json_file:
            config_data_loaded = json.load(json_file)'''
        
        self.FONT_SIZE = 12 # sutiable size for grid cells
        self.SCREEN_WIDTH = self.FONT_SIZE * 80
        self.SCREENHEIGHT = self.FONT_SIZE * 25
        
        self.offset = self.FONT_SIZE/2
        self.FRAME_RATE = 60
        pygame.init()

        # Set up display
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREENHEIGHT), pygame.RESIZABLE)
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


