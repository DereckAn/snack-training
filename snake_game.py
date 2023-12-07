import pygame 
from pygame.locals import K_ESCAPE, KEYDOWN, K_LEFT, K_RIGHT, K_UP, K_DOWN, QUIT
import time 

SIZE = 40 # Esto es para el tamaño de la imagen

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
        
        

        

class Game:
    def __init__(self): # This is the constructor
        pygame.init()
        self.screen = pygame.display.set_mode((1500, 1000)) # Esto es para la ventana # con el self. estamos haciendo que la variable sea global-- class member 
        self.screen.fill((255, 255, 255)) # Esto es para el color de la ventana
        self.snake = Snake(self.screen, 5)
        self.snake.draw()
    
    def run(self):
        running = True
        
        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN: # Esto es para ver si se presiono una tecla
                    if event.key == K_ESCAPE: # Esto es para ver si se presiono la tecla ESC
                        running = False
                    if event.key == K_LEFT:
                        self.snake.move_left()
                    if event.key == K_RIGHT:
                        self.snake.move_right()
                    if event.key == K_UP:
                        self.snake.move_up()
                    if event.key == K_DOWN:
                        self.snake.move_down()
                elif event.type == QUIT:
                    running = False
                    
            self.snake.walk()
            time.sleep(0.3) # 0.3 seconds move. It moves every 0.3 seconds
                


if __name__ == "__main__":
    game = Game()
    game.run()
    
    
    pygame.display.set_caption("Snake Game") # Esto es para el titulo de la ventana
    pygame.display.flip() # Esto es para actualizar la ventana
    
    
    
    