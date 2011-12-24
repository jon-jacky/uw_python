""""
Graphs and paths
"""

# A collection of pairs can describe a graph of nodes connected by edges

puget = (('Seattle', 'Bremerton'),
        ('Seattle', 'Tacoma'),
        ('Tacoma', 'Olympia'),
        ('Tacoma', 'Shelton'),
        ('Bremerton', 'Shelton'), 
        ('Shelton', 'Olympia'))

def check(graph, *path):
    """
    True when path given by sequence of args exists in graph
    """
    assert len(path) > 1
    for i in range(len(path)-1):
        if not path[i:i+2] in graph:
            return False
    return True

if __name__ == '__main__':
    print check(puget, 'Seattle', 'Bremerton', 'Shelton', 'Olympia') # True
    print check(puget, 'Seattle', 'Tacoma', 'Shelton', 'Olympia')    # True
    print check(puget, 'Seattle', 'Bremerton', 'Tacoma', 'Olympia')  # False
    



        
            
        
