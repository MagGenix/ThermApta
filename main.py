from MeltProfile import MeltProfile
from Aptamer import Aptamer
from Sequence import Sequence
    
import random
def randomSeq(length = 100): 
        # Could add variable probability instead of uniform prob
        bp = ["A", "U", "G", "C"]
        rand_seq = ""
        
        for i in range(0, length):
            rand_index = random.randint(0, 3)
            rand_seq += bp[rand_index]
        
        return rand_seq
        
def test():
    seq1 = Sequence("AUGCAUCGAUUACAUACGAUUCGAUCGAUGC")
    seq1.toString()
    print("\n\n\n\n\n")
    seq2 = Sequence(randomSeq(10000))
    seq2.toString()
        
    
test()