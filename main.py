# Author: Jasmine Singh
# Github Username: Jassig98
# Date: October 18, 2022
# Description: Fall_Distance.py

def fall_distance(t): #fuction
    g=9.8
    distance=(1/2)*g*t*t
    return distance
t=float(input())
distance=fall_distance(t)
print(distance)

