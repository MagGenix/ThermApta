# Sequence Class
# Contains information on any given sequence of RNA
# Used within Aptamer and contains MeltProfile

## include some function that checks validity of the sequence 
# check for repeats (single bp and multiple bp repeats)
# check for rogue stop codons or rbs in the sequence
# check for shine delgarno seq?
# use numbers to encode bp

import random
from MeltProfile import MeltProfile
from nupack import Model, mfe, pairs

class Sequence():
    
    def __init__(self, sense):
        self.sense = sense #primary_sequence interpretation of strand
        self.antisense = self.sense[::-1] #antisense strand (reversed strand)
        self.conservation_factors = [] #probability vector, higher prob means more likely mutation for that bp
        self.countBases()
        self.length = len(self.sense)
        self.melt_profile = MeltProfile(self.sense)
        
    def countBases(self):
        #count numbers of each bp type 
        self.g = 0
        self.c = 0
        self.a = 0
        self.u = 0
        for bp in list(self.sense):
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
        return self.melt_profile.curve_points
    
    def plot_melt_profile(self, fig=None, ax=None, title=""):
        self.melt_profile.plot(fig, ax, title)
        return
    
    def get_energy(self, temp):
        structure = mfe(
            strands=[self.sense],
            model=Model(
                material='rna',
                ensemble='stacking',
                celsius=temp,
                sodium=1.0,
                magnesium=0.0))
        return structure[0].energy
            
    def get_pair_prob(self, temp):
        pair_prob = pairs(
            strands=[self.sense], 
            model=Model(
                material='rna', 
                ensemble='stacking', 
                celsius=temp,
                sodium=1.0,
                magnesium=0.0))
        return pair_prob.to_array()
    #getters---------------------------------
    
    def get_c(self):
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
    
    def toString(self):
        print("Sequence: ", self.sense)
        print("Antisense: ", self.antisense)
        print("A: \t", self.a)
        print("U: \t", self.u)
        print("C: \t", self.c)
        print("G: \t", self.g)
    
        
        
## -----------------
    
   ## def isBlacklisted():
        
    
   ## def addToBlacklist();
        