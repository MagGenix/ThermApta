
import matplotlib.pyplot as plt

class MeltProfile():
    
    # Constructor for a MeltProfile Object
    # Parameters:
    #     seq - primary sequence of the given melt curve
    #     data - data points of the melt curve (ex: [T, %binding])
    def __init__(self, seq, c = 'b.'):
        self.seq = seq
        self.curve_points = None # n x 2 array of data points
        self.score = None # Score of this melt curve
        
        # Possible Desciptors
        self.lower = None # Lower bound of the melt curve
        self.upper = None # Upper bound of the melt curve
        
    def NUPACK_melt(self):
        # TODO: Use NUPACK to calculate the melt profile
        pass
    
    def plot(self):
        # TODO: plot the data in curve_points
        if (self.curve_points is None):
            print("Warning: No Points to plot for this MeltProfile, returning.")
            return
        fig = plt.figure(figsize = (6, 6))
        ax = fig.subplots(1, 1)
        ax.plot(self.curve_points[0], self.curve_points[1], c)
        return
    # TODO: Algorithms to calculate curve
    