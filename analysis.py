import Aptamer, MeltProfile, Sequence 

def dna_to_rna(sequence=""):
    for bases in sequence:
        if bases == "A":
            bases.replace(bases, "U")
        elif bases == "C":
            bases.replace(bases, "G")
        elif bases == "G":
            bases.replace(bases, "C")
        else:
            bases.replace(bases, "A")
    return sequence 
    
def rna_to_seq(mrna=""):
    return Sequence(mrna)

def seq_to_aptamer(sequence=""):
    return Aptamer(sequence)
