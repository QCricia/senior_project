import pygame
import time
import random

# initiate pygame
pygame.init()

# init clock and display
clock = pygame.time.Clock()
pygame.display.init()
pygame.mouse.set_visible(False)

# create window height and width
width = 800
height = 800
screen_size = (width,height)

# create the display surface object of specific dimension.
window = pygame.display.set_mode((screen_size), pygame.NOFRAME)
window.fill(0)

test_image = pygame.image.load("images/testing.png")
test_image2 = pygame.image.load("images/testing2.png")

# class that creates paint objects that move randomly
class Paint():
    def __init__(self, x, y, surface, image, offset):
        self.x = x
        self.y = y
        self.offset = offset
        self.surface = surface
        self.image = image
        self.get_color(self.image)
        self.radius = 1
        self.directions_x = [-4, -3, -2, -1, 0, 1, 2, 3, 4]
        self.directions_y = [-4, -3, -2, -1, 0, 1, 2, 3, 4]
        # self.directions_x = [-2, -1, 0, 1, 2]
        # self.directions_y = [-2, -1, 0, 1, 2]
        self.speed = 0
        

    def get_color(self, image):
        if self.x + self.offset >= image.get_width() or self.x + self.offset <= 0:
            return 
        if self.y + self.offset >= image.get_height() or self.y + self.offset <= 0:
            return
        self.color = image.get_at((self.x + self.offset, self.y + self.offset))

    def paint(self):
        self.get_color(self.image)
        self.speed += 1
        if self.speed%2 != 0:
            return
        self.x += self.directions_x[random.randint(0, len(self.directions_x) - 1)]
        self.y += self.directions_y[random.randint(0, len(self.directions_y) - 1)]
        if self.color[3] == 0:
            return
        pygame.draw.circle(self.surface, self.color, (self.x, self.y), self.radius, 0)

test_paint = []
for i in range(200):
    test_paint.append(Paint(200, 200, window, test_image, 200))
test_paint2 = []
for i in range(200):
    test_paint2.append(Paint(400, 400, window, test_image2, 100))

while True:
    # window.fill(0)

    

    if (pygame.time.get_ticks()/1000) < 60:
        for i in range(200):
            test_paint[i].paint()
    # elif (pygame.time.get_ticks()/1000) < 120:
        # for i in range(200):
        #     test_paint2[i].paint()

    pygame.display.update()
    clock.tick(120)