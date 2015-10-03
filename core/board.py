# -*- coding: utf-8 -*-
# Copyright (c) 2015 Zhassulan Zhussupov
# Author zhzhussupovkz@gmail.com
# Board class

import datetime

class Board:
    def __init__(self, pygame, screen):
        self.pygame = pygame
        self.screen = screen
        self.image = self.pygame.image.load("./images/scboard/board.png")
        self.ui = self.pygame.font.SysFont("monaco", 15)
        self.controls = self.pygame.font.SysFont("monaco", 20)

    def draw(self):
        self.screen.blit(self.image, [0, 520])
        cyear = datetime.datetime.now().year
        copyright = self.ui.render("Copyright (c) %s by zhzhussupovkz" % cyear, 1, (0, 0, 0))
        self.screen.blit(copyright, (160, 620))
