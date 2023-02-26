# Sequence Class
# Contains information on any given sequence of RNA
# Used within Aptamer and contains MeltProfile

class Sequence():
    
    
    def __init__(self, test):
        self.primary_sequence = ["ACGUACGUACGUGCAAUGCUUACGACAGUCAAGUCUAGCUAGUCCUGU"]
        self.conservation_factors = [];
        self.unfolding_temp = [];
        self.gc = [];
        self.length = [];
        
    def test():
        print("MagGenix")
        
    
    def updateGC():
        
        gc_s = 0
        sequence_bps = self.primary_seq.list
        
        for bp in sequence_bps:
            if (bp == "C" or bp == "G"):
                gc_s++
        
        self.gc_content = gcs / len(sequence_bps)
        
        return
        
    
    def getGC():
        
        return (self.gc_content)
    
    def isBlacklisted():
        
    
    def addToBlacklist();
        