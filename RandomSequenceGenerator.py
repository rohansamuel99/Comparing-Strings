import random
import sys 

file = open("dna_string.txt", "a")

def RandomSequenceGenerator():
    dna_bases = "ACGT"
    for nucleotide in dna_bases:
        file.write("".join (random.choice(dna_bases) for i in range(random.randint(19, 41))))
    file.write("\n")

RandomSequenceGenerator()