import math
#example 1
a = float(input("Input degree: "))
b = a*(math.pi/180)
print("Output radian:", b)

#example 2
Height = int(input("Height: "))
firstvalue = int(input("Base, first value: "))
secondvalue = int(input("Base, second value: "))
area1 = float(((firstvalue+secondvalue)/2)*Height)
print("Expected Output:", area1)

#example 3
sides = int(input("Input number of sides: "))
length = int(input("Input the length of a side: "))
area2 = float(0.5*(sides*length)*(length/2*( math.sin(math.pi/sides) / math.cos(math.pi/sides) ) ) )
print("The area of the polygon is:", area2)

#example 4
length1 = int(input("Length of base: "))
height1 = int(input("Height of parallelogram: "))
area3 = length1*height1
print("Expected Output:", area3)
