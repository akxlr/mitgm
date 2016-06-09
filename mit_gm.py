"""
Print a factor graph in .fg format for libDAI inference engine
usage: python mit_gm.py n_obj n_loc
For description of .fg file format, see https://staff.fnwi.uva.nl/j.m.mooij/libDAI/doc/fileformats.html
"""

import sys
import numpy as np

def add_unique_factor(s, v1, v2, n_loc):
    """ Factor to enforce two objects are not in the same location. """

    # 2
    # v1 v2
    # n_loc n_loc
    # n_loc * (n_loc - 1)
    # <nonzero table values>

    s += "2\n"                          # Number of variables in factor
    s += "%s %s\n" % (v1, v2)           # Variables in factor
    s += "%s %s\n" % (n_loc, n_loc)     # Number of values each variable can take
    s += "%s\n" % (n_loc * (n_loc - 1)) # Number of nonzero entries in factor table

    cpt = 1.0 - np.eye(n_loc)
    cpt_flat = cpt.T.flatten()
    for i in range(len(cpt_flat)):
        if cpt_flat[i] != 0:
            s += "%s %s\n" % (i, cpt_flat[i])

    s += "\n"
    return s, 1

def add_emission_factors(s, v, ys, n_loc, epsilon):
    """ Pairwise factors between v and each of the ys, describing emission probabilities. """

    assert len(ys) == n_loc

    for j in range(n_loc):
        # A single pairwise factor looks like
        # 2
        # v yj
        # n_loc 2
        # n_loc*2
        # <table>

        s += "2\n"                    # Number of variables in factor
        s += "%s %s\n" % (v, ys[j])   # Variables in factor
        s += "%s %s\n" % (n_loc, 2)   # Number of values each variable can take
        s += "%s\n" % (n_loc * 2)     # Number of nonzero entries in factor table

        cpt = np.empty((n_loc,2))
        cpt[:,0] = 1 - epsilon
        cpt[:,1] = epsilon
        cpt[j,:] = [epsilon, 1 - epsilon]
        cpt_flat = cpt.T.flatten()
        for i in range(len(cpt_flat)):
            s += "%s %s\n" % (i, cpt_flat[i])

        s += "\n"

    return s, n_loc

def y_id(i, j, n_obj, n_loc):
    """ Observed variables have indices starting from n_loc """
    return n_obj + (i * n_loc) + j

def main():
    if len(sys.argv) != 3:
        print("Usage: python %s n_obj n_loc" % sys.argv[0])

    else:
        n_obj = int(sys.argv[1])
        n_loc = int(sys.argv[2])

        epsilon = 0.1 # Failure probability

        s = ""
        n_factors = 0

        # Factors to enforce no two objects at the same location
        for i in range(n_obj):
            for j in range(n_obj):
                if i < j:
                    s, n = add_unique_factor(s, i, j, n_loc)
                    n_factors += n

        # Factors describing emission probabilities
        for i in range(n_obj):
            s, n = add_emission_factors(s, i, [y_id(i,j,n_obj,n_loc) for j in range(n_loc)], n_loc, epsilon)
            n_factors += n

        print("%s\n" % n_factors)
        print(s)

if __name__ == '__main__':
    main()



