"""
Generate random path through graph
"""

import random
from route import puget

def traverse(graph, n):
    """
    Generate random path of length up to n through graph
    """
    assert n > 0
    start = random.choice([ here for (here,there) in graph])
    path = [ start ]
    n -= 1
    while n > 0:
        neighbors = [ there for (here,there) in graph
                      if here == path[-1]]
        if neighbors:
            path.append(random.choice(neighbors))
            n -= 1
        else:
            break
    return path

print traverse(puget, 4)



