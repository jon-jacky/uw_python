"""
Monte Carlo simulation of a queue of vehicles at an intersection
"""

import random

vehicles = ('bus','auto','bike')

queue = []  # intially empty

def arrive():
    """
    select random vehicle and add to end of queue, return vehicle
    """
    v = random.choice(vehicles)
    queue.append(v)
    return v

def depart():
    """
    remove vehicle from head of queue, return vehicle
    """
    return queue.pop(0)

def run(n=3, s=None):
    """
    Run simulation of a queue of vehicles at an intersection
    n = number of vehicles that arrive
    seed = random seed, use any seed > 0 to make run reproducible
    """
    random.seed(s)
    while n > 0 or queue:
        f = random.choice((arrive, depart))
        if (f == arrive and n > 0) or (f == depart and queue):
            v = f()
            print '%s %s: %s' % (v, f.__name__, queue)
        if f == arrive:
            n -= 1            

if __name__ == '__main__':
    run()


            
 
    



