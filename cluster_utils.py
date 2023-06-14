import math
from collections import defaultdict


def reduce_clusters(c_tuple_list):

    """Takes in an unordered list of c_tuples. Identifies clusters of c_tuples by overlapping area.
    Then returns a list of c_tuples where each item in the list corresponds to one c_tuple per cluster of the highest area.

    The length of the returned list should equal the number of clusters formed from the original c_tuple list
    :param c_tuple_list: A list of c_tuple definitions in the form [(x, y, r), (x, y, r), ... ]
    :return: A list of c_tuple definitions in the form [(x, y, r), (x, y, r), ... ]"""

    clustered_list = cluster_overlapping_circles(c_tuple_list)
    reduced_cluster = []
    for cluster in clustered_list:
        largest_circle_index = 0
        for i in range(1, len(cluster)):
            if cluster[largest_circle_index][2] < cluster[i][2]:
                largest_circle_index = i
        reduced_cluster.append(cluster[largest_circle_index])

    return reduced_cluster


def are_circles_overlapping(c_tuple1, c_tuple2):

    # calculate the distance between centers of two circles
    distance = math.sqrt((c_tuple2[1] - c_tuple1[1]) ** 2 + (c_tuple2[1] - c_tuple1[1]) ** 2)

    if distance <= c_tuple1[2] + c_tuple2[2]:
        return True  # Circles Overlapping
    else:
        return False  # Circles Not Overlapping


def cluster_overlapping_circles(c_tuple_list):

    # Create adjacency matrix to represent the graph
    circle_count = len(c_tuple_list)
    graph = defaultdict(list)

    for i in range(circle_count):
        for j in range(i+1, circle_count):
            if are_circles_overlapping(c_tuple_list[i], c_tuple_list[j]):
                graph[i].append(j)
                graph[j].append(i)

    # Find the clusters by traversing the graph depth first
    visited = set()
    cluster_list = []
    for i in range(circle_count):
        if i not in visited:
            my_stack = [i]
            cluster = []
            while my_stack:
                item = my_stack.pop()
                if item not in visited:
                    cluster.append(c_tuple_list[item])
                    visited.add(item)
                    my_stack.extend(graph[item])
            cluster_list.append(cluster)

    return cluster_list


def main():
    # Test Data
    sample1 = [(0.5, 0.5, 0.5), (0.7, 0.7, 0.4), (4, 4, 0.7), (1.5, 1.5, 1.1)]
    sample2 = [(1.5, 1.5, 1.3), (4, 4, 0.7)]
    sample3 = [(1, 3, 0.7), (2, 3, 0.4), (3, 3, 0.9)]

    # print the reduced clusters
    print(reduce_clusters(sample1))


if __name__ == "__main__":
    main()


