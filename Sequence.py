# Sequence Class
# Contains information on any given sequence of RNA
# Used within Aptamer and contains MeltProfile

## include some function that checks validity of the sequence 
# check for repeats (single bp and multiple bp repeats)
# check for rogue stop codons or rbs in the sequence
# check for shine delgarno seq?
# use numbers to encode bp

import random

class Sequence():
    
<<<<<<< HEAD
    def __init__(self, seq_str):
        self.sense = seq_str
        self.antisense = self.sense[::-1]
        self.conservation_factors = [];
        self.unfolding_temp = [];
        self.updateBases()
        self.length = len(sense);
=======
    
    def __init__(self, sense = "ACGUACGUACGUGCAAUGCUUACGACAGUCAAGUCUAGCUAGUCCUGU"):
        self.sense = sense #primary_sequence interpretation of strand
        self.antisense = self.sense[::-1] #antisense strand (reversed strand)
        self.conservation_factors = []; #probability vector, higher prob means more likely mutation for that bp
    
        self.gc = 0.0 #gc = (G + C) / (total)
        self.au = 0.0 
        self.length = len(self.sense);
    
    
    # generate random sequence of specified length (default: 100 bp)
    def randomSeq(self, length = 100): 
        
        bp = ["A", "U", "G", "C"]
        rand_seq = ""
        
        for i in range(0, length):
            rand_index = random.randint(0, 3)
            rand_seq += bp[rand_index]
        
        print(rand_seq)
    
>>>>>>> 954ee91fccb556f6b476cd45a44286fef03461ad
    
    def updateBases(self):
        self.g = 0
        self.c = 0
        self.a = 0
        self.u = 0
        for bp in sequence_bps:
            if (bp == "C"):
                self.c = self.c + 1
            if (bp == "G"):
                self.g = self.g + 1
            if (bp == "A"):
                self.a = self.a + 1
            if (bp == "U"):
                self.u = self.u + 1        
        return
    
    def get_C(self):
        return (self.c)
    
    def get_g(self):
        return (self.g)
    
    def get_a(self):
        return (self.a)
    
    def get_u(self):
        return (self.u)
    
    
    def test(self):
        print("MagGenix")
        print(self.sense)
        print(self.antisense)
        
        self.updateGC()
        print(self.getGC())
        
        self.updateAU()
        print(self.getAU())
        self.randomSeq(length = 100)
        
        
## -----------------
    
   ## def isBlacklisted():
        
    
   ## def addToBlacklist();
        