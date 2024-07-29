import pygame
import time
import random

# initiate pygame
pygame.init()

# init clock and display
clock = pygame.time.Clock()
pygame.display.init()
pygame.mouse.set_visible(False)

# find current screen info
info = pygame.display.Info()
print(info.current_h)
print(info.current_w)

# create window height and width
width = 1440
height = 960
screen_size = (width,height)

# create the display surface object of specific dimension.
window = pygame.display.set_mode((screen_size), pygame.NOFRAME)
window.fill(0)

test_image3 = pygame.image.load("vernacular_mali_1.png")
test_image4 = pygame.image.load("pottery_mali.png")
test_image5 = pygame.image.load("statue_mali.png")
test_image6 = pygame.image.load("pottery_norway.png")
test_image7 = pygame.image.load("vernacular_norway_1.png")
test_image8 = pygame.image.load("vernacular_norway_2.png")

# class that creates paint objects that move randomly
class Paint():
    def __init__(self, x, y, surface, image, offset):
        self.x = x
        self.y = y
        self.offset_x = offset - self.x
        self.offset_y = 470 - self.y
        self.surface = surface
        self.image = image
        self.get_color(self.image)
        self.radius = 1
        self.directions_x = [-4, -3, -2, -1, 0, 1, 2, 3, 4]
        self.directions_y = [-4, -3, -2, -1, 0, 1, 2, 3, 4]
        # self.directions_x = [-2, -1, 0, 1, 2]
        # self.directions_y = [-2, -1, 0, 1, 2]
        self.speed = 0
        
    # takes the color of the pixel at a given location to give to the paint function
    def get_color(self, image):
        if self.x + self.offset_x >= image.get_width() or self.x + self.offset_x <= 0:
            return 
        if self.y + self.offset_y >= image.get_height() or self.y + self.offset_y <= 0:
            return
        self.color = image.get_at((self.x + self.offset_x, self.y + self.offset_y))

    # moves the paint objects in given directions
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
test_x = random.randint(0, width)
test_y = random.randint(0, height)
for i in range(200):
    test_paint.append(Paint(test_x, test_y, window, test_image3, 720))
test_paint2 = []
test_x = random.randint(0, width)
test_y = random.randint(0, height)
for i in range(200):
    test_paint2.append(Paint(test_x, test_y, window, test_image4, 720))
test_paint3 = []
test_x = random.randint(0, width)
test_y = random.randint(0, height)
for i in range(200):
    test_paint3.append(Paint(test_x, test_y, window, test_image5, 720))
test_paint4 = []
test_x = random.randint(0, width)
test_y = random.randint(0, height)
for i in range(200):
    test_paint4.append(Paint(test_x, test_y, window, test_image6, 720))
test_paint5 = []
test_x = random.randint(0, width)
test_y = random.randint(0, height)
for i in range(200):
    test_paint5.append(Paint(test_x, test_y, window, test_image7, 720))
test_paint6 = []
test_x = random.randint(0, width)
test_y = random.randint(0, height)
for i in range(200):
    test_paint6.append(Paint(test_x, test_y, window, test_image8, 720))

while True:
    # window.fill(0)

    if (pygame.time.get_ticks()/1000) < 120:
        for i in range(200):
            test_paint[i].paint()
        for i in range(200):
            test_paint2[i].paint()
        for i in range(200):
            test_paint3[i].paint()
        for i in range(200):
            test_paint4[i].paint()
        for i in range(200):
            test_paint5[i].paint()
        for i in range(200):
            test_paint6[i].paint()
    else:
            pygame.image.save(window, "testing.png")

    pygame.display.update()
    clock.tick(120)