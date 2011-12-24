from vehicle import *
from pedestrian import pedestrian
from random import randint

width = 65  # portion of one-dimensional space included in view

nvehicles = 2
vehicles = [ vehicle(float(randint(1,width-1)),float(randint(-5,5)))
                     for i in range(nvehicles) ]

# one safe vehicle
# in demo, initially comment out safe_vehicle, uncomment later
vehicles.append(safe_vehicle(float(randint(1,width-1)),
                             float(randint(-5,5)), icon='S'))
    
for v in vehicles: print v,'   ',
print

def clear(view):
    for i in range(width): view[i] = '.'    
    
nsteps = 10
stoplight = 'G' # green, go
view = list('.'*width)
for t in range(nsteps):
    clear(view)
    # in demo, initially comment out pedestrian, uncomment later
    if t == 6: vehicles.append(pedestrian(randint(1,width-1)))
    if t >= 6: stoplight = 'R' # red, stop        
    for v in vehicles:
        v.move(signals=stoplight)
        v.draw(view)
    print ''.join(view), stoplight # generate string from view



    
