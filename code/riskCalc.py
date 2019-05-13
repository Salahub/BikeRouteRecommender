from coordDistance import coordDist
    
def calcRisk(edge):
    ''' calculates risk weight
        INPUT: edge - Edge() object as defined in StreetGraph.py
        OUTPUT: calculated risk value
    '''
    src = edge.getSource()
    dest = edge.getDestination()
    d = coordDist(src.lat,src.lon,dest.lat,dest.lon)
    risk = (src.risk+dest.risk)*d/2
    return risk