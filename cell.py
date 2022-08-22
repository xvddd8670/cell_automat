import pygame
import random

class Cell:
    ##
    def __init__(self, position_x, position_y):
        self.type = 0
        self.rotate = 0
        self.energy = 0
        self.type_next = 0
        self.position_x = position_x
        self.position_y = position_y
        ##
        self.color_list = {'green' : (0, 255, 0),
                           'red' : (255, 0, 0),
                           'blue' : (0, 0, 255)}
        self.active_color = self.color_list['green']
    ##
    def check_cell(self, cells_list):
        self.rotate = random.randrange(0, 7)
        print(cells_list[3][6].position_x)
        print(cells_list[3][6].position_y)
    ##
    def render(self, screen):
        pygame.draw.rect(screen, self.active_color, pygame.Rect(self.position_x*6, self.position_y*6, 5, 5), 3)
