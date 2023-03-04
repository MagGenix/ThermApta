# Sequence Class
# Contains information on any given sequence of RNA
# Used within Aptamer and contains MeltProfile

## include some function that checks validity of the sequence 
# check for repeats (single bp and multiple bp repeats)
# check for rogue stop codons or rbs in the sequence
# check for shine delgarno seq?
# use numbers to encode bp

class Sequence():
    
    def __init__(self, seq_str):
        self.sense = seq_str
        self.antisense = self.sense[::-1]
        self.conservation_factors = [];
        self.unfolding_temp = [];
        self.updateBases()
        self.length = len(sense);
    
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
        
## -----------------
    
   ## def isBlacklisted():
        
    
   ## def addToBlacklist();
        