# -*- coding: utf-8 -*-
# Copyright (c) 2015 Zhassulan Zhussupov
# Author zhzhussupovkz@gmail.com
# Q&A class

import sqlite3
import time
import random

class QA:
    def __init__(self, world, screen):
        self.world, self.pygame = world, world.pygame
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
        level = world.amb.level
        qs = self.c.execute("SELECT * FROM question WHERE level=?", (int(level),))
        self.current = random.choice(qs.fetchall())

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

    def draw_question(self):
        if self.question:
            self.screen.blit(self.image, [50, 50])
            self.screen.blit(self.close, [380, 50])
            text = self.current[2]
            i = 100
            for t in self.chunk(text, 36):
                copyright = self.ui.render(t, 1, (0, 0, 0))
                self.screen.blit(copyright, (90, i))
                i += 15

            i += 20

            text = u"A) %s" % self.current[3]
            for t in self.chunk(text, 36):
                copyright = self.ui.render(t, 1, (0, 0, 0))
                self.screen.blit(copyright, (90, i))
                i += 15

            text = u"B) %s" % self.current[4]
            for t in self.chunk(text, 36):
                copyright = self.ui.render(t, 1, (0, 0, 0))
                self.screen.blit(copyright, (90, i))
                i += 15

            text = u"C) %s" % self.current[5]
            for t in self.chunk(text, 36):
                copyright = self.ui.render(t, 1, (0, 0, 0))
                self.screen.blit(copyright, (90, i))
                i += 15

            text = u"D) %s" % self.current[6]
            for t in self.chunk(text, 36):
                copyright = self.ui.render(t, 1, (0, 0, 0))
                self.screen.blit(copyright, (90, i))
                i += 15

            text = u"E) %s" % self.current[7]
            for t in self.chunk(text, 36):
                copyright = self.ui.render(t, 1, (0, 0, 0))
                self.screen.blit(copyright, (90, i))
                i += 15

            if self.current[9]:
                i += 20
                img = self.pygame.image.load("./images/qa/%s" % self.current[9])
                self.screen.blit(img, [150, i])
                size = img.get_rect().size
                i += size[1]

            i += 32

            self.screen.blit(self.a_button, [125, i])
            self.screen.blit(self.b_button, [175, i])
            self.screen.blit(self.c_button, [225, i])
            self.screen.blit(self.d_button, [275, i])
            self.screen.blit(self.e_button, [325, i])

            answer = self.current[8]
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
                if self.fin == u"Правильно!":
                    self.world.amb.score += 1000
                elif self.fin == u"Неправильно!":
                    self.world.amb.score -= 500
                self.question = False
                self.fin = ''
                level = self.world.amb.level
                qs = self.c.execute("SELECT * FROM question WHERE level=?", (int(level),))
                self.current = random.choice(qs.fetchall())

    def create_questions(self):
        self.c.execute("insert into question (id, level, q, a, b, c, d, e, answer) values (1, 1, 'Какие суставы чаще всего вовлекаются в патологический процесс при РА?', 'Проксимальные межфаланговые суставы кистей.', 'Дистальные межфаланговые суставы кистей.', 'Коленные суставы.', 'Суставы поясничного отдела позвоночника.', 'Суставы шейного отдела позвоночника', 'c');")
        self.c.execute("insert into question (id, level, q, a, b, c, d, e, answer) values (2, 1, 'Какими заболеваниями может сопровождаться РА?', 'Васкулит', 'Подагра', 'Остеохондроз', 'Плеврит', 'Остеопороз', 'a');")
        self.c.execute("insert into question (id, level, q, a, b, c, d, e, answer, img) values (3, 1, 'Как называется данный вид деформации пальцев кисти?', 'Шея лебедя', 'Синдром Шегрена', 'Пуговичная петля', 'Плавник моржа', 'Синдром Каплана', 'a', 'q3.png');")
        self.c.execute("insert into question (id, level, q, a, b, c, d, e, answer) values (4, 2, 'Для РА характерно: а) утренняя скованность; б) симметричность поражения суставов; в) поражение дистальных межфаланговых суставов; г) гиперемия в области суставов; д)боли в суставах в первую  половину ночи. Выберите правильную комбинацию ответов:', 'а,б', 'б,в', 'в,г', 'а,б,в', 'в,г,д', 'a');")
        self.c.execute("insert into question (id, level, q, a, b, c, d, e, answer) values (5, 2, 'При каком осложнении РА анализ мочи является информативным тестом?', 'Синдром Хаменна-Рича', 'Перикардит', 'Амилайдоз', 'Дигитальный ангиит', 'A,C', 'c');")
        self.c.execute("insert into question (id, level, q, a, b, c, d, e, answer) values (6, 2, 'Отметьте наиболее характерные легочные проявления ревматоидного артрита?', 'кровохарканье', 'фиброзирующийальвеолит', 'высокое содержание глюкозы в плевральной полости', 'Васкулит', 'Узелки Бушара', 'b');")
        self.c.execute("insert into question (id, level, q, a, b, c, d, e, answer) values (7, 3, 'Рентгенологическими признаками ревматоидного артрита являются: а) остеопороз; б) эрозии; в) остеофитоз; г) межпозвоночные оссификаты; д) одностороннийсакролеит. Выберите комбинацию ответов:', 'а,б;', 'б,в;', 'в,г;', 'а,б,в;', 'в,г,д;', 'a');")
        self.c.execute("insert into question (id, level, q, a, b, c, d, e, answer, img) values (8, 3, 'Какой вид РА указан на этой картинке?', 'синдром Фелти', 'синдром Каплана', 'синдром Шегнера', 'серпозитивный РА', 'ювенильный РА', 'e', 'q8.png');")
        self.c.execute("insert into question (id, level, q, a, b, c, d, e, answer) values (9, 3, 'Выберите характерные иммунологические изменения при РА?', 'Появление антиядерных антител.', 'Определение ревматоидного фактора.', 'Гипокомплементемия.', 'Появление антикардиолипиновых антител.', 'Появление антител к циклическому цитруллинированному пептиду.', 'e');")
        self.c.execute("insert into question (id, level, q, a, b, c, d, e, answer) values (10, 3, 'Укажите наиболее типичные изменения в клиническом анализе крови больных при РА?', 'лейкопения', 'ускорение СОЭ', 'гипохромная анемия', 'тромбоцитопения', 'B, C', 'e');")
        self.conn.commit()
