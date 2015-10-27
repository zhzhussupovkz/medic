# -*- coding: utf-8 -*-
# Copyright (c) 2015 Zhassulan Zhussupov
# Author zhzhussupovkz@gmail.com
# World class

import pygame, sys
import random
import math
from road import *
from ambulance import *
from car import *
from hospital import *
from patient import *
from tree import *
from house import *
from board import *
from qa import *

class World:
    SIZE = (480, 640)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Medic game')
        self.pygame = pygame
        self.screen = pygame.display.set_mode(self.SIZE)
        self.background_image = pygame.image.load("./images/env/green.png").convert()
        self.board = Board(pygame, self.screen)
        self.qa = QA(self, self.screen)
        self.road = Road(self, self.screen)
        self.cars, self.trees, self.houses = [], [], []
        self.gen_cars()
        self.gen_trees()
        self.gen_houses()
        self.amb = Ambulance(self, self.screen, 40, 175)
        self.patient = Patient(self, self.screen, 300, 340)
        self.hospital = Hospital(self, self.screen, 400, 340)

    def gen_cars(self):
        i = 20
        while i <= 440:
            self.cars.append(Car(self, self.screen, i, 55))
            i += 125

    def gen_trees(self):
        i = 20
        while i <= 440:
            self.trees.append(Tree(self, self.screen, i, 15))
            self.trees.append(Tree(self, self.screen, i, 270))
            i += 100

    def gen_houses(self):
        i = 50
        while i <= 450:
            self.houses.append(House(self, self.screen, i, 10))
            self.houses.append(House(self, self.screen, i, 280))
            i += 100

    def draw(self):
        self.board.draw()
        self.road.draw()
        self.amb.draw()
        self.patient.draw()
        self.hospital.draw()
        for car in self.cars:
            car.draw()
        for tree in self.trees:
            tree.draw()
        for house in self.houses:
            house.draw()
        self.qa.draw()
        self.qa.draw_question()

    def play(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            key = pygame.key.get_pressed()
            if key[pygame.K_ESCAPE]:
                sys.exit()
            self.screen.blit(self.background_image, [0, 0])
            self.draw()
            self.patient.update()
            self.patient.move()
            self.hospital.update()
            self.hospital.move()
            for car in self.cars:
                car.driving()
            for tree in self.trees:
                tree.move()
            for house in self.houses:
                house.move()
            self.road.move()
            self.amb.driving()
            self.qa.update()
            pygame.display.flip()
        pygame.quit()
        self.qa.close()
