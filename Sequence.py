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
    
    
    def updateGC(self):
        
        gc_s = 0
        sequence_bps = list(self.sense)
        
        for bp in sequence_bps:
            if (bp == "C" or bp == "G"):
                gc_s += 1
    
        self.gc = gc_s / len(sequence_bps)
        
        return
    
    def updateAU(self):
        
        au_s = 0
        sequence_bps = list(self.sense)
        
        for bp in sequence_bps:
            if (bp == "A" or bp == "U"):
                au_s += 1
            
        self.au = au_s / len(sequence_bps)
        
        return
    
    def getGC(self):
        return (self.gc)
    
    def getAU(self):
        return (self.au)
    
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
        