import math as m
    
def coordDist(lat0, lon0, lat1, lon1):
    ''' calculate distance between two points given their (lat,lon) coordinates 
        INPUT: latitude and longitude of initial (0) and final (1) points
        OUTPUT: distance bewteen the two points in km
    '''
    dlat = lat1 - lat0; dlon = lon1 - lon0
    a = (m.sin(dlat/2*m.pi/180))**2 + m.cos(lat0*m.pi/180)*m.cos(lat1*m.pi/180)*(m.sin(dlon/2*m.pi/180))**2
    c = 2*m.atan2(a**0.5,(1-a)**0.5)
    d = 6371*c; # Earth Radius R = 6371 km    
    return d