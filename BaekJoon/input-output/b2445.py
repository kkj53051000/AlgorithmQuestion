# https://www.acmicpc.net/problem/2445

t = int(input())

for i in range(0, t):
    for j in range(0, i+1):
        print("*", end="")
    for j in range(t-i, 1, -1):
        print(" ", end="")
    for j in range(t-i, 1, -1):
        print(" ", end="")
    for j in range(0, i+1):
        print("*", end="")
    print("")
for i in range(0, t-1):
    for j in range((t-i)-1, 0, -1):
        print("*", end="")
    for j in range(0, i+1):
        print(" ", end="")
    for j in range(0, i+1):
        print(" ", end="")
    for j in range((t-i)-1, 0, -1):
        print("*", end="")
    print("")