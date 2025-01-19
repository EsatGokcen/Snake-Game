import random
import pygame
from logic.snake import Snake

class Food:

    def __init__(self, snake: Snake):
        self.size = 10
        self.color = (255, 0, 0)  # red
        self.snake = snake
        self.position = self.generate_position()

    def generate_position(self):
        while True:
            position = [random.randrange(1, self.snake.width // self.size) * self.size,
                        random.randrange(1, self.snake.height // self.size) * self.size]
            if position not in self.snake.body:  # ensure food is not placed on the snake
                return position

    def draw(self, screen: pygame.Surface):
        pygame.draw.rect(screen, self.color,
                         [self.position[0], self.position[1],
                          self.size, self.size])

    def new_position(self):
        self.position = self.generate_position()

    def get_rect(self):
        return pygame.Rect(self.position[0], self.position[1], self.size, self.size)