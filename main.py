import pygame
from logic.snake import Snake
from logic.food import Food

def main():
    pygame.init()  # initialise pygame

    width, height = 600, 400
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Snake Game')

    # Main Game Loop
    running = True
    clock = pygame.time.Clock()
    snake_speed = 20

    print("Creating Snake object...")
    snake = Snake(width, height)  # create a snake from snake class / create an instance of snake
    print("Snake object created. Body:", snake.body)
    food = Food(snake)

    while running:
        for event in pygame.event.get():  # checks each event that happens in game
            if event.type == pygame.QUIT:  # .QUIT is pressing on the X on display
                running = False
            elif event.type == pygame.KEYDOWN:  # USER INPUT
                if event.key == pygame.K_w:
                    snake.change_dir('UP')
                elif event.key == pygame.K_s:
                    snake.change_dir('DOWN')
                elif event.key == pygame.K_a:
                    snake.change_dir('LEFT')
                elif event.key == pygame.K_d:
                    snake.change_dir('RIGHT')

        # check for collisions
        head = snake.body[0]
        if head[0] < 0 or head[0] >= width or head[1] < 0 or head[1] >= height:
            running = False
            print("Wall collision! Game Over...")
            break

        if head in snake.body[1:]:
            running = False
            print("Self collision! Game Over...")
            break

        # check if snake eats food
        if pygame.Rect(snake.body[0], (snake.size, snake.size)).colliderect(food.get_rect()):
            snake.grow()
            food.new_position()

        snake.move()

        # Color inside screen
        screen.fill((0, 0, 0))

        # Update display
        snake.draw(screen)
        food.draw(screen)
        pygame.display.flip()

        clock.tick(snake_speed)  # how fast the game moves

    # Quit Pygame
    pygame.quit()


if __name__ == '__main__':
    main()