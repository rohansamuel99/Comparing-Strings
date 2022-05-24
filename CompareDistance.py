# Date Created: 10-01-2022
# Date Modified: 1-04-2022
# Author: Rohan Hariharan
# File:  CompareDistance.py
# Info: Contains two functions; kmer_distance() which compares the knmer distance between two strings,
#       hamming_distance() which compares the hamming distance between two strings of equal length

import random
import sys
import matplotlib.pyplot as plt
import numpy as np


from RandomSequenceGenerator import RandomSequenceGenerator 

# initial ideas
# take 2 strings and assign a number to k and split them in rolling k's or normal spilts. 
# take the k-mers from both the strings and compare them side by side, and then use the number of characters between 2 similar k-mers from the strings 
# to find the distance between the k-mers
# this can be done by assigning the strings to a list and then parsing through the list to find k-mers 

# s = string 1
# t = string 2
# k = length of k-mer wanted
# print (qgram_distance2("GCTAGCTAGCAT", "ACGATCGATCGA", 2))
# using a dictionary
# s, t = RandomSequenceGenerator()
# print(s, t)
def kmer_distance(s, t, k):
    #empty dictionary
    d = {}

    for i in range(len(s) - k + 1):
        kmer = s[i:i + k]
        if kmer not in d:
            d[kmer] = 0
        d[kmer] += 1
    #     for z in range(0, k):
    #        if s[i : i + k - 1] == k:
    #            d += 1
    
    for j in range(len(t) - k + 1):
        kmer = t[j:j + k]
        if kmer not in d:
            d[kmer] = 0
        d[kmer] -= 1 
    #     for z in range(0, k):
    #         if s[i : i + k - 1] == k:
    #             d -= 1
    # return d
    # return abs(sum(d.values()))
    # return {key: abs(d[key]) for key in d}
    return sum(abs(d[key]) for key in d)
    

# print(kmer_distance("AGCT", "ACGT", 2))
# print(kmer_distance("GCTAGCTAGCAT", "ACGATCGATCGA", 3))
# print(kmer_distance(s, t, 2))


########## Hamming Distance ##########
# Can only be used to compare strings of the same length
def hamming_distance(s, t):
    difference = 0
    for i in range(len(s)): 
        if s[i] != t[i]:
            difference += 1
    return difference
    # return sum(1 for i in range(len(s)) if s[i] != t[i])
    # return sum(1 for a,b in zip(s,t) if a != b)

