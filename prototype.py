import pygame
import time
import random

# initiate pygame
pygame.init()

# for writing text on the screen
pygame.font.init() 
                   
my_font = pygame.font.Font('Flux_Architect_Regular.ttf', 30)

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

# an array with all the image names as strings, so I can initialize images in for loop
image_names = ["mali_1.png", "mali_2.png", "mali_3.png", "mali_4.png", "mali_5.png", "mali_6.png",
               "columbia_1.png", "columbia_2.png", "columbia_3.png", "columbia_4.png", 
               "norway_1.png", "norway_2.png", "norway_3.png", 
               "cameroon_1.png", "cameroon_2.png", "cameroon_3.png", "cameroon_4.png", 
               "china_1.png", "china_2.png", "china_3.png", "china_4.png", "china_5.png",
               "denmark_1.png", "denmark_2.png",
               "ethiopia_1.png","ethiopia_2.png", "ethiopia_3.png",
               "ghana_1.png", "ghana_2.png",
               "greece_1.png", "greece_2.png",
               "indonesia_1.png", "indonesia_2.png", "indonesia_3.png",
               "inuit_1.png",
               "iraq_1.png", "iraq_2.png",
               "japan_1.png", "japan_2.png", "japan_3.png", "japan_4.png",
               "mexico_1.png", "mexico_2.png",
               "myanmar_1.png", "myanmar_2.png",
               "navajo_1.png",
               "new_zealand_1.png", "new_zealand_2.png"] 

# create an array with all of the image objects
image_objects = []
for i in range(len(image_names)):
    image_objects.append(pygame.image.load(image_names[i]))

class Scrapbook():
    def __init__(self, scraps, place_names, speed, surface):
        self.images = scraps
        self.places = place_names
        self.surface = surface
        self.paints = []
        self.time_range = speed
        
        self.initialize_array()
        
        self.index = random.randint(1, len(self.paints) - 1)
            
    # class that creates paint objects that move randomly
    class Paint():
        def __init__(self, x, y, surface, image):
            self.x = x
            self.y = y
            self.start = [x, y]
            self.offset_x = 720 - self.x
            self.offset_y = 470 - self.y
            self.surface = surface
            self.image = image
            self.get_color(self.image)
            self.radius = 1
            self.directions_x = [-4, -3, -2, -1, 0, 1, 2, 3, 4]
            self.directions_y = [-4, -3, -2, -1, 0, 1, 2, 3, 4]
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
           
    def initialize_array(self):
        # array that contains arrays of paint objects
        self.paints = []

        # adds a paint object array for every image in image_objects
        for j in range(len(self.images)):
            paint_loop = []
            test_x = random.randint(0, width)
            test_y = random.randint(0, height)
            for i in range(200):
                paint_loop.append(self.Paint(test_x, test_y, window, self.images[j]))
            self.paints.append(paint_loop)
           
    # using the given time constraints, run the scrapbook, pasting images and places names 
    def get_crafting(self):
        if (pygame.time.get_ticks()/1000) < self.time_range:
            for i in range(200):
                self.paints[self.index][i].paint()
            for k in range(200):
                self.paints[self.index - 1][k].paint()
        elif (pygame.time.get_ticks()/1000) <= (self.time_range + 0.01):
            self.paints.pop(self.index)
            self.paints.pop(self.index - 1)
            self.index = random.randint(1, len(self.paints) - 1)
            self.time_range += 30
            
    def print_place(self):
        t = pygame.time.get_ticks()/1000
        if (t) < 0.5:
            print(self.places[self.index])
            print(self.places[self.index - 1])
        if (t) > self.time_range and (t) <= (self.time_range + 0.01):
            self.places.pop(self.index)
            self.places.pop(self.index - 1)
   
vernacular_sketchbook = Scrapbook(image_objects, image_names, 30, window) 

test_text_surface = my_font.render(image_names[0][0:-6].upper(), False, (255, 255, 255))

while True:
    # vernacular_sketchbook.get_crafting()
    
    window.blit(test_text_surface, (300,300))
    
    # vernacular_sketchbook.print_place()
    # if (pygame.time.get_ticks()/1000) > 120:
    #     print("yes")
    #     pygame.image.save(window, "testing.png")
    pygame.display.update()
    clock.tick(240)