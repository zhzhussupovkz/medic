# -*- coding: utf-8 -*-
# Copyright (c) 2015 Zhassulan Zhussupov
# Author zhzhussupovkz@gmail.com
# Q&A class

import sqlite3

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
        self.ui = self.pygame.font.SysFont("monaco", 20)
        self.conn = sqlite3.connect("./core/db/main.db")
        self.c = self.conn.cursor()

    def chunk(self, text, length):
        return list(text[0+i:length+i] for i in range(0, len(text), length))

    def draw(self):
        if self.drawing:
            self.screen.blit(self.image, [50, 50])
            self.screen.blit(self.close, [380, 50])
            text = u"Ревматоидный артрит (англ. rheumatoid arthritis) — это системное заболевание соединительной ткани с преимущественным поражением мелких суставов по типу эрозивно-деструктивного полиартрита неясной этиологии со сложным аутоиммунным патогенезом."
            text += u" Причины заболевания на сей день неизвестны. Косвенные данные: увеличение количества лейкоцитов в крови и скорости оседания эритроцитов (СОЭ) — указывают на инфекционную природу процесса. Полагают, что заболевание развивается в результате инфекции, вызывающей нарушения иммунной системы у наследственно предрасположенных лиц; при этом образуются так называемые иммунные комплексы (из антител, вирусов и проч.), которые откладываются в тканях и приводят к повреждению суставов. Но неэффективность лечения РА антибиотиками скорее всего свидетельствует о неправильности такого предположения."
            i = 100
            for t in self.chunk(text, 36):
                copyright = self.ui.render(t, 1, (0, 0, 0))
                self.screen.blit(copyright, (90, i))
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
