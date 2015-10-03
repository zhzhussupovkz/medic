# -*- coding: utf-8 -*-
# Copyright (c) 2015 Zhassulan Zhussupov
# Author zhzhussupovkz@gmail.com
# Hospital class

import random
import time

class Hospital:
    def __init__(self, world, screen, x, y):
        self.world, self.pygame = world, world.pygame
        self.screen = screen
        self.image = self.pygame.image.load("./images/houses/hospital.png")
        self.x, self.y, self.drawing = x, y, False

    def draw(self):
        if self.drawing:
            self.screen.blit(self.image, [self.x, self.y])

    # game logic
    def update(self):
        current = self.world.amb.last_hospital
        t = random.randint(current + 10, current + 30)
        if t == int(time.time()):
            self.drawing = True

    def move(self):
        if self.x <= 0:
            self.change()
            self.x = 480
        key = self.pygame.key.get_pressed()
        if key[self.pygame.K_RIGHT]:
            self.x -= 0.2

    def move(self):
        if self.drawing:
            if self.x <= 0:
                self.x = 480
                self.world.amb.last_hospital = int(time.time())
                self.change()
            key = self.pygame.key.get_pressed()
            if key[self.pygame.K_RIGHT]:
                self.x -= 0.2

    def change(self):
        self.drawing = False
