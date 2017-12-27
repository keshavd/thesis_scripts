# Name:         distance_figures.py
# Author:       Keshav Dial
# Description:  Optimized Graphing Figure Script
#               Must be run in environment after 
#               kPOP has finished.

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import collections
import clustering.enums

##############
#GET DISTANCES
##############
gene_clusters = main.gene_clusters

for i, distance_array in enumerate(main.distance_arrays):
    families = sorted([e.name for e in clustering.enums.families.Families])
    collection_collections = []
    for family in families:
        intra_family_distances = []
        unrelated_distances = []
        for idx1, gc1 in enumerate(gene_clusters):
            for idx2, gc2 in enumerate(gene_clusters):
                if gc1.family is family:
                    if gc1.family == gc2.family:
                        intra_family_distances.append(distance_array[idx1][idx2])
                    else:
                        unrelated_distances.append(distance_array[idx1][idx2])
        intra_family_distances_collection = collections.Counter(intra_family_distances)
        unrelated_distances_collection = collections.Counter(unrelated_distances)
        collection_collections.append((intra_family_distances_collection, unrelated_distances_collection))
    ###########
    # PLOTTTING
    ###########
    for idx, family in enumerate(families):
        related = collection_collections[idx][0]
        unrelated = collection_collections[idx][1]
        all_distances = related + unrelated
        x =  sorted(all_distances)
        fig, ax =  plt.subplots()
        #first plot unrelated_distances
        y2 = [unrelated[i] for i in x]
        ax.stackplot(x, y2, color="Blue", alpha=0.5) 
        #second plot related_distances
        y1 = [related[i] for i in x]
        ax.stackplot(x, y1, color="Red", alpha=0.5)
        plt.savefig("distance_array_%s_%s.png" % (str(i),family))
        plt.clf()
