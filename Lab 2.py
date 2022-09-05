#Jean Lorentz
#9/2/22
#this program will calculate the weight of an object on earth and convert it to the weight on the moon

import math

#asking user for input
weightOnEarth =float(input("Enter an  object's weight on Earth (in lbs):"))

#this section of the code converts the objects weight to lbs and oz
moonWeightoz = (weightOnEarth*.165*16)
moonlbs= (moonWeightoz//16)
moonOz=(moonWeightoz%16)
print("The object's weight on the Moon is",moonlbs,"lbs",int(moonOz),"oz")  

#This section of the code converts the objects weight to kg and g
moonWeightgrams = weightOnEarth*453.592*.165
moonKg = (moonWeightgrams//1000)
moonGrams= (moonWeightgrams%1000)
print("The object's weight on the moon is",moonKg,"kg",int(moonGrams),"g")

#This section of the code converts to objects weight on planet Pythoid

#finding pythoid lbs
insideOfSqRt= ((math.pow(weightOnEarth,2)-13)/8)+22
pythoidtotallbs=4* (insideOfSqRt**(1/2))

#converting lbs to oz
pythoidWeightOz=pythoidtotallbs*16

#finding seperate lbs and oz
pythoidlbs=pythoidWeightOz//16
pythoidOz=pythoidWeightOz%16
print("The object's weight on plant Pythoid is",pythoidlbs, "lbs" , int(pythoidOz) , "oz")


