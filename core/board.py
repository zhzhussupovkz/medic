# -*- coding: utf-8 -*-
# Copyright (c) 2015 Zhassulan Zhussupov
# Author zhzhussupovkz@gmail.com
# Board class

import datetime

class Board:
    def __init__(self, world, screen):
        self.pygame, self.world = world.pygame, world
        self.screen = screen
        self.image = self.pygame.image.load("./images/scboard/board.png")
        self.doctor = self.pygame.image.load("./images/scboard/doctor.png")
        self.ui = self.pygame.font.SysFont("monaco", 15)
        self.game_over_ui = self.pygame.font.SysFont("monaco", 100)

    def draw(self):
        self.screen.blit(self.image, [0, 520])
        self.screen.blit(self.doctor, [420, 525])
        cyear = datetime.datetime.now().year
        copyright = self.ui.render("Copyright (c) %s by zhzhussupovkz" % cyear, 1, (0, 0, 0))
        self.screen.blit(copyright, (160, 620))
        if self.world.game_over:
            g = self.ui.render(u"GAME OVER", 1, (0, 0, 0))
            self.screen.blit(g, (225, 550))

