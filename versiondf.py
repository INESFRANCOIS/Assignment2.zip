# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 20:05:02 2020
Script to run the program
@author: Inès
@version : 1.4.2
license: GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007

"""

# Importation of librairies and modules
import csv
import bacteriaclass
import matplotlib
import matplotlib.pyplot 
import pandas as pd

# Find the bombing point 
with open('windraster.csv', newline='') as f:
    reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
    r = 0
    for row in reader:
        r = r + 1 
        col = 0
        for value in row:
            col = col + 1
            if (value == 255): # the value 255 representing the bombing point
                y = r
                x = col
                print ("y =", r, "x = ", col, "value =", value)
f. close()

# Initialize the environment
environment = []
with open('windraster.csv', newline='') as f:
    reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
    for row in reader:
        rowlist = []
        for value in row:
            rowlist.append(value)
        environment.append(rowlist)
f. close()

#  Initialize the 2D lists zero and density 
rows = len(environment)
cols = len(environment[0])
density = []
zero = []
for r in range(0, rows):
    row = []
    for c in range (0, cols):
        row.append(0)
    density.append(row)
    zero.append(row)
       
# Initialize the number of bacteria and the number of iterations 
num_of_bacteria = 5 
num_of_iterations = 85 

# Create a figure
fig = matplotlib.pyplot.figure()
# Give a title for the figure 
fig.suptitle('Tracking biological weapon fallout')

# Create 5000 bacteria in bombing point
bacteria =[]
for i in range(num_of_bacteria):
   y = y  # y-coordinate of all bacteria in bombing point: 151
   x = x  # x-coordinate of all bacteria in bombing point: 51
   z = 75 # z-coordinate of all bacteria in bombing point: 75 (height of the building)
   bacteria.append(bacteriaclass.Agent(i, environment, bacteria, y, x, z))
x_coordinate = []
y_coordinate = []
z_coordinate = []
for i in range(len(bacteria)):
    x_coordinate.append(bacteria[i].x)
    y_coordinate.append(bacteria[i].y)
    z_coordinate.append(bacteria[i].z)
    
    
df_initial = pd.DataFrame({'x': x_coordinate, 'y': y_coordinate, 'z': z_coordinate})
   
# Simulation of movements of bacteria according current wind and turbulance
for j in range(num_of_iterations):
    for i in range(num_of_bacteria):
        bacteria[i].move(1)
        bacteria[i].turbulance(1)        
        
        
x_coordinate = []
y_coordinate = []
z_coordinate = []
for i in range(len(bacteria)):
    x_coordinate.append(bacteria[i].x)
    y_coordinate.append(bacteria[i].y)
    z_coordinate.append(bacteria[i].z)
df_final = pd.DataFrame({'x': x_coordinate, 'y': y_coordinate, 'z': z_coordinate})

                  
# Plot the density map
density = zero
for i in range(num_of_bacteria):
    density[bacteria[i].y][bacteria[i].x] = density[bacteria[i].y][bacteria[i].x] + 1
matplotlib.pyplot.imshow(density) 
fig.savefig('D:\Bacterie\Bacteria.png')    

       