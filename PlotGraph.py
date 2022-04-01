from click import style
# Date Created: 1-04-2022
# Date Modified: 1-04-2022
# Author: Rohan Hariharan
# File:  PlotGraph.py
# Info: Contains a function plot_graph() that takes in the x and y values from a file and plots a graph with them.

from matplotlib import pyplot

def plot_graph(x, y):  
    
    style.use('ggplot')
    pyplot.plot(x,y)  

    pyplot.title("Comparison between K-mer Distance and Hamming Distance")    
    pyplot.ylabel('Hamming Distance')    
    pyplot.xlabel('K-mer Distance')    
    pyplot.show()    