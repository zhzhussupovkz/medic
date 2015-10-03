# -*- coding: utf-8 -*-
# Copyright (c) 2015 Zhassulan Zhussupov
# Author zhzhussupovkz@gmail.com
# Ambulance class

import time

class Ambulance(object):
    def __init__(self, world, screen, x, y):
        self.pygame, self.world = world.pygame, world
        self.image = self.pygame.image.load("./images/ambulance_little.png")
        self.heart = self.pygame.image.load("./images/scboard/heart.png")
        self.x, self.y = x, y
        self.screen = screen
        self.lives, self.score, self.level = 3, 0, 1
        self.total_distance = 0
        self.last_hospital = int(time.time())
        self.ui = self.pygame.font.SysFont("monaco", 20)

    def draw(self):
        self.screen.blit(self.image, [self.x, self.y])
        self.draw_score()

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
        if self.x <= 320:
            self.x += 0.2
        self.total_distance += 10
        if self.total_distance % 1000 == 0:
            self.score += 10

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

    def draw_score(self):
        i = 0
        for j in range(0, self.lives):
            self.screen.blit(self.heart, [20 + i, 525])
            i += 34
        ui_sc = self.ui.render("Score: %s" % self.score, 1, (0, 0, 0))
        self.screen.blit(ui_sc, (20, 575))
        ui_lvl = self.ui.render("Level: %s" % self.level, 1, (0, 0, 0))
        self.screen.blit(ui_lvl, (420, 575))
