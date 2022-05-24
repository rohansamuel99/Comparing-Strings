# Date Created: 1-04-2022
# Date Modified: 1-04-2022
# Author: Rohan Hariharan
# File:  PlotGraph.py
# Info: Contains a function plot_graph() that takes in the x and y values  and plots a graph with them.

from click import style
import matplotlib.pyplot as plt
import numpy as np
from CompareDistance import *
from RandomSequenceGenerator import RandomSequenceGenerator 

def plot_graph():  
    
    kmer_points = []
    kmer_points2 = []
    hamming_points = []

    for i in range (100):
        s, t = RandomSequenceGenerator(100)

        print("String s: " + s + '\n',"String t: " + t)
        print("10-mer Distance is: " + str(kmer_distance(s, t, 37)))
        # print("5-mer Distance is: " + str(kmer_distance(s, t, 5)) + '\n')
        print("Hamming Distance is: " + str(hamming_distance(s, t)) + '\n')

        kmer_points.append(kmer_distance(s, t, 37)) # x-axis
        # kmer_points2.append(kmer_distance(s, t, 5)) # y-axis
        hamming_points.append(hamming_distance(s, t)) # y-axis

        np.array([kmer_points])
        # np.array([kmer_points2])
        np.array([hamming_points])

    plt.title("Comparison between 10-mer Distance and Hamming Distance")   
    plt.xlabel('10-mer Distance') 
    # plt.ylabel('5-mer Distance')  
    plt.ylabel('Hamming Distance')      
    ax = plt.gca()
    ax.set_xlim([0, 200])
    ax.set_ylim([0, 100])
    # ax.set_xlim([0, 50])
    # ax.set_ylim([0, 50])
    plt.scatter(kmer_points, hamming_points) # x-axis, y-axis
    # plt.scatter(kmer_points, kmer_points2) # x-axis, y-axis
    plt.show()
    

plot_graph()