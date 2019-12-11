import os

f = open("input.txt")
lines = f.read().splitlines()

total = 0

def fuelRequired(x):
    return int(int(x)/3)-2

for x in lines:
    sum = 0

    while int(x) >= 9:
        x = fuelRequired(x)
        sum = sum + x

    total = total + sum
print (total)
f.close()