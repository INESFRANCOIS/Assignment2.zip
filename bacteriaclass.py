# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 18:07:45 2020
Agent class 
@author: Inès
@version : 1.2.3
license: GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007

"""

# Importation of the random module
import random 
# Importation of module testmod in the librairie doctest 
from doctest import testmod

random.seed

class Agent :

"""
This class simulates movements of bacteria according the current wind and turbulances.

The constructors has two arguments: 
environment (a list of list representing the city in which agents are located) 
bacteria (a list of bacteria in the environment) 

Bacteria have four characteristics : name, x-coordinate, y-coordinate and z-coordinate.

There are two functions to simulate movements of bacteria: move and turbulance. 

"""
    
    # Constructor 

    def __init__(self, name, environment, bacteria, y, x, z):
        
        """
        Function to initialize the attributes of the Bacteria class.

        Parameters
        ----------
        name : Number
             Label for the different variables   
        environment : a list of lists
            the environment in which the bacteria are located.
        bacteria : list
            Initial position of the bacteria
        y : Number
            y-cordinate of the bacteria 
        x : Number
            x_coordinate of the bacteria
        z : Number
            z_coordinate of the bacteria
                     
        Returns
        -------
        None
        
        """
        self.name = name
        self. environment = environment
        self.bacteria = bacteria
        self.y = y
        self.x = x
        self.z = z
        
    # Method to simulate the movement of bacteria according the current wind 
    def move(self, d):
        
        """
        Function to simulate the movement of bacteria.

        Parameters
        ----------
        d : Number
            Value to be added or substracted
        
        Returns
        -------
        None
        
        Testing code
        >>> random.seed(0)
        >>> bacteria = []
        >>> environment = []
        >>> row = []
        >>> row.append(7)
        >>> environment.append(row)
        >>> y = 151
        >>> x = 51
        >>> a = Agent (0,environment,bacteria,y,x,0)
        >>> a.move(1)
        >>> a.x
        51
        >>> a.move(1)
        >>> a.y
        0
        
        """    
        
        environment_width = len(self.environment[0])
        environment_height = len(self.environment)
        r= random.random()
        # print ("r", r)
        if r <= 0.05:
            self.x = (self.x - d) % environment_width # west 
        elif 0.05 < r <= 0.8:
            self.x = (self.x + d) % environment_width # east 
        elif 0.8 < r <= 0.9:
            self.y = (self.y + d) % environment_height # north 
        else: # r > 0.9
            self.y = (self.y - d) % environment_height # south
        
    # Method to simulate the movement of bacteria in presence or absence of turbulance 
    def turbulance(self, z):
        
        """
        Function to simulate the turbulance.

        Parameters
        ----------
        z : Number
            Value to be added or substracted 
        
        Returns
        -------
        None
        
        Testing code
        >>> random.seed(0)
        >>> bacteria = []
        >>> environment = []
        >>> row = []
        >>> row.append(7)
        >>> environment.append(row)
        >>> z = 75
        >>> a = Agent (0,environment,bacteria,0,0,z)
        >>> a.turbulance(1)
        >>> a.z
        74
        >>> a.turbulance(1)
        >>> a.z
        73
        >>> a.turbulance(1)
        >>> a.z
        72
       
        
        """  
        if self.z > 0: # Ensure that when the bacteria are on the ground, they won't be blown by the wind   
            if self.z >= 75: # Turbulance
                r= random.random()
                if r <= 0.2:
                    self.z = self.z + z
                elif 0.2 < r < 0.3:
                    self.z = self.z
                else: 
                   self.z = self.z - z
            else: # No turbulance (z<75)
                self.z = self.z - z
        else: # z <= 0
            self.x = self.x
            self.y = self.y
            self.z = self.z     
                

    def __str__(self): 
        return f'{self.name},{self.x}, {self.y}, {self.z}'
    
    if __name__ =='__main__':
        import doctest
        doctest.testmod ()
        		
