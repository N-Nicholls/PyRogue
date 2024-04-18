from states.gamestate import GameState
from objects.physchar import PhysChar

import pygame
import random

# class to hold a level. Holds blocks and mobs and anything in a game instance
class LevelState(GameState):
    
    def __init__(self, level_file, game, controls):
        super().__init__(game)  
        # groups for rendering
        self.game = game
        self.all_sprites = pygame.sprite.Group()
        self.controls = controls
        self.parseLevel(level_file, game)

        # events and timers
        self.ADDENEMY = pygame.USEREVENT + 1
        pygame.time.set_timer(self.ADDENEMY, 1000) # add enemy every second, in ms

    def parseLevel(self, levelFile, game):
        currentLayer = None
        prevLayer = None

        # spawn points
        self.characterArr = []

        x = game.offset
        y = game.offset
        self.COOLDOWN = 0

        # World is 1920x1080, each block is 30x30, so 64x36 blocks
        temp = [None, None, None, None, None, None, None, None, None, None] # for elevators
        temp2 = []
        with open(levelFile, 'r') as file:
            lines = file.readlines()
        for line in lines:
            line = line.strip()
            words = line.split()
            
            if not words:
                continue # Skip empty lines

            if words[0].lower() in ["main"]:
                currentLayer = words[0].lower()
                x, y = game.offset, game.offset
                continue
            elif words[0].lower() == "end":
                break

            if currentLayer:
                for col in line:
                    if currentLayer == "main":
                        if col == "#":  # block
                            blockArr.append(PhysChar(self.game, (x, y), "./sprites/brick.png", True, False, 0.85, 0, (1,1,1,1)))

                    x += game.block_size  # Move to the next block in the row
                y += game.block_size  # Move to the next row
                x = game.offset  # Reset x to the start of the next row      

        for elements in blockArr:
            self.blocks.add(elements)
            self.all_sprites.add(elements)
    
    def handleEvents(self, events): 
        pressed_keys = pygame.key.get_pressed()
        for event in events:
            if event.type == self.ADDENEMY:
                # self.spawnEnemy()
                pass

    def update(self):
        # dynamic updates
        pressed_keys = pygame.key.get_pressed()
        self.player.update(pressed_keys)
        

    def draw(self, surface):
        surface.fill((0, 0, 0))
        for entity in self.all_sprites:
            surface.blit(entity.surf, entity.rect)
        self.game.screen.blit(surface, (0, 0))
        pygame.display.update()
            





