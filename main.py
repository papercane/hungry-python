
import sys, random
import pygame as pg
from pygame.math import Vector2

pg.init()

# game variables
WINDOW = 550

# colours
BLACK = (0,0,0)
GREEN = (206,210,175)
DARK = (134,178,163)
PINK = (247,159,153)
YELLOW = (253,207,175)

cell_size = 20
number_of_cells = 25

screen = pg.display.set_mode((cell_size*number_of_cells, cell_size*number_of_cells))
pg.display.set_caption("hungry hungry snake")
clock = pg.time.Clock()

class Food:
    def __init__(self, snake_body) -> None:
        self.position = self.generate_random_pos(snake_body)
    def draw(self):
        # draw this on rect surface for collision detection
        food_rect = pg.Rect(self.position.x * cell_size, self.position.y * cell_size,
                            cell_size,cell_size)
        pg.draw.rect(screen, DARK , food_rect, 0, 10)
    
    def generate_random_cell(self):
        x = random.randint(0, number_of_cells - 1)
        y = random.randint(0, number_of_cells - 1)
        return Vector2(x,y)

    def generate_random_pos(self, snake_body):
        position = self.generate_random_cell()
        
        while position in snake_body:
            position = self.generate_random_cell()
        return position
    
class Snake:
    def __init__(self) -> None:
        self.body = [Vector2(6,9), Vector2(5,9), Vector2(4,9)]
        self.direction = Vector2(1,0)
        self.add_segment = False
    def draw(self):
        for segment in self.body:
            segment_rect = (segment.x * cell_size, segment.y * cell_size,
                            cell_size, cell_size)
            pg.draw.rect(screen, PINK, segment_rect, 0 , 5)
    def update(self):
        self.body.insert(0, self.body[0] + self.direction)
        if self.add_segment == True:
            self.add_segment = False
            
        else:
            self.body = self.body[:-1] # selecting all elements in the list execpt for the last one
    def reset(self):
        self.body = [Vector2(6,9), Vector2(5,9), Vector2(4,9)]
        self.direction = Vector2(1,0)
    
class Game:
    def __init__(self) -> None:
        self.snake = Snake()
        self.food = Food(self.snake.body)
        self.state = "RUNNING"
    def draw(self):
        self.snake.draw()
        self.food.draw()
        
    def update(self):
        if self.state == "RUNNING":
            self.snake.update()
            self.check_eat()
            self.check_border()
        
    def check_eat(self):
        if self.snake.body[0] == self.food.position:
            self.food.position = Vector2(self.food.generate_random_pos(self.snake.body))
            self.snake.add_segment = True

            
    def check_border(self):
        if self.snake.body[0].x == number_of_cells or self.snake.body[0].x == -1:
            self.game_over()
        if self.snake.body[0].y == number_of_cells or self.snake.body[0].y == -1:
            self.game_over()
            
    def game_over(self):
        self.snake.reset()
        self.food.position = Vector2(self.food.generate_random_pos(self.snake.body))
        self.state = "STOP"

UPDATE_SNAKE = pg.USEREVENT
pg.time.set_timer(UPDATE_SNAKE, 200)

game = Game()

# game loop
while True:
    
    for event in pg.event.get():
        #endloop
        if event.type == pg.QUIT:
            pg.display.quit()
            pg.quit()
            sys.exit()
            
        if event.type == UPDATE_SNAKE:
            game.update()
            
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_UP and game.snake.direction != Vector2(0,1):
                game.snake.direction = Vector2(0, -1)
            elif event.key == pg.K_DOWN and game.snake.direction != Vector2(0, -1):
                game.snake.direction = Vector2(0,1)
            elif event.key == pg.K_LEFT and game.snake.direction != Vector2(1,0):
                game.snake.direction = Vector2(-1,0)
            elif event.key == pg.K_RIGHT and game.snake.direction != Vector2(-1,0):
                game.snake.direction = Vector2(1,0)
            
   
    
    
    # update objects
    #draw
    screen.fill(GREEN)
    game.draw()
    
    #pg.display.flip()
    pg.display.update()
    clock.tick(60)
    
