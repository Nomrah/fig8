import math

#TODO and random thoughts: d2-d7 can be same value (.2092) so don't need to increment the name. Only need three distances in reality (first distance from center, distance between turning WPs, and distance from top semi circle to bottom)
#TODO clean up bearings between waypoints. There's got to be a better way than me eye balling it

R = 6378.1 #Radius of the Earth
brng1 = 5.8032198 #Bearing is 332.5 degrees converted to radians.
d1 = 1.090 #Distance in km from the center point

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
d2 = .2092 #Distance in km from WP to WP, use this for the rest of the semi circle


lat1 = math.radians(lat1) #Current lat point converted to radians
lon1 = math.radians(lon1) #Current long point converted to radians

lat2 = math.asin( math.sin(lat1)*math.cos(d2/R) +
     math.cos(lat1)*math.sin(d2/R)*math.cos(brng2))

lon2 = lon1 + math.atan2(math.sin(brng2)*math.sin(d2/R)*math.cos(lat1),
             math.cos(d2/R)-math.sin(lat1)*math.sin(lat1))

lat2 = math.degrees(lat2)
lon2 = math.degrees(lon2)

#print(lat2)
#print(lon2)
print(lat2, lon2, sep=",") #Prints a coordinate pair, sep adds the comma


R = 6378.1 #Radius of the Earth
brng3 = 0.715585 #Bearing is 41 degrees converted to radians.
d3 = .2092 #Distance in km


lat2 = math.radians(lat2) #Current lat point converted to radians
lon2 = math.radians(lon2) #Current long point converted to radians

lat3 = math.asin( math.sin(lat2)*math.cos(d3/R) +
     math.cos(lat2)*math.sin(d3/R)*math.cos(brng3))

lon3 = lon2 + math.atan2(math.sin(brng3)*math.sin(d3/R)*math.cos(lat2),
             math.cos(d3/R)-math.sin(lat2)*math.sin(lat2))

lat3 = math.degrees(lat3)
lon3 = math.degrees(lon3)

#print(lat3)
#print(lon3)
print(lat3, lon3, sep=",") #Prints a coordinate pair, sep adds the comma


R = 6378.1 #Radius of the Earth
brng4 = 1.130973 #Bearing is 64.8 degrees converted to radians.
d4 = .2092 #Distance in km


lat3 = math.radians(lat3) #Current lat point converted to radians
lon3 = math.radians(lon3) #Current long point converted to radians

lat4 = math.asin( math.sin(lat3)*math.cos(d4/R) +
     math.cos(lat2)*math.sin(d4/R)*math.cos(brng4))

lon4 = lon3 + math.atan2(math.sin(brng4)*math.sin(d4/R)*math.cos(lat3),
             math.cos(d4/R)-math.sin(lat3)*math.sin(lat3))

lat4 = math.degrees(lat4)
lon4 = math.degrees(lon4)

#print(lat4)
#print(lon4)
print(lat4, lon4, sep=",") #Prints a coordinate pair, sep adds the comma


R = 6378.1 #Radius of the Earth
brng5 = 1.56556 #Bearing is 89.7 degrees converted to radians.
d5 = .2092 #Distance in km


lat4 = math.radians(lat4) #Current lat point converted to radians
lon4 = math.radians(lon4) #Current long point converted to radians

lat5 = math.asin( math.sin(lat4)*math.cos(d5/R) +
     math.cos(lat4)*math.sin(d5/R)*math.cos(brng5))

lon5 = lon4 + math.atan2(math.sin(brng5)*math.sin(d5/R)*math.cos(lat4),
             math.cos(d5/R)-math.sin(lat4)*math.sin(lat4))

lat5 = math.degrees(lat5)
lon5 = math.degrees(lon5)

#print(lat5)
#print(lon5)
print(lat5, lon5, sep=",") #Prints a coordinate pair, sep adds the comma


R = 6378.1 #Radius of the Earth
brng6 = 1.9739674 #Bearing is 113.1 degrees converted to radians.
d6 = .2092 #Distance in km


lat5 = math.radians(lat5) #Current lat point converted to radians
lon5 = math.radians(lon5) #Current long point converted to radians

lat6 = math.asin( math.sin(lat5)*math.cos(d6/R) +
     math.cos(lat5)*math.sin(d6/R)*math.cos(brng6))

lon6 = lon5 + math.atan2(math.sin(brng6)*math.sin(d6/R)*math.cos(lat5),
             math.cos(d6/R)-math.sin(lat5)*math.sin(lat5))

lat6 = math.degrees(lat6)
lon6 = math.degrees(lon6)

#print(lat6)
#print(lon6)
print(lat6, lon6, sep=",") #Prints a coordinate pair, sep adds the comma


R = 6378.1 #Radius of the Earth
brng7 = 2.3893557 #Bearing is 136.9 degrees converted to radians.
d7 = .2092 #Distance in km


lat6 = math.radians(lat6) #Current lat point converted to radians
lon6 = math.radians(lon6) #Current long point converted to radians

lat7 = math.asin( math.sin(lat6)*math.cos(d7/R) +
     math.cos(lat6)*math.sin(d7/R)*math.cos(brng7))

lon7 = lon6 + math.atan2(math.sin(brng7)*math.sin(d7/R)*math.cos(lat6),
             math.cos(d7/R)-math.sin(lat6)*math.sin(lat6))

lat7 = math.degrees(lat7)
lon7 = math.degrees(lon7)

#print(lat7)
#print(lon7)
print(lat7, lon7, sep=",") #Prints a coordinate pair, sep adds the comma


R = 6378.1 #Radius of the Earth
brng8 = 2.8152161 #Bearing is 161.3 degrees converted to radians.
d8 = .2092 #Distance in km


lat7 = math.radians(lat7) #Current lat point converted to radians
lon7 = math.radians(lon7) #Current long point converted to radians

lat8 = math.asin( math.sin(lat7)*math.cos(d8/R) +
     math.cos(lat7)*math.sin(d8/R)*math.cos(brng8))

lon8 = lon7 + math.atan2(math.sin(brng8)*math.sin(d8/R)*math.cos(lat7),
             math.cos(d8/R)-math.sin(lat7)*math.sin(lat7))

lat8 = math.degrees(lat8)
lon8 = math.degrees(lon8)

#print(lat8)
#print(lon8)
print(lat8, lon8, sep=",") #Prints a coordinate pair, sep adds the comma


R = 6378.1 #Radius of the Earth
brng9 = 3.6250489 #Bearing is 207.7 degrees converted to radians.
d9 = 2.119 #Distance in km, this is the long leg to bottom semi circle


lat8 = math.radians(lat8) #Current lat point converted to radians
lon8 = math.radians(lon8) #Current long point converted to radians

lat9 = math.asin( math.sin(lat8)*math.cos(d9/R) +
     math.cos(lat8)*math.sin(d9/R)*math.cos(brng9))

lon9 = lon8 + math.atan2(math.sin(brng9)*math.sin(d9/R)*math.cos(lat8),
             math.cos(d9/R)-math.sin(lat8)*math.sin(lat8))

lat9 = math.degrees(lat9)
lon9 = math.degrees(lon9)

#print(lat9)
#print(lon9)
print(lat9, lon9, sep=",") #Prints a coordinate pair, sep adds the comma


R = 6378.1 #Radius of the Earth
brng9 = 3.6250489 #Bearing is 207.7 degrees converted to radians.
d9 = 2.119 #Distance in km, this is the long leg to bottom semi circle


lat8 = math.radians(lat8) #Current lat point converted to radians
lon8 = math.radians(lon8) #Current long point converted to radians

lat9 = math.asin( math.sin(lat8)*math.cos(d9/R) +
     math.cos(lat8)*math.sin(d9/R)*math.cos(brng9))

lon9 = lon8 + math.atan2(math.sin(brng9)*math.sin(d9/R)*math.cos(lat8),
             math.cos(d9/R)-math.sin(lat8)*math.sin(lat8))

lat9 = math.degrees(lat9)
lon9 = math.degrees(lon9)

#print(lat9)
#print(lon9)
print(lat9, lon9, sep=",") #Prints a coordinate pair, sep adds the comma