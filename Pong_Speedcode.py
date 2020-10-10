import pygame

#ispisano za 1h i 20min!!!

win_height = 600
win_width = 1000

win = pygame.display.set_mode((win_width, win_height))

pygame.display.set_caption("Pong Speedcode")

class Block(object):
    def __init__(self, x, y, width, height, vel):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = vel

    def move_up(self):
        self.y -= self.vel

    def move_down(self):
        self.y += self.vel

class Ball(object):
    def __init__(self, x, y, r, velx, vely, speed_up):
        self.x = x
        self.y = y
        self.r = r
        self.velx = velx
        self.vely = vely
        self.speed_up = speed_up

    def move (self):
        self.x += self.velx
        self.y += self.vely

    def collision_block (self, Block1, Block2):
        if (self.x <= Block1.x + Block1.width) and (self.y >= Block1.y) and (self.y <= Block1.y + Block1.height):
            self.velx -= self.speed_up
            return (True)
        elif (self.x >= Block2.x) and (self.y >= Block2.y) and (self.y <= Block2.y + Block2.height):
            self.velx += self.speed_up
            return (True)
        else:
            return (False)

    def collision_win (self, win_height):
        if (self.y <= 0) or (self.y >= win_height):
            return (True)
        else:
            return (False)

    def out_of_bounds(self, win_width):
        if (self.x <= 0) or (self.x >= win_width):
            return (True)
        else:
            return (False)

def reset (Block1, Block2, Ball):
    Block1.x = 50
    Block1.y = 300
    Block2.x = 950
    Block2.y = 300
    Ball.x = 500
    Ball.y = 300
    Ball.velx = 5
    Ball.vely = 5

Block1 = Block(50, 300, 15, 130, 6)
Block2 = Block(950, 300, 15, 130, 6)
Ball = Ball(500, 300, 8, 5, 5, 1)

run = True
while run:

    pygame.time.delay(20)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    key = pygame.key.get_pressed()

    if (key[pygame.K_w]) and (Block1.y > 0):
        Block1.move_up()
    if (key[pygame.K_s]) and (Block1.y + Block1.height< win_height):
        Block1.move_down()
    if (key[pygame.K_UP]) and (Block2.y > 0):
        Block2.move_up()
    if (key[pygame.K_DOWN]) and (Block2.y + Block2.height < win_height):
        Block2.move_down()

    if Ball.collision_block(Block1, Block2):
        Ball.velx *= -1

    if Ball.collision_win(win_height):
        Ball.vely *= -1

    if Ball.out_of_bounds(win_width):
        reset(Block1, Block2, Ball)

    Ball.move()

    win.fill((0, 0, 0))
    pygame.draw.rect(win, (255, 255, 255), (Block1.x, Block1.y, Block1.width, Block1.height))
    pygame.draw.rect(win, (255, 255, 255), (Block2.x, Block2.y, Block2.width, Block2.height))
    pygame.draw.circle(win, (255, 255, 255), (Ball.x, Ball.y), Ball.r, 0)
    pygame.display.update()

pygame.quit()






