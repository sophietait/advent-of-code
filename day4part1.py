
start = [2,7,8,8,8,8]
end = [7,9,9,9,9,9]

total = 1

lines = start

def compare(x):
    if lines[x] <= lines[x + 1]:
        return True
    else:
        return False

for x in lines:
    if compare(x) == True:
        print(lines)
        if compare(x+1) == True:
            print(x)

    
