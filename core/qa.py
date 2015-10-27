# -*- coding: utf-8 -*-
# Copyright (c) 2015 Zhassulan Zhussupov
# Author zhzhussupovkz@gmail.com
# Q&A class

import sqlite3
import time

class QA:
    def __init__(self, pygame, screen):
        self.pygame = pygame
        self.screen = screen
        self.drawing, self.question = True, False
        self.image = self.pygame.image.load("./images/qa/qa.png")
        self.close = self.pygame.image.load("./images/qa/close.png")
        self.a_button = self.pygame.image.load("./images/qa/a.png")
        self.b_button = self.pygame.image.load("./images/qa/b.png")
        self.c_button = self.pygame.image.load("./images/qa/c.png")
        self.d_button = self.pygame.image.load("./images/qa/d.png")
        self.e_button = self.pygame.image.load("./images/qa/e.png")
        self.ui_main = self.pygame.font.SysFont("monaco", 16)
        self.ui = self.pygame.font.SysFont("monaco", 20)
        self.conn = sqlite3.connect("./core/db/main.db")
        self.c = self.conn.cursor()
        self.fin = ''
        self.last_answer = int(time.time())

    def chunk(self, text, length):
        return list(text[0+i:length+i] for i in range(0, len(text), length))

    def draw(self):
        if self.drawing:
            self.screen.blit(self.image, [50, 50])
            self.screen.blit(self.close, [380, 50])
            text = []
            text.append(u"Ревматоидный артрит — системное воспалительное заболевание соединительной ткани с преимущественным поражением суставов по типу хронического прогрессирующего эрозивно-деструктивного полиартрита")
            text.append(u"Встречается во всех климатогеографических зонах примерно у 0,4—1% населения, преимущественно у женщин среднего и пожилого возраста.")
            text.append(u"Этиология: В соответствии с мультифакториальной теорией ревматоидного артрита может развиться под влиянием разнообразных воздействий окружающей среды при условии генетической предрасположенности. Среди возможных этиологических факторов рассматриваются некоторые инфекционные агенты; стрептококки группы В. микоплазмы, ретровирусы, вирус Эпстайна-Барр.")
            text.append(u"Симптомы: 1) Утомляемость; 2) Небольшое повышение температуры тела; 3) Увеличение лимфатических узлов; 4) Похудение")
            text.append(u"Диагностика: 1) анемия; 2) увеличение СОЭ;   3)повышение содержания С-реактивного белка")

            i = 100
            for k in range(0, len(text)):
                j = 0 + (k * 12)
                for t in self.chunk(text[k], 44):
                    copyright = self.ui_main.render(t, 1, (0, 0, 0))
                    self.screen.blit(copyright, (90, i + j))
                    i += 15

    def draw_question(self, id):
        qs = self.c.execute("SELECT * FROM question WHERE id=?", (int(id),))
        current = qs.fetchone()
        if self.question:
            self.screen.blit(self.image, [50, 50])
            self.screen.blit(self.close, [380, 50])
            text = current[1]
            i = 100
            for t in self.chunk(text, 36):
                copyright = self.ui.render(t, 1, (0, 0, 0))
                self.screen.blit(copyright, (90, i))
                i += 15

            i += 20

            text = u"A) %s" % current[2]
            for t in self.chunk(text, 36):
                copyright = self.ui.render(t, 1, (0, 0, 0))
                self.screen.blit(copyright, (90, i))
                i += 15

            text = u"B) %s" % current[3]
            for t in self.chunk(text, 36):
                copyright = self.ui.render(t, 1, (0, 0, 0))
                self.screen.blit(copyright, (90, i))
                i += 15

            text = u"C) %s" % current[4]
            for t in self.chunk(text, 36):
                copyright = self.ui.render(t, 1, (0, 0, 0))
                self.screen.blit(copyright, (90, i))
                i += 15

            text = u"D) %s" % current[5]
            for t in self.chunk(text, 36):
                copyright = self.ui.render(t, 1, (0, 0, 0))
                self.screen.blit(copyright, (90, i))
                i += 15

            text = u"E) %s" % current[6]
            for t in self.chunk(text, 36):
                copyright = self.ui.render(t, 1, (0, 0, 0))
                self.screen.blit(copyright, (90, i))
                i += 15

            i += 32

            self.screen.blit(self.a_button, [125, i])
            self.screen.blit(self.b_button, [175, i])
            self.screen.blit(self.c_button, [225, i])
            self.screen.blit(self.d_button, [275, i])
            self.screen.blit(self.e_button, [325, i])

            answer = current[7]
            f = self.ui.render(self.fin, 1, (0, 0, 0))
            self.screen.blit(f, (200, i + 50))

            for event in self.pygame.event.get():
                if event.type == self.pygame.MOUSEBUTTONDOWN and event.button == 1:
                    pos = self.pygame.mouse.get_pos()
                    mx, my = list(pos)
                    if answer == 'a' and mx >= 125 and mx <= 155 and my >= (i - 5) and my <= (i + 30):
                        self.fin = u"Правильно!"
                        self.last_answer = int(time.time())
                    elif answer == 'b' and mx >= 175 and mx <= 200 and my >= (i - 5) and my <= (i + 30):
                        self.fin = u"Правильно!"
                        self.last_answer = int(time.time())
                    elif answer == 'c' and mx >= 225 and mx <= 250 and my >= (i - 5) and my <= (i + 30):
                        self.fin = u"Правильно!"
                        self.last_answer = int(time.time())
                    elif answer == 'd' and mx >= 270 and mx <= 300 and my >= (i - 5) and my <= (i + 30):
                        self.fin = u"Правильно!"
                        self.last_answer = int(time.time())
                    elif answer == 'b' and mx >= 325 and mx <= 355 and my >= (i - 5) and my <= (i + 30):
                        self.fin = u"Правильно!"
                        self.last_answer = int(time.time())
                    elif mx >= 125 and mx <= 355 and my >= (i - 5) and my <= (i + 30):
                        self.fin = u"Неправильно!"
                        self.last_answer = int(time.time())

    def close(self):
        self.conn.commit()
        self.conn.close()

    def update(self):
        for event in self.pygame.event.get():
            if event.type == self.pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = self.pygame.mouse.get_pos()
                mx, my = list(pos)
                if mx >= 385 and mx <= 400 and my >= 60 and my <= 70:
                    self.drawing, self.question = False, False

        if self.question:
            t = self.last_answer + 2
            if t == int(time.time()) and self.fin in [u"Правильно!", u"Неправильно!"]:
                self.question = False
