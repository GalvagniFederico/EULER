import math
from collections import defaultdict



def connections(attempt):
    l = len(attempt)
    for i in range(l - 1):
        for j in range(i + 1, l):
            yield attempt[i], attempt[j]


def make_number_graph(keylog):
    graph = defaultdict(set)
    for attempt in keylog:
        for a, b in connections(attempt):
            graph[a].add(b)
    return graph

def PassCodeDerivation():
    attempts = [str(int(line)) for line in open("file/079_Attempts.txt", "r").readlines()]
    
    print(make_number_graph(attempts))


PassCodeDerivation()