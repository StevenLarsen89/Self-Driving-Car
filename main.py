# SELF-DRIVING CAR

import pygame
import random
import sys
from os import path
from config import *
from sprites import *


class Game:
    def __init__(self):
        # initialize game window, objects, etc.
        # initiate pygame
        pygame.init()
        # pygame module for loading and playing sounds
        pygame.mixer.init()
        # set size of game display
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        # title of game window
        pygame.display.set_caption('Ghost Driver')
        # define game clock
        self.clock = pygame.time.Clock()
        self.load_data()
        self.running = True



    def load_data(self):
        game_folder = path.dirname(__file__)
        image_folder = path.join(game_folder, 'img')
        self.player_img = pygame.image.load(path.join(image_folder, CAR_IMG)).convert_alpha()
        self.player_img = pygame.transform.scale(self.player_img, (CAR_WIDTH, CAR_HEIGHT))

    """" start a new game """
    def new(self):
        self.all_sprites = pygame.sprite.Group()
        self.player = Player(self, WIDTH*0.1, HEIGHT/2)
        self.run()

    """ Main Game Loop"""
    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    """ Game Loop - Update"""
    def update(self):
        # Game Loop - Update
        self.all_sprites.update()


    def events(self):
        # Game Loop - Events
        for event in pygame.event.get():
            # if user clicks on 'x' in top right corner, set 'crashed' to True, thereby ending game
            if event.type == pygame.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
                pygame.quit()
                quit()


    def draw(self):
        # Game Loop - Draw
        self.screen.fill(WHITE)
        # starting area
        pygame.draw.rect(self.screen, GREEN, pygame.Rect(WIDTH*0.1-CAR_WIDTH, HEIGHT/2-CAR_HEIGHT, 100, 100))
        # all sprites
        self.all_sprites.draw(self.screen)
        pygame.draw.rect(self.screen, BLACK, self.player.hit_rect, 2)
        pygame.display.flip()


    def show_start_screen(self):
        # show splash/start screen
        pass

    def show_go_screen(self):
        # show game over/continue
        pass

g = Game()
g.show_start_screen()
while g.running:
    g.new()
    g.show_go_screen()

pygame.quit()