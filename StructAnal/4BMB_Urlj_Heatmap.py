#!/usr/bin/python

__author__ = "Yekaterina Kovalyova"
__copyright__ = "Copyright 2017"
__credits__ = ["Yekaterina Kovalyova"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Yekaterina Kovalyova"
__email__ = "yekaterina.kovalyova@yale.edu"

### Usage:      python 4BMB_Urlj_Heatmap.py -u1 <U_RLJ 1> -u2 <U_RLJ 2> 
### Example:    python 4BMB_Urlj_Heatmap.py -u1 4BMB_F19.txt -u2 4BMB_F19Y.txt
### Note:       Structural comparison of protein to its mutant.

import argparse
import mpl_toolkits
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser(description='Protein Structure Analysis')
parser.add_argument('-u1', '--u1', help='U_RLJs of protein 1', required=True)
parser.add_argument('-u2', '--u2', help='U_RLJs of protein 2', required=True)
args = parser.parse_args()

# Plot repulsive Lennard Jones potential of residues as fxn of Chi_1 and Chi_2
# Hard-coded for the given files
def U_rlj(u1, u2):
    #Process the given files with chi1, chi2, and energies
    (wt_chi1, wt_chi2, wt_u) = processU(u1) #wildtype residue
    (mut_chi1, mut_chi2, mut_u) = processU(u2) #mutant residue

    #######################################################
    ###For heatmap plots, make 2D arrays of each value###
    #######################################################
    
    WT_chi1 = [] #2D array for WT chi1
    WT_chi2 = [] #2D array for WT chi2
    WT_u = [] #2D array for WT energy
    MUT_chi1 = [] #2D array for mutant chi1
    MUT_chi2 = [] #2D array for mutant chi2
    MUT_u = [] #2D array for mutant energy
    count = 0

    #Actually make the arrays 2D and populate
    #Hard-coded 72x72, for 72 chi1 angles x 72 chi2 angles
    for i in range(0, 72):
        WT_chi1.append([])
        WT_chi2.append([])
        WT_u.append([])
        
        MUT_chi1.append([])
        MUT_chi2.append([])
        MUT_u.append([])
        
        for j in range(0, 72):
            WT_chi1[i].append(wt_chi1[count])
            WT_chi2[i].append(wt_chi2[count])
            WT_u[i].append(wt_u[count])
             
            MUT_chi1[i].append(mut_chi1[count])
            MUT_chi2[i].append(mut_chi2[count])
            MUT_u[i].append(mut_u[count])

            count += 1
    
    ###############################################
    ###Plot the energies as fxn of chi1 and chi2###
    ###############################################
    
    plt.figure()
    plt.contourf(WT_chi1, WT_chi2, WT_u, cmap=plt.cm.hot,
                  vmax=3, vmin=0)
    plt.title('Repulsive Lennard Jones Energy of F19 in 4BMB')
    plt.xlabel('Chi_1')
    plt.ylabel('Chi_2')
    plt.colorbar()
    plt.show()

    plt.figure()
    plt.contourf(MUT_chi1, MUT_chi2, MUT_u, cmap=plt.cm.hot,
                  vmax=3, vmin=0)
    plt.title('Repulsive Lennard Jones Energy of F19Y in 4BME')
    plt.xlabel('Chi_1')
    plt.ylabel('Chi_2')
    plt.colorbar()
    plt.show()

# Get the chi1, chi2, and energies in separate arrays
def processU(Ufile):
    chi1 = []
    chi2 = []
    U = []
    f = open(Ufile, 'r')
    f.readline()    
    for line in f:
        tmp = line.split(" ")
        chi1.append(int(tmp[0]))
        chi2.append(int(tmp[1]))
        U.append(float(tmp[2]))
    f.close()
    return (chi1, chi2, U)  
           
# Run programs
U_rlj(args.u1, args.u2)