"""CS 211 - Sabrina Zhang
Lab 5 - Matlibplot Animate sin and cos"""

import matplotlib.pyplot as plt
from numpy import pi, arange
from math import sin, cos
from random import random
import numpy as np
from matplotlib.animation import FuncAnimation

def animate_plot(t, v1, v2): 
    x = [] 
    y = [] 
    z = [] 

    # function that draws each frame of the animation 
    def animate(i): 
        x.append(t[i])
        y.append(v1[i])
        z.append(v2[i])
        ax.plot(x,y)
        ax.plot(x,z)
        plt.xlabel("time")
        plt.ylabel("sin and cos")
       
    # create the figure and axes objects 
    fig, ax = plt.subplots() 
    # run the animation 
    ani = FuncAnimation(fig, animate, frames=n, interval=30, repeat=False) 
    plt.show()
    
n = 100
x = [i for i in arange(0, 2 * pi, 2 * pi/100)]
y1 = [sin(i) for i in x]
y2 = [cos(i) for i in x]

animate_plot(x, y1, y2)