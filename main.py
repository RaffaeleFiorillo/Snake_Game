import pygame
from random import randint

pygame.init()
pygame.font.init()
SCREEN = pygame.display.set_mode((500, 500))
CLOCK = pygame.time.Clock()
text_font = pygame.font.SysFont('Times New Roman', 12)


class Snake:
    def __init__(self):
        self.body_coordinates = [(randint(15, 35), randint(15, 35))]
        self.should_grow = False

    def move(self, vector, food_coo):
        head_coo = [(self.body_coordinates[0][0] + vector[0], self.body_coordinates[0][1] + vector[1])]
        self.body_coordinates = [coo for coo in self.body_coordinates[:-1]]
        self.body_coordinates = head_coo + self.body_coordinates
        if self.body_coordinates[0] == food_coo:
            self.should_grow = True


class Food:
    def __init__(self, snake_body_coo):
        self.coordinates = (randint(0, 49), randint(0, 49))
        while self.coordinates in snake_body_coo:
            self.coordinates = [(randint(0, 49), randint(0, 49))]


class World:
    def __init__(self):
        self.last_vector = (0, 0)
        self.SNAKE = Snake()
        self.FOOD = Food(self.SNAKE.body_coordinates)
        self.make_snake_grow, self.last_food_coo = False, None

    def move_snake(self, key=False):
        if key:
            key_effects = {pygame.K_RIGHT: (1, 0), pygame.K_LEFT: (-1, 0), pygame.K_UP: (0, -1), pygame.K_DOWN: (0, 1)}
            self.last_vector = key_effects[key]
        self.SNAKE.move(self.last_vector, self.FOOD.coordinates)

    def snake_growth(self):
        if self.SNAKE.should_grow:
            self.last_food_coo = self.FOOD.coordinates
            self.FOOD = Food(self.SNAKE.body_coordinates)
            self.SNAKE.should_grow = False
        if self.last_food_coo and self.SNAKE.body_coordinates[-1] == self.last_food_coo:
            self.SNAKE.body_coordinates.append(self.last_food_coo)
            self.last_food_coo = None

    def verify_death_condition(self):
        for coo in self.SNAKE.body_coordinates[1:]:
            if self.SNAKE.body_coordinates[0] == coo:
                pygame.time.wait(200)
                exit()

    def adjust_snake_position(self):
        self.SNAKE.body_coordinates[0] = (self.SNAKE.body_coordinates[0][0]%50, self.SNAKE.body_coordinates[0][1]%50)

    def draw(self):
        [pygame.draw.rect(SCREEN, (0, 0, 0), (10*i, 10*y, 10, 10)) for y in range(50) for i in range(50)]
        head_coo = self.SNAKE.body_coordinates[0]
        pygame.draw.rect(SCREEN, (0, 200, 200), (10 * head_coo[0], 10 * head_coo[1], 10, 10))
        [pygame.draw.rect(SCREEN, (0, 255, 0), (10*i, 10*y, 10, 10)) for i, y in self.SNAKE.body_coordinates[1:]]
        pygame.draw.rect(SCREEN, (255, 255, 0), (10 * self.FOOD.coordinates[0], 10 * self.FOOD.coordinates[1], 10, 10))


def manage_events():
    directions = [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN and event.key in directions:
            world.move_snake(event.key)
            return None
    world.move_snake()


def refresh():
    world.draw()
    world.adjust_snake_position()
    SCREEN.blit(text_font.render(str(len(world.SNAKE.body_coordinates)), True, (255, 0, 0)), (5, 3))
    pygame.display.update()


world = World()
while True:
    CLOCK.tick(20)
    world.snake_growth()
    manage_events()
    refresh()
    world.verify_death_condition()
