# https://www.acmicpc.net/problem/2441

t = int(input())

for i in range(0, t):
    for j in range(0, i):
        print(" ", end="")
    for j in range(t-i, 0, -1):
        print("*", end="")
    print("")