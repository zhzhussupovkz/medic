# -*- coding: utf-8 -*-
# Copyright (c) 2015 Zhassulan Zhussupov
# Author zhzhussupovkz@gmail.com
# Patient class

import random
import time

class Patient:
    def __init__(self, world, screen, x, y):
        self.pygame = world.pygame
        self.screen, self.world = screen, world
        model = random.choice(["boy.png", "girl.png"])
        self.image = self.pygame.image.load("./images/patients/" + model)
        self.x, self.y = x, y
        self.drawing = False
        self.ui = self.pygame.font.SysFont("monaco", 25)

    def draw(self):
        if self.drawing:
            self.screen.blit(self.image, [self.x, self.y])

    # move passenger
    def move(self):
        if self.x <= 0:
            self.change()
            self.x = 480
        key = self.pygame.key.get_pressed()
        if key[self.pygame.K_RIGHT]:
            self.x -= 0.2
