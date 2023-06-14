def reduce_clusters(ctuple_list):

"""
Takes in an unordered list of ctuples. Identifies clusters of ctuples by overlapping area.
Then returns a list of ctuples where each item in the list corresponds to one ctuple per
cluster of the highest area.

The length of the returned list should equal the number of clusters formed from the original
ctuple list
 :param ctuple_list: A list of ctuple definitions in the form [(x, y, r), (x, y, r), ... ]
 :return: A list of ctuple definitions in the form [(x, y, r), (x, y, r), ... ]
"""


