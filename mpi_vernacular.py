#!/usr/bin/env python
import os
import os.path
import sys
import pygame
from pygame.locals import *
import time
import random
from mpi4py import MPI

# initiate pygame and give permission to use pygame's functionality.
pygame.init()

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# set window position
os.environ['SDL_VIDEO_WINDOW_POS'] = "0,0"
# get this display
os.environ['DISPLAY'] = ':0.0'
# with caffeine installed (sudo apt install caffeine) we can wake the screen
os.system('caffeinate sleep 1') # passes caffeinate out to shell to wake screensaver 

# init clock and display
clock = pygame.time.Clock()
pygame.display.init()
pygame.mouse.set_visible(False)

# get the screen hight and width
disp_info = pygame.display.Info()
width = disp_info.current_w
height = disp_info.current_h
screen_size = (width,height)
universe_size = (width*2, height*2)

# set up the screen
window = pygame.display.set_mode((screen_size), pygame.NOFRAME)
window.fill(0)

# Constants
w0 = 0; h0 = 0
w1 = width; h1 = 0
w2 = 0; h2 = height
w3 = width; h3 = height
my_font = pygame.font.Font('/home/pi/work/chalaszynski/senior_project/Flux_Architect_Regular.ttf', 22)
my_font_2 = pygame.font.Font('/home/pi/work/chalaszynski/senior_project/Flux_Architect_Regular.ttf', 180)
my_font_3 = pygame.font.Font('/home/pi/work/chalaszynski/senior_project/Flux_Architect_Regular.ttf', 90)

######### from here it is the same as prototype

# an array with all the image names as strings, so I can initialize images in for loop
vernacular_names = ["/home/pi/work/chalaszynski/senior_project/mali_1.png", "/home/pi/work/chalaszynski/senior_project/mali_2.png", "/home/pi/work/chalaszynski/senior_project/mali_3.png", "/home/pi/work/chalaszynski/senior_project/mali_4.png", "/home/pi/work/chalaszynski/senior_project/mali_5.png", "/home/pi/work/chalaszynski/senior_project/mali_6.png",
               "/home/pi/work/chalaszynski/senior_project/columbia_1.png", "/home/pi/work/chalaszynski/senior_project/columbia_2.png", "/home/pi/work/chalaszynski/senior_project/columbia_3.png", "/home/pi/work/chalaszynski/senior_project/columbia_4.png", 
               "/home/pi/work/chalaszynski/senior_project/norway_1.png", "/home/pi/work/chalaszynski/senior_project/norway_2.png", "/home/pi/work/chalaszynski/senior_project/norway_3.png", "/home/pi/work/chalaszynski/senior_project/norway_4.png", "/home/pi/work/chalaszynski/senior_project/norway_5.png", 
               "/home/pi/work/chalaszynski/senior_project/cameroon_1.png", "/home/pi/work/chalaszynski/senior_project/cameroon_2.png", "/home/pi/work/chalaszynski/senior_project/cameroon_3.png", "/home/pi/work/chalaszynski/senior_project/cameroon_5.png", 
               "/home/pi/work/chalaszynski/senior_project/china_2.png", "/home/pi/work/chalaszynski/senior_project/china_3.png", "/home/pi/work/chalaszynski/senior_project/china_4.png", "/home/pi/work/chalaszynski/senior_project/china_5.png",
               "/home/pi/work/chalaszynski/senior_project/denmark_1.png", "/home/pi/work/chalaszynski/senior_project/denmark_2.png", "/home/pi/work/chalaszynski/senior_project/denmark_3.png",
               "/home/pi/work/chalaszynski/senior_project/ethiopia_1.png","/home/pi/work/chalaszynski/senior_project/ethiopia_2.png", "/home/pi/work/chalaszynski/senior_project/ethiopia_4.png",
               "/home/pi/work/chalaszynski/senior_project/ghana_1.png", "/home/pi/work/chalaszynski/senior_project/ghana_2.png",
               "/home/pi/work/chalaszynski/senior_project/greece_1.png", "/home/pi/work/chalaszynski/senior_project/greece_2.png", "/home/pi/work/chalaszynski/senior_project/greece_3.png",
               "/home/pi/work/chalaszynski/senior_project/indonesia_2.png", "/home/pi/work/chalaszynski/senior_project/indonesia_3.png", "/home/pi/work/chalaszynski/senior_project/indonesia_4.png", "/home/pi/work/chalaszynski/senior_project/indonesia_5.png",
               "/home/pi/work/chalaszynski/senior_project/inuit_1.png", "/home/pi/work/chalaszynski/senior_project/inuit_2.png", "/home/pi/work/chalaszynski/senior_project/inuit_3.png",
               "/home/pi/work/chalaszynski/senior_project/iraq_1.png", "/home/pi/work/chalaszynski/senior_project/iraq_2.png", "/home/pi/work/chalaszynski/senior_project/iraq_3.png", "/home/pi/work/chalaszynski/senior_project/iraq_4.png",
               "/home/pi/work/chalaszynski/senior_project/japan_1.png", "/home/pi/work/chalaszynski/senior_project/japan_2.png", "/home/pi/work/chalaszynski/senior_project/japan_3.png", "/home/pi/work/chalaszynski/senior_project/japan_4.png", "/home/pi/work/chalaszynski/senior_project/japan_5.png",
               "/home/pi/work/chalaszynski/senior_project/mexico_1.png", "/home/pi/work/chalaszynski/senior_project/mexico_2.png", "/home/pi/work/chalaszynski/senior_project/mexico_3.png",
               "/home/pi/work/chalaszynski/senior_project/myanmar_1.png", "/home/pi/work/chalaszynski/senior_project/myanmar_2.png",
               "/home/pi/work/chalaszynski/senior_project/navajo_1.png", "/home/pi/work/chalaszynski/senior_project/navajo_2.png", "/home/pi/work/chalaszynski/senior_project/navajo_3.png", "/home/pi/work/chalaszynski/senior_project/navajo_4.png",
               "/home/pi/work/chalaszynski/senior_project/new_zealand_1.png", "/home/pi/work/chalaszynski/senior_project/new_zealand_2.png", "/home/pi/work/chalaszynski/senior_project/new_zealand_3.png", "/home/pi/work/chalaszynski/senior_project/new_zealand_4.png",
               "/home/pi/work/chalaszynski/senior_project/pueblo_1.png", "/home/pi/work/chalaszynski/senior_project/pueblo_2.png", "/home/pi/work/chalaszynski/senior_project/pueblo_3.png",
               "/home/pi/work/chalaszynski/senior_project/russia_1.png", "/home/pi/work/chalaszynski/senior_project/russia_2.png", "/home/pi/work/chalaszynski/senior_project/russia_3.png", "/home/pi/work/chalaszynski/senior_project/russia_4.png", "/home/pi/work/chalaszynski/senior_project/russia_5.png",
               "/home/pi/work/chalaszynski/senior_project/saudi_arabia_1.png", "/home/pi/work/chalaszynski/senior_project/saudi_arabia_2.png", "/home/pi/work/chalaszynski/senior_project/saudi_arabia_3.png",
               "/home/pi/work/chalaszynski/senior_project/vietnam_1.png", "/home/pi/work/chalaszynski/senior_project/vietnam_2.png", "/home/pi/work/chalaszynski/senior_project/vietnam_3.png", "/home/pi/work/chalaszynski/senior_project/vietnam_4.png",
               "/home/pi/work/chalaszynski/senior_project/phillipines_1.png", "/home/pi/work/chalaszynski/senior_project/phillipines_2.png", "/home/pi/work/chalaszynski/senior_project/phillipines_3.png",
               "/home/pi/work/chalaszynski/senior_project/germany_1.png", "/home/pi/work/chalaszynski/senior_project/germany_2.png", "/home/pi/work/chalaszynski/senior_project/germany_3.png"] 

# plant_names = ["indonesia_1.png", "ethiopia_3.png", "china_1.png", "cameroon_4.png"]

# create an array with all of the image objects
vernacular_objects = []
for i in range(len(vernacular_names)):
    vernacular_objects.append(pygame.image.load(vernacular_names[i]))
    
# plant_objects = []
# for i in range(len(plant_names)):
#     plant_objects.append(pygame.image.load(plant_names[i]).convert_alpha())

class Scrapbook():
    def __init__(self, scraps, place_names, speed, surface):
        self.images = scraps
        self.places = place_names
        self.places_surface = pygame.Surface((width, height), pygame.SRCALPHA)
        self.surface = surface
        self.paints = []
        self.time_range = speed
        
        self.initialize_array()
        
        self.paint_indexes = []
        
        self.initialize_paint_indexes()
        
        self.index = random.randint(1, len(self.paint_indexes) - 1)
        self.ind = self.paint_indexes[self.index]
        self.ind_1 = self.paint_indexes[self.index - 1]
        
        self.init_place()
        
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
            
        def paint_no_image(self):
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
            
    def initialize_paint_indexes(self):
        for i in range(len(self.paints)):
            self.paint_indexes.append(i)
           
    # using the given time constraints, run the scrapbook, pasting images and places names 
    def get_crafting(self):
        if (len(self.paint_indexes)) <= 3:
            # print("hi")
            for j in range(len(self.paints)):
                for i in range(200):
                    self.paints[j][i].paint_no_image()
            return
        if (pygame.time.get_ticks()/1000) < self.time_range:
            for i in range(200):
                self.paints[self.ind][i].paint()
            for k in range(200):
                self.paints[self.ind_1][k].paint()
            self.print_place()
        elif (pygame.time.get_ticks()/1000) <= (self.time_range + 0.01):
            self.paint_indexes.pop(self.index)
            self.paint_indexes.pop(self.index - 1)
            self.index = random.randint(1, len(self.paint_indexes) - 1)
            self.ind = self.paint_indexes[self.index]
            self.ind_1 = self.paint_indexes[self.index - 1]
            self.init_place()
            self.time_range += 30
            # print(self.time_range)
            
    # turns the file names into a writeable place name, creates a text object at a randomized location, blits text object onto
    # text surface, then draws a rectangle onece behind the text(the rectangle can be covered but not the text)
    def init_place(self):
        place_name_1 = self.places[self.ind][42:-6].upper()
        place_name_2 = self.places[self.ind_1][42:-6].upper()
        if place_name_1 == place_name_2:
            self.different_places = False
        else:
            self.different_places = True
        self.place_text_surface_1 = my_font.render(place_name_1, False, self.paints[self.ind][0].color)
        self.place_text_surface_2 = my_font.render(place_name_2, False, self.paints[self.ind_1][0].color)
        self.place_x_1 = random.randint(30,width - 150)
        self.place_y_1 = random.randint(30,height - 30)
        self.place_x_2 = random.randint(30,width - 150)
        self.place_y_2 = random.randint(30,height - 30)
        
        self.places_surface.blit(self.place_text_surface_1, (self.place_x_1,self.place_y_1))
        if self.different_places:
            self.places_surface.blit(self.place_text_surface_2, (self.place_x_2,self.place_y_2))
    
    def print_place(self):
        self.surface.blit(self.places_surface, (0,0))
        
vernacular_sketchbook = Scrapbook(vernacular_objects, vernacular_names, 30, window)

time = 0

title = my_font_2.render("Sustainable in the Vernacular", False, [255,255,255])
title_2 = my_font_3.render("Cassie Halaszynski", False, [255,255,255])

def run_it():
    if time < 5:
        if rank == 0:
            window.blit(title, (175,200))
            window.blit(title_2, (1377,400))
        elif rank == 1:
            window.blit(title, (-1744.5,200))
            window.blit(title_2, (-543,400))
    
    comm.barrier()
    if rank == 0:
        vernacular_sketchbook.get_crafting()
    elif rank == 1:
        vernacular_sketchbook.get_crafting()
    elif rank == 2:
        vernacular_sketchbook.get_crafting()
    elif rank == 3:
        vernacular_sketchbook.get_crafting()
        
while True:
    run_it()
    time += 1
    
    pygame.display.update()
    clock.tick(240)
    
    if (pygame.time.get_ticks()/1000) > 1770:
        pygame.quit()