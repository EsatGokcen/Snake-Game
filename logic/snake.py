import pygame

class Snake:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.size = 10
        self.body = [
            [width // 2, height // 2]
        ]  # center the snake in screen, two lists so we can add more segments to snake
        self.direction = 'RIGHT'
        self.change_to = self.direction

    def change_dir(self, direction):  # MOVEMENT RESTRICTIONS
        if direction == 'UP' and self.direction != 'DOWN':
            self.direction = 'UP'
        if direction == 'DOWN' and self.direction != 'UP':
            self.direction = 'DOWN'
        if direction == 'LEFT' and self.direction != 'RIGHT':
            self.direction = 'LEFT'
        if direction == 'RIGHT' and self.direction != 'LEFT':
            self.direction = 'RIGHT'

    def move(self):  # HOW SNAKE REACT TO USER INPUT
        head = self.body[0]
        if self.direction == 'UP':
            new_head = [head[0], head[1] - self.size]
        if self.direction == 'DOWN':
            new_head = [head[0], head[1] + self.size]
        if self.direction == 'LEFT':
            new_head = [head[0] - self.size, head[1]]
        if self.direction == 'RIGHT':
            new_head = [head[0] + self.size, head[1]]

        self.body = [new_head] + self.body[:-1]

    def grow(self):
        self.body.append(self.body[-1])

    def draw(self, screen):  # DRAW SNAKE ON SCREEN
        for segment in self.body:  # snake is divided into sections
            pygame.draw.rect(screen, (0, 255, 0),
                             pygame.Rect(segment[0], segment[1], self.size, self.size))

    def get_head_rect(self):  # for collision
        head = self.body[0]
        return pygame.Rect(head[0], head[1], self.size, self.size)