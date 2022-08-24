import pygame
import random

class Cell:
    ##
    def __init__(self, position_x, position_y):
        #####
        #DNA#
        #####
        #self.dna = {'food_type': 0,
                    #'priority_food/reproduction': 0,
                    #'energy_transfer_for_reproduction': 4,
                    #'energy_transfer': 0,
                    #'energy_intake': 0,
                    #'migration': 2,
                    #'cannibalism': 0 }
        self.dna = [0, #type food 
                    0, #priority food/reproduction/energy_transfer/energy_intake/migration
                    4, #count energy transfer for reproduction 
                    2, #migration chance
                    False, #cannibalism
                    False, #vampirism
                    0, #energy vampirism count
                    False, #energy transfer
                    0, #count energy transfer
                    1] #mutation chance
        #####
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
        cells_list[3][6].energy = 10
        print(cells_list[3][6].energy)
    ##
    def update(self, cells_list):
        if self.type == 0:
            i=0
        elif self.type == 1:
            i=0
        elif self.type == 2:
            i=0
    ##
    def render(self, screen):
        pygame.draw.rect(screen, self.active_color, pygame.Rect(self.position_x*6, self.position_y*6, 5, 5), 3)




















