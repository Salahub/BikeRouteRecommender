from coordDistance import coordDist
import math as m
    
def calcComf(edge):
    ''' calculates discomfort weight
        INPUT: edge - Edge() object as defined in StreetGraph.py
        OUTPUT: calculated comfort value
    '''
    src = edge.getSource()
    dest = edge.getDestination()
    dh = dest.h - src.h
    if dh < -0.025:
        dh = -0.025
    d = coordDist(src.lat,src.lon,dest.lat,dest.lon)
    grade = dh/(d*1000)
    comf = d*(2*m.exp(15*grade)-1)
    return comf