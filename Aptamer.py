from Sequence import Sequence
from MeltProfile import MeltProfile

class Aptamer():
    def __init__(self, seq_list = [], structure = []): 
        #Takes three variables, the list of Sequences, the structure, the melting profiling 
        self.seq_list = seq_list #list of Sequence objs
        self.assembled_seq = concat_seq(seq_list)
        self.structure = structure
        self.melt_profile = MeltProfile()
        
    def graph_points(self): 
        #plots the melt profile 
        #Calls Method in Meltprofile Class 
        return self.melt_prof.plot()
    
    def concat_seq(seq_list): #returns full sequence of Aptamer, from obj representation 
        total_seq = ""
        for seq in seq_list:
            total_seq += seq.getSense()
            
        return (total_seq) 
    
    def countBases(self):
        #count numbers of each bp type by adding counts from each seq in list
        
        self.g = 0
        self.a = 0
        self.u = 0
        self.c = 0
        
        for seq in self.seq_list:
            
            self.g += seq.get_g
            self.c += seq.get_u
            self.a += seq.get_a
            self.c += seq.get_c
    
    def isBlacklisted(self, blacklist_file=""):
    # checks for primary sequence in the blacklist file and returns True if present 
        reference = self.seq_list

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
        reference = self.seq_list

        if not self.isBlacklisted(self, blacklist_file):
            with open(blacklist_file, "a") as f:
                f.write("\n".join(reference) + "\n")