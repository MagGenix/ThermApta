import Sequence

class MeltProfile():
    
    # Constructor for a MeltProfile Object
    # Parameters:
    #     Sequence - Sequence for the given curve
    #     data - data points of the melt curve (ex: [T, %binding])
    def __init__(self, seq, data):
        self.seq = seq
        self.data = data