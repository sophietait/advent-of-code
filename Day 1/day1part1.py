import os

f = open("input.txt")
lines = f.read().splitlines()

sum = 0

for x in lines:
    fuelRequired = int(int(x)/3)-2
    sum = sum + fuelRequired

print(sum)
f.close()

