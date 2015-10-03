# -*- coding: utf-8 -*-
# Copyright (c) 2015 Zhassulan Zhussupov
# Author zhzhussupovkz@gmail.com
# World class

import pygame, sys
import random
import math
from road import *
from ambulance import *
from hospital import *
from board import *

class World:
    SIZE = (480, 640)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Medic game')
        self.pygame = pygame
        self.screen = pygame.display.set_mode(self.SIZE)
        self.background_image = pygame.image.load("./images/env/green.png").convert()
        self.board = Board(pygame, self.screen)
        self.road = Road(self, self.screen)
        self.amb = Ambulance(self, self.screen, 40, 175)
        self.hospital = Hospital(self, self.screen, 400, 260)

    def draw(self):
        self.board.draw()
        self.road.draw()
        self.amb.draw()
        self.hospital.draw()

    def play(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            key = pygame.key.get_pressed()
            if key[pygame.K_ESCAPE]:
                sys.exit()
            self.screen.blit(self.background_image, [0, 0])
            self.draw()
            self.road.move()
            self.amb.driving()
            pygame.display.flip()
        pygame.quit()
