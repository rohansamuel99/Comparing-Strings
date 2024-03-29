# Date Created: 10-01-2022
# Date Modified: 1-04-2022
# Author: Rohan Hariharan
# File:  RandomSequenceGenerator.py
# Info: Contains a function RandomSequenceGenerator() that creates a random sequence of 2 DNA strings

import random
import sys 

# file = open("dna_string.txt", "a")

def RandomSequenceGenerator(string_length):
    dna_bases = "ACGT"
    # file.write("".join (random.choice(dna_bases) for i in range(random.randint(19, 41))))
    return ["".join(random.choice(dna_bases) for i in range(string_length))for pair in range(2)]
    # file.write("\n")