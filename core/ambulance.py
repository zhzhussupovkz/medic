# -*- coding: utf-8 -*-
# Copyright (c) 2015 Zhassulan Zhussupov
# Author zhzhussupovkz@gmail.com
# Ambulance class

class Ambulance(object):
    def __init__(self, world, screen, x, y):
        self.pygame, self.world = world.pygame, world
        self.image = self.pygame.image.load("./images/ambulance_little.png")
        self.x, self.y = x, y
        self.screen = screen

    def draw(self):
        self.screen.blit(self.image, [self.x, self.y])

    def move_left(self):
        self.y -= 0.2
        if self.y <= 165:
            self.y = 165

    def move_right(self):
        self.y += 0.2
        if self.y >= 200:
            self.y = 200

    def brake(self):
        if self.x >= 200:
            self.x -= 0.1

    def go(self):
        if self.x <= 400:
            self.x += 0.2

    def driving(self):
        key = self.pygame.key.get_pressed()
        if key[self.pygame.K_RIGHT]:
            self.go()
        elif key[self.pygame.K_LEFT]:
            self.brake()
        if key[self.pygame.K_DOWN]:
            self.move_right()
        elif key[self.pygame.K_UP]:
            self.move_left()
