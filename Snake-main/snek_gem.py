import pygame, random,sys
from pygame.math import Vector2
from random import randint

class snek:
    def __init__(self):
        self.body = [Vector2(7,10), Vector2(6,10), Vector2(5,10)]
        self.direction = Vector2(1,0)
        self.new_block = False
    def draw_snek(self):
        for block in self.body:
            snek_rect = pygame.Rect(block.x  * cell_size, block.y * cell_size,cell_size,cell_size)
            pygame.draw.rect(window, (255, 255, 0), snek_rect)
    def move_snek(self):
        if self.new_block == True:
            body_copy = self.body[:]
            body_copy.insert(0,body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0,body_copy[0] + self.direction)
            self.body = body_copy[:]
    def add_block(self):
        self.new_block = True
class fruit:
    def __init__(self):
        self.randomize()

    def draw_fruit(self):
        fruit_rect = pygame.Rect(self.pos.x  * cell_size, self.pos.y * cell_size,  cell_size, cell_size)
        pygame.draw.rect(window, (255, 175, 57), fruit_rect)
    def randomize(self):
        self.x = randint(0, cell_number - 1)
        self.y =  randint(0, cell_number - 1)
        self.pos = Vector2(self.x, self.y)
class main:
    def __init__(self):
        self.snake = snek()
        self.fruit = fruit()


    def update(self):
        self.snake.move_snek()
    def draw_stuff(self):
        self.snake.draw_snek()
        self.fruit.draw_fruit()
    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.randomize()

            self.snake.add_block()
    def check_fail(self):
        if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number:
            self.game_over()
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()
    def game_over(self):
        pygame.quit()
        sys.exit()
        
pygame.init()
cell_size = 40
cell_number = 20
window = pygame.display.set_mode((cell_size * cell_number, 750))
pygame.display.set_caption('Snek')
clock = pygame.time.Clock()

fruity = fruit()

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE,  150)
run = True
snake = snek()
game = main()
main = main()
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == SCREEN_UPDATE:
            game.update()
            main.snake.move_snek()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                main.snake.direction = Vector2(0, -1)
            if event.key == pygame.K_DOWN:
                main.snake.direction = Vector2(0, 1)
            if event.key == pygame.K_LEFT:
                main.snake.direction = Vector2(-1, 0)
            if event.key == pygame.K_RIGHT:
                main.snake.direction = Vector2(1, 0)
    window.fill((0, 255, 255))
    main.draw_stuff()
    main.check_collision()
    main.check_fail()
    pygame.display.update()
    clock.tick(120)
pygame.quit()
