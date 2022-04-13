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
brng10 = 3.0124383 #Bearing is 172.6 degrees converted to radians.
d10 = .2092 #Distance in km


lat9 = math.radians(lat9) #Current lat point converted to radians
lon9 = math.radians(lon9) #Current long point converted to radians

lat10 = math.asin( math.sin(lat9)*math.cos(d10/R) +
     math.cos(lat9)*math.sin(d10/R)*math.cos(brng10))

lon10 = lon9 + math.atan2(math.sin(brng10)*math.sin(d10/R)*math.cos(lat9),
             math.cos(d10/R)-math.sin(lat9)*math.sin(lat9))

lat10 = math.degrees(lat10)
lon10 = math.degrees(lon10)

#print(lat10)
#print(lon10)
print(lat10, lon10, sep=",") #Prints a coordinate pair, sep adds the comma


R = 6378.1 #Radius of the Earth
brng11 = 2.6092672 #Bearing is 149.5 degrees converted to radians.
d11 = .2092 #Distance in km


lat10 = math.radians(lat10) #Current lat point converted to radians
lon10 = math.radians(lon10) #Current long point converted to radians

lat11 = math.asin( math.sin(lat10)*math.cos(d11/R) +
     math.cos(lat10)*math.sin(d11/R)*math.cos(brng11))

lon11 = lon10 + math.atan2(math.sin(brng11)*math.sin(d11/R)*math.cos(lat10),
             math.cos(d11/R)-math.sin(lat10)*math.sin(lat10))

lat11 = math.degrees(lat11)
lon11 = math.degrees(lon11)

#print(lat11)
#print(lon11)
print(lat11, lon11, sep=",") #Prints a coordinate pair, sep adds the comma


R = 6378.1 #Radius of the Earth
brng12 = 2.1834069 #Bearing is 125.1 degrees converted to radians.
d12 = .2092 #Distance in km


lat11 = math.radians(lat11) #Current lat point converted to radians
lon11 = math.radians(lon11) #Current long point converted to radians

lat12 = math.asin( math.sin(lat11)*math.cos(d12/R) +
     math.cos(lat11)*math.sin(d12/R)*math.cos(brng12))

lon12 = lon11 + math.atan2(math.sin(brng12)*math.sin(d12/R)*math.cos(lat11),
             math.cos(d12/R)-math.sin(lat11)*math.sin(lat11))

lat12 = math.degrees(lat12)
lon12 = math.degrees(lon12)

#print(lat12)
#print(lon12)
print(lat12, lon12, sep=",") #Prints a coordinate pair, sep adds the comma


R = 6378.1 #Radius of the Earth
brng13 = 1.7558012 #Bearing is 100.6 degrees converted to radians.
d13 = .2092 #Distance in km


lat12 = math.radians(lat12) #Current lat point converted to radians
lon12 = math.radians(lon12) #Current long point converted to radians

lat13 = math.asin( math.sin(lat12)*math.cos(d13/R) +
     math.cos(lat12)*math.sin(d13/R)*math.cos(brng13))

lon13 = lon12 + math.atan2(math.sin(brng13)*math.sin(d13/R)*math.cos(lat12),
             math.cos(d13/R)-math.sin(lat12)*math.sin(lat12))

lat13 = math.degrees(lat13)
lon13 = math.degrees(lon13)

#print(lat13)
#print(lon13)
print(lat13, lon13, sep=",") #Prints a coordinate pair, sep adds the comma


R = 6378.1 #Radius of the Earth
brng14 = 1.34914 #Bearing is 77.3 degrees converted to radians.
d14 = .2092 #Distance in km


lat13 = math.radians(lat13) #Current lat point converted to radians
lon13 = math.radians(lon13) #Current long point converted to radians

lat14 = math.asin( math.sin(lat13)*math.cos(d14/R) +
     math.cos(lat13)*math.sin(d14/R)*math.cos(brng14))

lon14 = lon13 + math.atan2(math.sin(brng14)*math.sin(d14/R)*math.cos(lat13),
             math.cos(d14/R)-math.sin(lat13)*math.sin(lat13))

lat14 = math.degrees(lat14)
lon14 = math.degrees(lon14)

#print(lat14)
#print(lon14)
print(lat14, lon14, sep=",") #Prints a coordinate pair, sep adds the comma


R = 6378.1 #Radius of the Earth
brng15 = 0.9180432 #Bearing is 52.6 degrees converted to radians.
d15 = .2092 #Distance in km


lat14 = math.radians(lat14) #Current lat point converted to radians
lon14 = math.radians(lon14) #Current long point converted to radians

lat15 = math.asin( math.sin(lat14)*math.cos(d15/R) +
     math.cos(lat14)*math.sin(d15/R)*math.cos(brng15))

lon15 = lon14 + math.atan2(math.sin(brng15)*math.sin(d15/R)*math.cos(lat14),
             math.cos(d15/R)-math.sin(lat14)*math.sin(lat14))

lat15 = math.degrees(lat15)
lon15 = math.degrees(lon15)

#print(lat15)
#print(lon15)
print(lat15, lon15, sep=",") #Prints a coordinate pair, sep adds the comma


R = 6378.1 #Radius of the Earth
brng16 = 0.5026548 #Bearing is 28.8 degrees converted to radians.
d16 = .2092 #Distance in km


lat15 = math.radians(lat15) #Current lat point converted to radians
lon15 = math.radians(lon15) #Current long point converted to radians

lat16 = math.asin( math.sin(lat15)*math.cos(d16/R) +
     math.cos(lat15)*math.sin(d16/R)*math.cos(brng16))

lon16 = lon15 + math.atan2(math.sin(brng16)*math.sin(d16/R)*math.cos(lat15),
             math.cos(d16/R)-math.sin(lat15)*math.sin(lat15))

lat16 = math.degrees(lat16)
lon16 = math.degrees(lon16)

#print(lat16)
#print(lon16)
print(lat16, lon16, sep=",") #Prints a coordinate pair, sep adds the comma


R = 6378.1 #Radius of the Earth
brng17 = 0.0820305 #Bearing is 4.7 degrees converted to radians.
d17 = .2092 #Distance in km


lat16 = math.radians(lat16) #Current lat point converted to radians
lon16 = math.radians(lon16) #Current long point converted to radians

lat17 = math.asin( math.sin(lat16)*math.cos(d17/R) +
     math.cos(lat16)*math.sin(d17/R)*math.cos(brng17))

lon17 = lon16 + math.atan2(math.sin(brng17)*math.sin(d17/R)*math.cos(lat16),
             math.cos(d17/R)-math.sin(lat16)*math.sin(lat16))

lat17 = math.degrees(lat17)
lon17 = math.degrees(lon17)

#print(lat17)
#print(lon17)
print(lat17, lon17, sep=",") #Prints a coordinate pair, sep adds the comma

#EVERYTHING BELOW THIS LINE IS ME TRYING TO FIGURE STUFF OUT

#This is trying to have it spit out a complete ffn.wpl write console script


#coordinates1 = {
    #math.degrees(lat15), math.degrees(lon15),
   # math.degrees(lat16), math.degrees(lon16),
   # lat17, lon17
               #} #I don't know why this one doesn't work. It looks like it groups all lons and lats together, instead of keeping them as pairs

coordinates2 = math.degrees(lat1),",", math.degrees(lon1),",", math.degrees(lat2),",", math.degrees(lon2),",", math.degrees(lat3),",", math.degrees(lon3),",", math.degrees(lat4),",", math.degrees(lon4),",", math.degrees(lat5),",", math.degrees(lon5),",", math.degrees(lat6),",", math.degrees(lon6),",", math.degrees(lat7),",", math.degrees(lon7),",", math.degrees(lat8),",", math.degrees(lon8),",", math.degrees(lat9),",", math.degrees(lon9),",", math.degrees(lat10),",", math.degrees(lon10),",", math.degrees(lat11),",", math.degrees(lon11),",", math.degrees(lat12),",", math.degrees(lon12),",", math.degrees(lat13),",", math.degrees(lon13),",", math.degrees(lat14),",", math.degrees(lon14),",", math.degrees(lat15),",", math.degrees(lon15),",", math.degrees(lat16),",", math.degrees(lon16),",", lat17,",", lon17

#print(coordinates2)

print("%ffn.wpl(false,[",*coordinates2,"])", sep="") #the *removes list formating (like brackets or parentheses), sep removes print's spacing, and I had to add the commas into the list