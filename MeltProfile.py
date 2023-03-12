from nupack import Model, mfe, pairs
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
import numpy as np
import math

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
        t_low = 25
        t_high = 100
        temps = np.linspace(t_low, t_high, 100)
        curve_points = np.empty((100, 2))
        for temp, idx in zip(temps, range(len(temps))):
            pair_prob = pairs(
                strands=[self.seq], 
                model=Model(
                    material='rna', 
                    ensemble='stacking', 
                    celsius=temp,
                    sodium=1.0,
                    magnesium=0.0))
            bound = np.argmax(pair_prob.to_array(), axis=1)
            curve_points[idx][0] = temp
            # if pair_prob shows most likely "bound" to itself, it is unbound
            curve_points[idx][1] = sum([bound[i] != i for i in range(len(bound))]) / len(bound)
        self.curve_points = curve_points
        self.lower = min(curve_points[:, 1])
        self.upper = max(curve_points[:, 1])
    
    def plot(self, fig=None, ax=None, title=""):
        # TODO: plot the data in curve_points
        if (self.curve_points is None):
            print("Warning: No Points to plot for this MeltProfile, returning.")
            return
        
        if (fig == None):
            fig = plt.figure(figsize = (12, 6))
        if (ax == None):
            ax = fig.subplots(1, 1)
        ax.plot(self.curve_points[:, 0], self.curve_points[:, 1])
        ax.set_title(title)
        ax.set_xlabel("Temperature (C)")
        ax.set_ylabel("% Nucleotides Bound")
        ax.set_ylim([0, 1])
        ax.set_xlim([25, 105])
    # TODO: Algorithms to calculate curve
    
    def score_against_goal(self):
        goal = lambda x: 0.9 - 0.8 / (1 + math.exp(x**(-10*x + 400)))
        diffs = np.array([percent_unbound - goal(percent_unbound) for percent_unbound in self.curve_points[:, 1]])
        rmsd = np.sqrt((diffs * diffs).mean())
        return rmsd
