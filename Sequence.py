# Sequence Class
# Contains information on any given sequence of RNA
# Used within Aptamer and contains MeltProfile

## include some function that checks validity of the sequence 
# check for repeats (single bp and multiple bp repeats)
# check for rogue stop codons or rbs in the sequence
# check for shine delgarno seq?
# use numbers to encode bp

class Sequence():
    
    def __init__(self):
        self.sense = "ACGUACGUACGUGCAAUGCUUACGACAGUCAAGUCUAGCUAGUCCUGU"
        self.antisense = self.sense[::-1]
        self.conservation_factors = [];
        self.unfolding_temp = [];
        self.gc = 0.0
        self.au = 0.0
        self.length = [];
    
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
        
## -----------------
    
   ## def isBlacklisted():
        
    
   ## def addToBlacklist();
        