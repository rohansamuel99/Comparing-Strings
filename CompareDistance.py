# initial ideas
# take 2 strings and assign a number to k and split them in rolling k's or normal spilts. 
# take the k-mers from both the strings and compare them side by side, and then use the number of characters between 2 similar k-mers from the strings 
# to find the distance between the k-mers
# this can be done by assigning the strings to a list and then parsing through the list to find k-mers 

# the monstrosity
qgram_distance2 = lambda s, t, k: sum(abs({z:sum((1 if a==z else 0)for a in[s[i:i+k]for i in range(len(s)-k+1)])-sum((1 if b==z else 0)for b in[t[i:i+k] for i in range(len(t)-k+1)])for z in{q:0 for q in[s[i:i+k]for i in range(len(s)-k+1)]+[t[i:i+k]for i in range(len(t)-k+1)]}}[key])for key in{z:sum((1 if a==z else 0)for a in[s[i:i+k]for i in range(len(s)-k+1)])-sum((1 if b==z else 0)for b in[t[i:i+k]for i in range(len(t)-k+1)])for z in{q:0 for q in[s[i:i+k]for i in range(len(s)-k+1)]+[t[i:i+k]for i in range(len(t)-k+1)]}})
# s = string 1 from dna_string.txt
# t = string 2 from dna_string.txt
# k = length of k-mer wanted
# print (qgram_distance2("GCTAGCTAGCAT", "ACGATCGATCGA", 2))
# using a dictionary
 
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
print(kmer_distance("GCTAGCTAGCAT", "ACGATCGATCGA", 2))

########## Hamming Distance ##########
def hamming_distance(s, t):
    nucleotide = {"A": "0001", "T": "0010", "G": "0011", "C": "0100"}
    # iterate through string and then substitute each string with teh value.