import math

R = 6378.1 #Radius of the Earth
brng1 = 5.8032198 #Bearing is 332.5 degrees converted to radians.
d1 = 1.090 #Distance in km

centerLat = math.radians(20.0431489131703) #Current lat point converted to radians
centerLon = math.radians(-155.968645221192) #Current long point converted to radians

lat1 = math.asin( math.sin(centerLat)*math.cos(d1/R) +
     math.cos(centerLat)*math.sin(d1/R)*math.cos(brng1))

lon1 = centerLon + math.atan2(math.sin(brng1)*math.sin(d1/R)*math.cos(centerLat),
             math.cos(d1/R)-math.sin(centerLat)*math.sin(lat1))

lat1 = math.degrees(lat1)
lon1 = math.degrees(lon1)

#print(lat1)
#print(lon1)
print(lat1, lon1)