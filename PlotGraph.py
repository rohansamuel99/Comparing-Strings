# Date Created: 1-04-2022
# Date Modified: 1-04-2022
# Author: Rohan Hariharan
# File:  PlotGraph.py
# Info: Contains a function plot_graph() that takes in the x and y values from a file and plots a graph with them.

from click import style
import matplotlib.pyplot as plt
import numpy as np
from CompareDistance import *
from RandomSequenceGenerator import RandomSequenceGenerator 

def plot_graph():  
    
    kmer_points = []
    hamming_points = []

    for i in range (100):
        s, t = RandomSequenceGenerator(100)

        print(s, t)
        print(kmer_distance(s, t, 2))
        print(hamming_distance(s, t))

        kmer_points.append(kmer_distance(s, t, 2))
        hamming_points.append(hamming_distance(s, t))

        np.array([kmer_points])
        np.array([hamming_points])

    plt.title("Comparison between K-mer Distance and Hamming Distance")    
    plt.ylabel('Hamming Distance')    
    plt.xlabel('K-mer Distance')   
    ax = plt.gca()
    ax.set_xlim([0, 90])
    ax.set_ylim([0, 100])
    plt.scatter(kmer_points, hamming_points)
    plt.show()
    
    

plot_graph()