# take 2 strings and assign a number to k and split them in rolling k's or normal spilts. 
# take the k-mers from both the strings and compare them side by side, and then use the number of characters between 2 similar k-mers from the strings 
# to find the distance between the k-mers
# this can be done by assigning the strings to a list and then parsing through the list to find k-mers 

def get_q_gram_distance(s, t, kmers, k):
    #strings s, t of length n and m respectively
    n=len(s)
    m=len(t)
    #an empty array 
    d=[]
    for i in range(len(kmers)):
        d.append(0)#init vector, O(q)
        
    for i in range(1, n - k + 1):#slide window, O(n)
        for r in range(0, len(mers)):#get count, O(q)
            if s[i:i + k - 1] == kmers[r]:
                d[r]+=1#first vector sends postive effect
        
                    
    for i in range(1, m - k + 1):#slide window, O(m)
        for r in range(0,len(mers)):#get count, O(q)
            if s[i:i + k - 1] == kmers[r]:
                d[r] -= 1#second vector sends negtive effect
    res = 0
    for i in vector:
        res += abs(i)
        
    return res

#Dan Gee
qgram_distance2 = lambda s, t, k: sum(abs({z:sum((1 if a==z else 0)for a in[s[i:i+k]for i in range(len(s)-k+1)])-sum((1 if b==z else 0)for b in[t[i:i+k]for i in range(len(t)-k+1)])for z in{q:0 for q in[s[i:i+k]for i in range(len(s)-k+1)]+[t[i:i+k]for i in range(len(t)-k+1)]}}[key])for key in{z:sum((1 if a==z else 0)for a in[s[i:i+k]for i in range(len(s)-k+1)])-sum((1 if b==z else 0)for b in[t[i:i+k]for i in range(len(t)-k+1)])for z in{q:0 for q in[s[i:i+k]for i in range(len(s)-k+1)]+[t[i:i+k]for i in range(len(t)-k+1)]}})
# s = string 1 from dna_string.txt
# t = string 2 from dna_string.txt
# k = length of k-mer wanted

def kmer_distance(s, t, k):
    
    d = {}

