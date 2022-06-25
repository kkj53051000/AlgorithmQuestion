# https://www.acmicpc.net/problem/2440

t = int(input())

for i in range(t, 0, -1):
    
    for j in range(0, i):
        print("*", end="")
    print("")