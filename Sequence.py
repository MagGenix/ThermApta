# Sequence Class
# Contains information on any given sequence of RNA
# Used within Aptamer and contains MeltProfile

## include some function that checks validity of the sequence 
# check for repeats (single bp and multiple bp repeats)
# check for rogue stop codons or rbs in the sequence
# check for shine delgarno seq?
# use numbers to encode bp

import random
import MeltProfile

class Sequence():
    
    def __init__(self, sense = None):
        self.sense = sense #primary_sequence interpretation of strand
        self.antisense = self.sense[::-1] #antisense strand (reversed strand)
        self.conservation_factors = [] #probability vector, higher prob means more likely mutation for that bp
        self.updateBases()
        self.length = len(self.sense)
        self.melt_profile = MeltProfile(self.sense)
    
    
    # generate random sequence of specified length (default: 100 bp)
    def randomSeq(self, length = 100): 
        
        bp = ["A", "U", "G", "C"]
        rand_seq = ""
        
        for i in range(0, length):
            rand_index = random.randint(0, 3)
            rand_seq += bp[rand_index]
        
        if (self.sense not None):
            print("Warning: Overwriting a sequence with a random sequence")
        
        self.sense = rand_seq
        
    def updateBases(self):
        self.g = 0
        self.c = 0
        self.a = 0
        self.u = 0
        for bp in sequenace_bps:
            if (bp == "C"):
                self.c = self.c + 1
            if (bp == "G"):
                self.g = self.g + 1
            if (bp == "A"):
                self.a = self.a + 1
            if (bp == "U"):
                self.u = self.u + 1        
        return
    
    def generate_melt_profile(self):
        
        self.melt_profile.NUPACK_melt()

        return
    
    #getters---------------------------------
    
    def get_C(self):
        return (self.c)
    
    def get_g(self):
        return (self.g)
    
    def get_a(self):
        return (self.a)
    
    def get_u(self):
        return (self.u)
    
    def getSense(self):
        return (self.sense) 
    
    def test(self):
        pass
    
    
        
        
## -----------------
    
   ## def isBlacklisted():
        
    
   ## def addToBlacklist();
        