# https://www.acmicpc.net/problem/2446

# 0, 1, 2, 3, 4, 3, 2, 1, 0
# 9, 7, 5, 3, 1, 3, 5, 7, 9

t = int(input())

# Gap Num List

gapList = []

for i in range(0, t):
    gapList.append(i)

for i in range(len(gapList)-2, -1, -1):
    gapList.append(i)

# Star Num List
starList = []

maxStarNum = 1

for i in range(0, t-1):
    maxStarNum += 2

for i in range(maxStarNum, 0, -2):
    starList.append(i)

for i in range(len(starList)-2, -1, -1):
    starList.append(starList[i])

for i in range(0, (t*2)-1):
    for j in range(0, gapList[i]):
        print(" ", end="")
    
    for j in range(0, starList[i]):
        print("*", end="")
    
    print("")