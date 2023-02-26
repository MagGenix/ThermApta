
class Aptamer():
    def __init__(self, assembled_seq = [], structure = [], melt_prof = []): 
        #Takes three variables, the sequence, the structure, the melting profiling 
        self.assembled_seq = assembled_seq
        self.structure = structure
        self.melt_prof = melt_profile 
        
    def graph_points(): 
        #plots the melt profile 
        #Calls Method in Meltprofile Class 
        return self.melt_prof.plot
        
    def updateGC():
        pass 
    
    def getGC():
        pass
    '''
    def isBlaclisted(backlist_file = ""): 
        # checks for primary sequence in the backlist file and returns true if present 
        reference = self.assembled_seq
        
        with open(backlist_file) as f:
            sequences = f.readlines() #Assuming each sequence is on a newline 
            
            for i in reference:
                for j in sequences:
                    if i == j:
                        return True
                    else:
                        pass #For Now 
    
    def addBlackisted(backlist_file = ""):
        # checks for primary sequence in the backlist file and adds sequence if not present 
        reference = self.assembled_seq
        
        if self.isBlaclisted(backlist_file = "") != True:
            with open(backlist_file,"a") as f:
                f.write(ref for ref in referemces)
    
    '''
    def isBlacklisted(blacklist_file=""):
    # checks for primary sequence in the blacklist file and returns True if present 
    reference = self.assembled_seq

    with open(blacklist_file) as f:
        sequences = f.readlines() # Assuming each sequence is on a newline 

        for i in reference:
            for j in sequences:
                if i.strip() == j.strip():
                    return True
                else:
                    pass # For now
                
    def addBlacklisted(blacklist_file=""):
    # checks for primary sequence in the blacklist file and adds sequence if not present 
    reference = self.assembled_seq

    if not self.isBlacklisted(blacklist_file):
        with open(blacklist_file, "a") as f:
            f.write("\n".join(reference) + "\n")