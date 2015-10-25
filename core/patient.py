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
        self.x, self.y, self.distance = x, y, random.randint(10000, 25000)
        self.drawing, self.ride = False, False
        self.ui = self.pygame.font.SysFont("monaco", 25)

    def draw(self):
        if self.drawing:
            self.screen.blit(self.image, [self.x, self.y])

    # move patient
    def move(self):
        if self.x <= 0:
            self.change()
            self.x = 480
        key = self.pygame.key.get_pressed()
        if key[self.pygame.K_RIGHT]:
            self.x -= 0.2

    # patient game logic
    def update(self):
        if not self.world.amb.patient:
            current = self.world.amb.last_trip
            t = random.randint(current + 5, current + 30)
            if t == int(time.time()):
                self.drawing = True
            key = self.pygame.key.get_pressed()
            if key[self.pygame.K_z] and (self.ride == False):
                self.drawing = False
                self.world.amb.add_patient()
                self.world.qa.question = True

    # change patient
    def change(self):
        model = random.choice(["boy.png", "girl.png"])
        self.image = self.pygame.image.load("./images/patients/" + model)

    # cab ride
    def cab_ride(self):
        self.distance -= 1000
        if self.distance <= 0:
            self.distance = 0

    # update distance
    def update_dist(self):
        self.distance = random.randint(10000, 25000)