# -*- coding: utf-8 -*-
# Copyright (c) 2015 Zhassulan Zhussupov
# Author zhzhussupovkz@gmail.com
# Car class

import random

class Car(object):
    def __init__(self, world, screen, x, y):
        self.pygame, self.world = world.pygame, world
        model = random.choice(["car_1", "car_2", "car_3", "car_4", "car_5", "car_6"])
        self.image = self.pygame.image.load("./images/cars/" + model + ".png")
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
        if self.x <= 200:
            self.x += 0.1

    def go(self):
        if self.x >= 0:
            key = self.pygame.key.get_pressed()
            if key[self.pygame.K_RIGHT]:
                self.x -= 0.5
            self.x -= 0.2

    def driving(self):
        self.go()
        if self.x <= 0:
            self.change()
            self.x = 480

    def change(self):
        model = random.choice(["car_1", "car_2", "car_3", "car_4", "car_5", "car_6"])
        image = self.pygame.image.load("./images/cars/" + model + ".png")
        coord = random.randint(55, 80)
        self.y = coord