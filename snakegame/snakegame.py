import pygame
import random

#Let's you initilze all the modules from the pyagame
pygame.init()
running= True
clock= pygame.time.Clock()

# Create a screen
window_h= 1500
window_w= 1500
screen= pygame.display.set_mode((window_h,window_w))

#initialize the snake
class Snake:
    def __init__(self):
        self.body=[[window_h//2, window_w//2]]
        self.grow= False
        self.direction= "UP"

    def snake_movements(self):
        head= self.body[0][:]
        if self.direction=="UP":
            head[1]+=15
        if self.direction=="DOWN":
            head[1]-=15
        if self.direction=="RIGHT":
            head[0]+=15
        if self.direction=="LEFT":
            head[0]-=15

        self.body.insert(0, head)
        if not self.grow:
            self.body.pop()
        else:
            self.grow = False

    def growth(self):
        self.grow= True

    def direction_change(self, direction):
        if direction=="UP" and self.direction!="DOWN":
            self.direction= direction
        if direction=="DOWN" and self.direction!="UP":
            self.direction= direction
        if direction=="LEFT" and self.direction!="RIGHT":
            self.direction= direction
        if direction=="RIGHT" and self.direction!="LEFT":
            self.direction= direction
      
#randomize the fruit
class Fruit:
    def __init__(self):
        self.position= [random.randint(100,1400), random.randint(100,1400)]
        self.ate= False
    
    def draw_fruit(self):
        pygame.draw.rect(screen, 'red', pygame.Rect(self.position[0], self.position[1],15,15))
        if self.ate:
            self.position= [random.randint(100,1400), random.randint(100,1400)]
            self.ate= False
           
#Check for the snake collision
def snake_collision(snake):
    # if snake collides with the borders of the screen
    if snake.body[0][0] >= window_w or snake.body[0][0]<0 or snake.body[0][1]>= window_h or snake.body[0][1]<0:
        return True
    
    #if the snake collides with itself:
    if snake.body[0] in snake.body[1:]:
        return True
    
    return False

#Snake growth on eating the fruits
def snake_ate(snake, fruit):
    if snake.body[0] == fruit.position:
        fruit.ate = True
        snake.growth()

#main game loop
snake= Snake()
fruit= Fruit()

while running:
    screen.fill('black')

    #end of the game when you'X" the game
    for event in pygame.event.get():
        if event.type== pygame.quit:
            running= False
        elif event.type==pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.direction_change('UP')
            elif event.key == pygame.K_DOWN:
                snake.direction_change('DOWN')
            elif event.key == pygame.K_LEFT:
                snake.direction_change('LEFT')
            elif event.key == pygame.K_RIGHT:
                snake.direction_change('RIGHT')

    snake.snake_movements()
    snake_ate(snake, fruit)

    if snake_collision(snake):
        running = False

    fruit.draw_fruit()
    
    for block in snake.body:
        pygame.draw.rect(screen, 'green', pygame.Rect(block[0], block[1], 15, 15))

    pygame.display.update()
    clock.tick(15)

pygame.quit()




