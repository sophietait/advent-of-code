import os

f = open("input.txt")
stringLines = f.read().split(',')
lines = list(map(int, stringLines))

def add(x):
    y = lines[x+1]
    z = lines[x+2]
    lines[lines[x+3]] = lines[y] + lines[z]

def multipy(x):
    y = lines[x+1]
    z = lines[x+2]
    lines[lines[x+3]] = lines[y] * lines[z]
    x = x+4

lines[1] = 12
lines[2] = 2
x = 0
while True:
    if lines[x] == 1:
        add(x)
        x = x + 4

    if lines[x] == 2:
        multipy(x)
        x = x + 4

    if lines[x] == 99:
        break
print(lines[0])

f.close()