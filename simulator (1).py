import random
import math
from matplotlib import pyplot as plt
import numpy as np

def normpdf(x, mean, sd):
    """
    Return the value of the normal distribution 
    with the specified mean and standard deviation (sd) at
    position x.
    You do not have to understand how this function works exactly. 
    """
    var = float(sd)**2
    denom = (2*math.pi*var)**.5
    num = math.exp(-(float(x)-float(mean))**2/(2*var))
    return num/denom

def pdeath(x, mean, sd):
    start = x-0.5
    end = x+0.5
    step =0.01    
    integral = 0.0
    while start<=end:
        integral += step * (normpdf(start,mean,sd) + normpdf(start+step,mean,sd)) / 2
        start += step            
    return integral    
    
recovery_time = 4 # recovery time in time-steps
virality = 0.2    # probability that a neighbor cell is infected in 
                  # each time step                                                  

class Cell(object):

    def __init__(self,x, y):
        self.x = x
        self.y = y 
        self.state = "S" # can be "S" (susceptible), "R" (resistant = dead), or 
                         # "I" (infected)
        self.time = 0
    
    def __str__(self):
        return str(self.x) + ', ' + str(self.y)
    
    def infect(self): #how to increment without resetting to 0
        self.time = 0
        self.state = "I" 
        pass
    
    def process(self, adjacent_cells):
        if (self.state == "I") and (self.time >= 1):
            for i in adjacent_cells:
                if (i.state  == "S"):
                    print("possibly infected")
                    infect_probability = random.random()
                    if infect_probability <= virality:
                        i.infect()
        else:
            self.time += 1
        pass
        
        
        
class Map(object):
    
    cells = dict()
    
    def __init__(self):
        self.height = 150
        self.width = 150           
        self.cells = {}

    def add_cell(self, cell):
        self.cell = cell
        key = (cell.x, cell.y)
        self.cells[key] = self.cell
        
    def display(self):
        #print(self.cells)
        img = np.zeros((150,150,3))
        for y in range(150):
            for x in range(150):
                if (x,y) in self.cells:
                    if Cell(x,y).state == "S": #check if its in the dictionary first
                        img[x,y]= (0.0,1.0,0.0)
                    if Cell(x,y).state == "I":
                        img[x,y] = (1.0,0.0,0.0)
                    if Cell(x,y).state == "R":
                        img[x,y] = (0.5,0.5,0.5)
                 
        plt.imshow(img)
        pass 
    

    def adjacent_cells(self, x,y): #
        self.x = x
        self.y = y
        adjacent_cells_list = []
        if (x + 1,y) in self.cells: 
            adjacent_cells_list.append(self.cells[(x + 1,y)])
        if (x,y + 1) in self.cells:
            adjacent_cells_list.append(self.cells[(x,y + 1)])
        if (x - 1,y) in self.cells:
            adjacent_cells_list.append(self.cells[(x - 1,y)])
        if (x,y - 1) in self.cells:
            adjacent_cells_list.append(self.cells[(x,y - 1)])
        return adjacent_cells_list
        pass
    
    def time_step(self):
        for key in self.cells:   
            Cell.process(self.cells[key],self.adjacent_cells(key[0],key[1]))
        self.display()
        # Update each cell on the map 
        # display the map.
        
        # ... cell.process(adjacent_cells... )
        pass

            
def read_map(filename):
    
    m = Map()
    
    f = open(filename,'r')
    
    for line in f:
        coordinates = line.strip().split(',')
        c = Cell(int(coordinates[0]),int(coordinates[1]))
        Map.add_cell(m, c)

    return m
new_map = read_map('nyc_map.csv')