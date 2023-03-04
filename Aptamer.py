
class Aptamer():
    def __init__(self, assembled_seq = [], structure = [], melt_prof = []): 
        #Takes three variables, the sequence, the structure, the melting profiling 
        self.assembled_seq = assembled_seq
        self.structure = structure
        self.melt_prof = melt_profile 
        
    def graph_points(): 
        #plots the melt profile 
        #Calls Method in Meltprofile Class 
        return self.melt_prof.plot()
        
    def updateGC():
        #Manually read through assembled sequences to count G and C content
        #O(N) - reads every character of every sequence in assembled_seq
        #Saves information in fields G and C
        '''WILL LIKELY CHANGE TO UPDATE A, U, G, and C'''
        dna = self.assembeled_seq
        count_c = 0 
        count_g = 0
        total = []
        
        for sequence in dna:
            for position in range(len(sequence)):
                if sequence[position] == "C":
                    count_c += 1
                elif sequence[position] == "G":
                    count_g += 1
            count_dictionary = {"Number_of_C":count_c, "Number_of_G":count_g}
            total.append(count_dictionary)
        
        return total
    
    def getGC(sequence= ""):
        #Returns stored G/C values
        dna = self.assembled_seq
        ref = dna.index(sequence)
        total = self.updateGC() 
        '''Probably change into 4 getter functions for A, U, G, C'''
        return [total[ref].values()]
    
    
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