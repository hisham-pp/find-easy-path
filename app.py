#!/usr/bin/env python3

import itertools
import math
import time

def distance(p1, p2):
    return math.dist(p1, p2)

def total_path_distance(path):
    dist = 0
    for i in range(len(path) - 1):
        dist += distance(path[i], path[i + 1])
    return dist

def find_shortest_path(points):
    start_time = time.time()

    shortest_path = None
    shortest_distance = float("inf")

    for perm in itertools.permutations(points):
        dist = total_path_distance(perm)
        if dist < shortest_distance:
            shortest_distance = dist
            shortest_path = perm

    end_time = time.time()

    return shortest_path, shortest_distance, end_time - start_time


# Example points (x, y)
points = [
    (0, 0),
    (3, 3),
    (5, 8),
    (1, 7),
    (6, 1),
     (0, 0),
    (3, 3),
    (5, 8),
    (1, 7),
    (6, 1), (0, 0),
    (3, 3),
    (5, 8),
    (1, 7),
    (6, 1), (0, 0),
    (3, 3),
    (5, 8),
    (1, 7),
    (6, 1),
]

path, distance_value, time_taken = find_shortest_path(points)

print("Shortest Path:", path)
print("Total Distance:", distance_value)
print("Time Taken:", time_taken, "seconds")
