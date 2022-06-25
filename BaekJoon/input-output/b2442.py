# https://www.acmicpc.net/problem/2442

t = int(input())

startNum = 1

for i in range(0, t):
    for j in range((t-i)-1, 0, -1):
        print(" ", end="")
    for j in range(0, startNum):
        print("*", end="")
    print("")
    startNum += 2