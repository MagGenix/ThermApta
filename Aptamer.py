import Sequence
import MeltProfile

class Aptamer():
    def __init__(self, assembled_seq = [], structure = []): 
        #Takes three variables, the sequence, the structure, the melting profiling 
        self.assembled_seq = assembled_seq #list of Sequence objs
        self.structure = structure
        self.melt_profile = MeltProfile(concat_seq(self.assembled_seq))
        
    def graph_points(self): 
        #plots the melt profile 
        #Calls Method in Meltprofile Class 
        return self.melt_prof.plot()
    
    def concat_seq(assembled_seq): #returns full sequence of Aptamer, from obj representation 
        total_seq = "
        for seq in assembled_seq:
            total_seq += seq.getSense()
            
        return (total_seq) 
    
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

        if not self.isBlacklisted(self, blacklist_file):
            with open(blacklist_file, "a") as f:
                f.write("\n".join(reference) + "\n")