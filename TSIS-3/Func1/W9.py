import math
def Vol(Rad):
    return (4/3) * math.pi*pow(Rad, 3)

Rad= int(input())
print(float(Vol(Rad)))