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
print(lat1, lon1, sep=",") #Prints a coordinate pair, sep adds the comma

R = 6378.1 #Radius of the Earth
brng2 = 0.3036873 #Bearing is 17.4 degrees converted to radians.
d2 = .2092 #Distance in km


lat1 = math.radians(lat1) #Current lat point converted to radians
lon1 = math.radians(lon1) #Current long point converted to radians

lat2 = math.asin( math.sin(lat1)*math.cos(d2/R) +
     math.cos(lat1)*math.sin(d2/R)*math.cos(brng2))

lon2 = lon1 + math.atan2(math.sin(brng2)*math.sin(d2/R)*math.cos(lat1),
             math.cos(d2/R)-math.sin(lat1)*math.sin(lat1))

lat2 = math.degrees(lat2)
lon2 = math.degrees(lon2)

print(lat2)
print(lon2)


R = 6378.1 #Radius of the Earth
brng2 = 0.3036873 #Bearing is 17.4 degrees converted to radians.
d2 = .2092 #Distance in km


lat1 = math.radians(lat1) #Current lat point converted to radians
lon1 = math.radians(lon1) #Current long point converted to radians

lat3 = math.asin( math.sin(lat1)*math.cos(d2/R) +
     math.cos(lat1)*math.sin(d2/R)*math.cos(brng2))

lon3 = lon1 + math.atan2(math.sin(brng2)*math.sin(d2/R)*math.cos(lat1),
             math.cos(d2/R)-math.sin(lat1)*math.sin(lat1))

lat3 = math.degrees(lat2)
lon3 = math.degrees(lon2)

print(lat3)
print(lon3)