import Aptamer, MeltProfile, Sequence 

def dna_to_rna(sequence=""):
    rna = sequence.upper()\
            .replace("A", "u")\
            .replace("C", "g")\
            .replace("G", "c")\
            .replace("T", "a")\
            .upper()
    return rna
    
def rna_to_seq(mrna=""):
    return Sequence(mrna)

def seq_to_aptamer(sequence=""):
    return Aptamer(sequence)
