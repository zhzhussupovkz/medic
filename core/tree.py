# -*- coding: utf-8 -*-
# Copyright (c) 2015 Zhassulan Zhussupov
# Author zhzhussupovkz@gmail.com
# Tree class

import random

class Tree:
    def __init__(self, world, screen, x, y):
        self.world, self.pygame = world, world.pygame
        self.screen = screen
        model = random.choice(['tree.png', 'tree_1.png'])
        self.image = self.pygame.image.load("./images/houses/" + model)
        self.x, self.y = x, y

    def draw(self):
        self.screen.blit(self.image, [self.x, self.y])

    def move(self):
        if self.x <= 0:
            self.change()
            self.x = 480
        key = self.pygame.key.get_pressed()
        if key[self.pygame.K_RIGHT]:
            self.x -= 0.2

    def change(self):
        model = random.choice(['tree.png', 'tree_1.png'])
        self.image = self.pygame.image.load("./images/houses/" + model)
