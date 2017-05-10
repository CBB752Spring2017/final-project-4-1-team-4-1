CBB752Spring17 Final Project - 4.1
=====================

**Yekaterina Kovalyova, CBB 752**

Three programs compare WT and mutant structures of the 4BMB protein.

**Comparing two residues in terms of repulsive Lennard Jones energies as a function of residue Chi_1 and Chi_2 angles.**

 *A. For 3D plot of energy as a function of the dihedral angles, to run program:*

	python 4BMB_Urlj.py -u1 4BMB_F19.txt -u2 4BMB_F19Y.txt

 *B. For heatmap of energy as a function of the dihedral angles, to run program:*

	python 4BMB_Urlj_Heatmap.py -u1 4BMB_F19.txt -u2 4BMB_F19Y.txt


Both programs behave identically; the only difference the is plot(s) they spit out. Programs read in chi_1, chi_2, and energy values, converts them into 2D arrays (process uses hardcoded dimensions for arrays, not friendly for chi rotations of different values, but easily changeable) appropriate for plotting in 3D, and plots these arrays. While the 3D wiregrid plot may not be ideal representation, both proteins can be plotted simultaneously for easy qualitative comparison. All images pertaining to these data are called 4BMB_Urlj*. 
	

**Comparing two proteins in terms of root-mean-square deviations of backbone heavy atoms.**

*To run program:* 

    python 4BMB_RMSD.py -p1 4bmb_aligned.pdb -p2 4bme_aligned.pdb


Program processes PBD files to extract relevant info (residue #, atom name, coordinates), iterates through each residue, gets coordinates of each heavy backbone atom (C, N, O, Calpha, hardcoded and not friendly for changing which atoms to consider), and calculates the root-mean-square deviation for these four atoms between the WT and mutant proteins. Note, it does not make sense to use side-chain atoms since if multiple residues are different, there would be no corresponding atoms to calculate RMSD. Program plots RMSD for each residue. Program spits out RMSD for the entire protein.
