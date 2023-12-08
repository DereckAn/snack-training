import pygame
from pygame.locals import K_ESCAPE, KEYDOWN, K_LEFT, K_RIGHT, K_UP, K_DOWN, QUIT, K_RETURN
import time
import random

SIZE = 40 # Esto es para el tamaño de la imagen
SCREEN_X = 1500
SCREEN_Y = 1000
BACKGROUND_COLOR = (255, 255, 255) # Esto es para el color de la ventana
INITIAL_LENGTH = 5

class Apple:
    def __init__(self, screen_p):
        self.image = pygame.image.load("apple.jpg").convert()
        self.screen_p = screen_p
        self.x = SIZE * random.randint(0, (SCREEN_X-SIZE) // SIZE) # Posición aleatoria en el eje x
        self.y = SIZE * random.randint(0, (SCREEN_Y-SIZE) // SIZE) # Posición aleatoria en el eje y
        
    def draw(self):
        self.screen_p.blit(self.image, (self.x, self.y))
        pygame.display.update()
        
    def move(self):
        self.x = SIZE * random.randint(0, (SCREEN_X-SIZE) // SIZE) # Nueva posición aleatoria en el eje x
        self.y = SIZE * random.randint(0, (SCREEN_Y-SIZE) // SIZE) # Nueva posición aleatoria en el eje y

class Snake:
    def __init__(self, screen_p, length):
        self.length = length
        self.screen_p = screen_p
        self.block = pygame.image.load("block.jpg").convert()
        self.block_x = [SIZE]*length # Esto es para que la imagen se mueva en el eje x
        self.block_y = [SIZE]*length # Esto es para que la imagen se mueva en el eje y
        self.direction = "right"
    
    def draw(self):
        self.screen_p.fill((255, 255, 255))
        for i in range(self.length):
            self.screen_p.blit(self.block, (self.block_x[i], self.block_y[i])) # Esto es para poner la imagen en una posicion especifica
        pygame.display.update()
    
    def move_left(self):
        self.direction = "left"
        
    def move_right(self):
        self.direction = "right"
        
    def move_up(self):
        self.direction = "up"
        
    def move_down(self):
        self.direction = "down"
        
    def walk(self):
        for i in range(self.length-1, 0, -1):
            self.block_x[i] = self.block_x[i-1]
            self.block_y[i] = self.block_y[i-1]
        
        if self.direction == "right":
            self.block_x[0] += SIZE
        if self.direction == "left":
            self.block_x[0] -= SIZE
        if self.direction == "up":
            self.block_y[0] -= SIZE
        if self.direction == "down":
            self.block_y[0] += SIZE
            
        self.draw()
    
    
    def increase_length(self):
        self.length += 1
        self.block_x.append(-1)
        self.block_y.append(-1)
        
        

        

class Game:
    running = True
    def __init__(self): # This is the constructor
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_X, SCREEN_Y)) # Esto es para la ventana # con el self. estamos haciendo que la variable sea global-- class member
        self.screen.fill(BACKGROUND_COLOR) # Esto es para el color de la ventana
        self.snake = Snake(self.screen, INITIAL_LENGTH)
        self.snake.draw()
        self.apple = Apple(self.screen)
        self.apple.draw()
        
    def play(self):
        self.snake.walk()
        self.display_score()
        
        #Collision with apple
        if self.snake.block_x[0] == self.apple.x and self.snake.block_y[0] == self.apple.y:
            self.snake.increase_length()
            self.apple.move()
            
        self.apple.draw()

        #Collision with snake body
        for i in range(1, self.snake.length):
            if self.snake.block_x[i] == self.apple.x and self.snake.block_y[i] == self.apple.y:
                self.apple.move()
        
        for (block_x, block_y) in zip(self.snake.block_x[1:], self.snake.block_y[1:]):
            if self.snake.block_x[0] == block_x and self.snake.block_y[0] == block_y:
                raise "Hit the body error"

        # Collision with the boundaries
        if not (0 <= self.snake.block_x[0] <= SCREEN_X and 0 <= self.snake.block_y[0] <= SCREEN_Y):
            raise "Hit the boundary error"
        
    
    def show_game_over(self):
        self.screen.fill(BACKGROUND_COLOR)
        font = pygame.font.SysFont('arial', 30)
        line1 = font.render(f"Game is over! Your score is {self.snake.length - INITIAL_LENGTH}", True, (200, 200, 200))
        self.screen.blit(line1, (200, 300))
        line2 = font.render(f"To play again press Enter. To exit press Escape!", True, (200, 200, 200))
        self.screen.blit(line2, (200, 350))
        pygame.display.update()
    
    def display_score(self):
        font = pygame.font.SysFont('arial', 30)
        score = font.render(f"Score: {self.snake.length - INITIAL_LENGTH}", True, (200, 200, 200))
        self.screen.blit(score, (SCREEN_X-200, 10))
        
    def reset(self):
        self.snake = Snake(self.screen, INITIAL_LENGTH)
        self.apple = Apple(self.screen)
                

    def run(self):
        pause = False
        while self.running:
            for event in pygame.event.get():
                if event.type == KEYDOWN: # Esto es para ver si se presiono una tecla
                    if event.key == K_ESCAPE: # Esto es para ver si se presiono la tecla ESC
                        self.running = False
                    if event.key == K_RETURN:
                        pause = False
                        
                    if not pause:
                        if event.key == K_LEFT:
                            self.snake.move_left()
                        if event.key == K_RIGHT:
                            self.snake.move_right()
                        if event.key == K_UP:
                            self.snake.move_up()
                        if event.key == K_DOWN:
                            self.snake.move_down()
                elif event.type == QUIT:
                    self.running = False
            try:
                if not pause:
                    self.play()
            except Exception as e:
                self.show_game_over()
                pause = True
                self.reset()
                
            time.sleep(0.1) # 0.3 seconds move. It moves every 0.3 seconds
                
    

if __name__ == "__main__":
    game = Game()
    game.run()
    
    
    pygame.display.set_caption("Snake Game") # Esto es para el titulo de la ventana
    # pygame.display.flip() # Esto es para actualizar la ventana
    
    
    
    