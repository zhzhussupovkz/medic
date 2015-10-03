# -*- coding: utf-8 -*-
# Copyright (c) 2015 Zhassulan Zhussupov
# Author zhzhussupovkz@gmail.com
# Hospital class

class Hospital:
    def __init__(self, world, screen, x, y):
        self.world, self.pygame = world, world.pygame
        self.screen = screen
        self.image = self.pygame.image.load("./images/houses/hospital.png")
        self.x, self.y = x, y

    def draw(self):
        self.screen.blit(self.image, [self.x, self.y])
