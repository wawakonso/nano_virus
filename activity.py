from models import Cell, Virus
import numpy
from math import sqrt


type_list = ['Tumorous','Red','White']
nano_virus = Virus()

cell_objects = {}
distance_cells = []

tumorous_cells = []
red_cells = []
white_cells = []

count_1 = count_2 = count_3 = 0
i = 100

while i > 0:
    cell_objects[i]= Cell()
    rand_prop = numpy.random.choice(numpy.arange(1, 4), p=[0.05, 0.25, 0.70])
    cell_objects[i].set_type(type_list[rand_prop-1])
    i=i-1

def calculate_distance(cell1,cell2):
    distance = sqrt((cell1.get_x() - cell2.get_x())**2 +
                    (cell1.get_y() - cell2.get_y())**2 +
                    (cell1.get_z() - cell2.get_z())**2 )
    return distance

def locate_cell_by_type(cell_objects):
    c = len(cell_objects)
    for cels in range(1,101):
        if cell_objects[cels].get_type() == "Tumorous":
            tumorous_cells.append(cels)
        elif cell_objects[cels].get_type() == "Red":
            red_cells.append(cels)
        else:
            white_cells.append(cels)
    

#def tumorous_infection():

j = 1
while j <= 100:
    distance_cells.append(calculate_distance(nano_virus, cell_objects[j]))
    j=j+1



locate_cell_by_type(cell_objects)
print tumorous_cells
print red_cells
print white_cells
