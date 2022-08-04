import random

class Cell:
    def __init__(self):
        self.type = 0
        self.rotate = 0
        self.energy = 0
        self.type_next = 0
    def check_cell(self):
        self.rotate = random.randrange(0, 7)
