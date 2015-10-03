# -*- coding: utf-8 -*-
# Copyright (c) 2015 Zhassulan Zhussupov
# Author zhzhussupovkz@gmail.com
# Line class

class Line:
    def __init__(self, world, screen, x, y):
        self.world, self.pygame = world, world.pygame
        self.screen = screen
        self.x, self.y = x, y
        self.img = self.pygame.image.load("./images/env/line.png").convert()

    def draw(self):
        self.screen.blit(self.img, [self.x, self.y])

    def move(self):
        if self.x <= 0:
            self.x = 480
        key = self.pygame.key.get_pressed()
        if key[self.pygame.K_RIGHT]:
            self.x -= 0.2
