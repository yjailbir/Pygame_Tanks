import pygame as pg
from sys import exit


class Tank(pg.sprite.Sprite):
    def __init__(self, file, x, y):
        pg.sprite.Sprite.__init__(self)
        self.images = file
        if x == 120:
            self.image = pg.transform.scale(pg.image.load(self.images[1]), (50, 50))
        else:
            self.image = pg.transform.scale(pg.image.load(self.images[0]), (50, 50))
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.x = x - self.rect.width
        self.rect.y = y - self.rect.height
        self.move_up = False
        self.move_down = False
        self.move_right = False
        self.move_left = False
        self.made_a_shot = False
        self.shell = None
        if x == 120:
            self.weapon = "down"
        else:
            self.weapon = "up"
        self.win = False

    def move(self):
        if self.move_up:
            self.image = pg.transform.scale(pg.image.load(self.images[0]), (50, 50))
            self.image.set_colorkey((255, 255, 255))
            if self.rect.y > 0:
                self.rect.y -= 1
        elif self.move_down:
            self.image = pg.transform.scale(pg.image.load(self.images[1]), (50, 50))
            self.image.set_colorkey((255, 255, 255))
            if self.rect.y < 550:
                self.rect.y += 1
        elif self.move_left:
            self.image = pg.transform.scale(pg.image.load(self.images[2]), (50, 50))
            self.image.set_colorkey((255, 255, 255))
            if self.rect.x > 0:
                self.rect.x -= 1
        elif self.move_right:
            self.image = pg.transform.scale(pg.image.load(self.images[3]), (50, 50))
            self.image.set_colorkey((255, 255, 255))
            if self.rect.x < 950:
                self.rect.x += 1


class Shell(pg.sprite.Sprite):
    def __init__(self, tank, enemy):
        pg.sprite.Sprite.__init__(self)
        self.tank = tank
        self.enemy = enemy
        if tank.weapon in ["up", "down"]:
            self.image = pg.image.load("снаряд_по_у.png")
            self.image.set_colorkey((255, 255, 255))
            self.rect = self.image.get_rect()
        else:
            self.image = pg.image.load("снаряд_по_х.png")
            self.image.set_colorkey((255, 255, 255))
            self.rect = self.image.get_rect()
        self.orientation = tank.weapon

    def fly(self):
        if self.orientation == "up":
            self.rect.y -= 3
        elif self.orientation == "down":
            self.rect.y += 3
        elif self.orientation == "left":
            self.rect.x -= 3
        elif self.orientation == "right":
            self.rect.x += 3
        if self.rect.y < 0 or self.rect.y > 566 or self.rect.x < 0 or self.rect.x > 966:
            self.tank.made_a_shot = False
            self.tank.shell = None
        if self.enemy.rect.x <= self.rect.x <= self.enemy.rect.x + 50 and self.enemy.rect.y <= self.rect.y <= \
                self.enemy.rect.y + 50:
            self.tank.win = True
        if 0 <= self.rect.x <= 50 and 0 <= self.rect.y <= 50:
            grey_tank.win = True
        if 950 <= self.rect.x <= 1000  and 550 <= self.rect.y <= 600:
            yellow_tank.win = True


class Bomb(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.transform.scale(pg.image.load("бомба.png"), (30, 30))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


screen = pg.display.set_mode((1000, 600))
clock = pg.time.Clock()
pg.display.set_caption("Tanks")
yellow_tank = Tank(["жёлтый_танчик_вверх.png",
                    "жёлтый_танчик_вниз.png",
                    "жёлтый_танчик_влево.png",
                    "жёлтый_танчик_вправо.png"], 120, 50)
grey_tank = Tank(["серый_танчик_вверх.png",
                  "серый_танчик_вниз.png",
                  "серый_танчик_влево.png",
                  "серый_танчик_вправо.png"], 930, 600)
base = pg.image.load("база.png")
bombs = pg.sprite.Group()
bombs.add(
    Bomb(100, 100),
    Bomb(440, 67),
    Bomb(900, 330),
    Bomb(754, 500),
    Bomb(325, 234),
    Bomb(234, 432),
    Bomb(856, 213),
    Bomb(763, 278),
    Bomb(182, 118),
    Bomb(75, 391),
    Bomb(384, 350),
    Bomb(20, 513),
    Bomb(540, 303),
    Bomb(588, 104),
    Bomb(511, 481),
    Bomb(159, 259),
    Bomb(648, 70)
)
yellow_tank_can_move, grey_tank_can_move = True, True
bang = pg.transform.scale(pg.image.load("взрыв.png"), (50, 50))
while True:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            exit()
        elif i.type == pg.KEYDOWN:
            if i.key == pg.K_w:
                yellow_tank.move_up = True
                yellow_tank.move_down = False
                yellow_tank.move_left = False
                yellow_tank.move_right = False
                yellow_tank.weapon = "up"
            elif i.key == pg.K_s:
                yellow_tank.move_down = True
                yellow_tank.move_up = False
                yellow_tank.move_left = False
                yellow_tank.move_right = False
                yellow_tank.weapon = "down"
            elif i.key == pg.K_a:
                yellow_tank.move_left = True
                yellow_tank.move_down = False
                yellow_tank.move_up = False
                yellow_tank.move_right = False
                yellow_tank.weapon = "left"
            elif i.key == pg.K_d:
                yellow_tank.move_right = True
                yellow_tank.move_left = False
                yellow_tank.move_down = False
                yellow_tank.move_up = False
                yellow_tank.weapon = "right"
            if i.key == pg.K_UP:
                grey_tank.move_up = True
                grey_tank.move_down = False
                grey_tank.move_left = False
                grey_tank.move_right = False
                grey_tank.weapon = "up"
            elif i.key == pg.K_DOWN:
                grey_tank.move_down = True
                grey_tank.move_up = False
                grey_tank.move_left = False
                grey_tank.move_right = False
                grey_tank.weapon = "down"
            elif i.key == pg.K_LEFT:
                grey_tank.move_left = True
                grey_tank.move_down = False
                grey_tank.move_up = False
                grey_tank.move_right = False
                grey_tank.weapon = "left"
            elif i.key == pg.K_RIGHT:
                grey_tank.move_right = True
                grey_tank.move_left = False
                grey_tank.move_down = False
                grey_tank.move_up = False
                grey_tank.weapon = "right"
            if i.key == pg.K_SPACE and not yellow_tank.made_a_shot:
                yellow_tank.made_a_shot = True
                yellow_tank.shell = Shell(yellow_tank, grey_tank)
                if yellow_tank.weapon == "up":
                    yellow_tank.shell.rect.x = yellow_tank.rect.x + 16
                    yellow_tank.shell.rect.y = yellow_tank.rect.y
                elif yellow_tank.weapon == "down":
                    yellow_tank.shell.rect.x = yellow_tank.rect.x + 16
                    yellow_tank.shell.rect.y = yellow_tank.rect.y + 45
                elif yellow_tank.weapon == "right":
                    yellow_tank.shell.rect.x = yellow_tank.rect.x + 45
                    yellow_tank.shell.rect.y = yellow_tank.rect.y + 16
                else:
                    yellow_tank.shell.rect.x = yellow_tank.rect.x
                    yellow_tank.shell.rect.y = yellow_tank.rect.y + 16
            if i.key == pg.K_KP0 and not grey_tank.made_a_shot:
                grey_tank.made_a_shot = True
                grey_tank.shell = Shell(grey_tank, yellow_tank)
                if grey_tank.weapon == "up":
                    grey_tank.shell.rect.x = grey_tank.rect.x + 16
                    grey_tank.shell.rect.y = grey_tank.rect.y
                elif grey_tank.weapon == "down":
                    grey_tank.shell.rect.x = grey_tank.rect.x + 16
                    grey_tank.shell.rect.y = grey_tank.rect.y + 45
                elif grey_tank.weapon == "right":
                    grey_tank.shell.rect.x = grey_tank.rect.x + 45
                    grey_tank.shell.rect.y = grey_tank.rect.y + 16
                else:
                    grey_tank.shell.rect.x = grey_tank.rect.x
                    grey_tank.shell.rect.y = grey_tank.rect.y + 16
        elif i.type == pg.KEYUP:
            keys = pg.key.get_pressed()
            if not keys[pg.K_w] and not keys[pg.K_d] and not keys[pg.K_a] and not keys[pg.K_s]:
                yellow_tank.move_right = False
                yellow_tank.move_left = False
                yellow_tank.move_down = False
                yellow_tank.move_up = False
            if not keys[pg.K_UP] and not keys[pg.K_DOWN] and not keys[pg.K_LEFT] and not keys[pg.K_RIGHT]:
                grey_tank.move_right = False
                grey_tank.move_left = False
                grey_tank.move_down = False
                grey_tank.move_up = False
    if not yellow_tank.win and not grey_tank.win:
        screen.fill((0, 0, 0))
        if yellow_tank_can_move:
            yellow_tank.move()
        if grey_tank_can_move:
            grey_tank.move()
        screen.blit(yellow_tank.image, yellow_tank.rect)
        screen.blit(grey_tank.image, grey_tank.rect)
        screen.blit(base, (0, 0))
        screen.blit(base, (950, 550))
        bombs.draw(screen)
        if pg.sprite.spritecollideany(yellow_tank, bombs):
            yellow_tank_can_move = False
            screen.blit(bang, yellow_tank.rect)
        if pg.sprite.spritecollideany(grey_tank, bombs):
            grey_tank_can_move = False
            screen.blit(bang, grey_tank.rect)
        if yellow_tank.made_a_shot:
            screen.blit(yellow_tank.shell.image, yellow_tank.shell.rect)
            yellow_tank.shell.fly()
        if grey_tank.made_a_shot:
            screen.blit(grey_tank.shell.image, grey_tank.shell.rect)
            grey_tank.shell.fly()
        if (not yellow_tank_can_move) and (not grey_tank_can_move):
            msg = pg.image.load("никто не победил.png")
            screen.blit(msg, (250, 250))
    elif yellow_tank.win:
        msg = pg.image.load("жёлтый победил.png")
        screen.blit(bang, grey_tank.rect)
        screen.blit(msg, (250, 250))
    elif grey_tank.win:
        msg = pg.image.load("серый победил.png")
        screen.blit(bang, yellow_tank.rect)
        screen.blit(msg, (250, 250))
    pg.display.update()
    clock.tick(120)
