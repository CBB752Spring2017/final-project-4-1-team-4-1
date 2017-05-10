CBB752Spring17 Final Project - 4.1
=====================

**Yekaterina Kovalyova, CBB 752**

Program analyzes WT and mutant proteins in terms of root-mean-square deviations of backbone heavy atoms, and repulsive Lennard Jones energies as a function of residue Chi_1 and Chi_2 angles. 

*To run program:* 

    python 4BMB.py -p1 4bmb_aligned.pdb -p2 4bme_aligned.pdb -u1 4BMB_F19.txt -u2 4BMB_F19Y.txt


Program has two main functions



Program reads in DNA sequence (processed in a simple text file) and text file containing at least one guide RNA sequence (excluding the PAM sequence). It searches DNA sequence for a designated PAM sequence (default 'NGG'), uses Smith-Waterman alignment algorithm to align the DNA's 20 nucleotides before PAM sequence with the gRNA (note if gRNA originally had uracils, they are changed to thymines for comparison to DNA), and writes full DNA with aligned gRNA to gRNAtargets.txt. Program also checks to see any off-target effects on reverse complement of given DNA.

User can dictate maximum number of mismatches before gRNA is considered valid (default 5), and alignment parameters. Note, no scoring matrix used here; match score is the same for all four nucleotides, and dictated by user (default 1).

Since no clear "target" is provided, perfect alignment score is considered "on-target". Only places where gRNA aligns with at most max number of mismatches are written to output. For each such place, output shows the gRNA sequence, the full DNA sequence, and the aligned gRNA; further, output tells if this is "target" or "off-target" based on alignment score, and whether we are looking at the forward DNA strand or reverse complement DNA strand.

Sample DNA sequence, gRNA sequences, and resulting output are provided.