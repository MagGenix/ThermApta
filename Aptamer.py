import Sequence
import MeltProfile

class Aptamer():
    def __init__(self, assembled_seq = [], structure = [], melt_prof = []): 
        #Takes three variables, the sequence, the structure, the melting profiling 
        self.assembled_seq = assembled_seq
        self.structure = structure
        self.melt_prof = melt_profile 
        
    def graph_points(self): 
        #plots the melt profile 
        #Calls Method in Meltprofile Class 
        return self.melt_prof.plot()
        
    def update_bases(self):
        #Manually read through assembled sequences to count G and C content
        #O(N) - reads every character of every sequence in assembled_seq
        #Saves information in fields for all bases 
        
        dna = self.assembeled_seq
        total = []
        
        for sequence in dna:
            Sequence.updateBases(sequence)
            total.append([self.a, self.u, self.g, self.c])
            
        return total
    
    def get_bases(self, sequence= ""):
        #Returns stored G/C values
        dna = self.assembled_seq
        ref = dna.index(sequence)
        total = self.update_bases() 
        
        return [total[ref]]
    
    def length(self, sequence=""):
        bases = self.get_bases(sequence)
    
        return sum(bases)
        
    
    
    def isBlacklisted(self, blacklist_file=""):
    # checks for primary sequence in the blacklist file and returns True if present 
        reference = self.assembled_seq

        with open(self, blacklist_file) as f:
            sequences = f.readlines() # Assuming each sequence is on a newline 

            for i in reference:
                for j in sequences:
                    if i.strip() == j.strip():
                        return True
                    else:
                        pass # For now
                
    def addBlacklisted(self, blacklist_file=""):
    # checks for primary sequence in the blacklist file and adds sequence if not present 
        reference = self.assembled_seq

    if not self.isBlacklisted(blacklist_file):
        with open(blacklist_file, "a") as f:
            f.write("\n".join(reference) + "\n")