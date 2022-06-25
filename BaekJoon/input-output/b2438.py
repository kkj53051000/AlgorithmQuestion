# https://www.acmicpc.net/problem/2438

t = int(input())

for i in range(0, t):

    for j in range(0, i+1):
        print("*", end="")
    print("")