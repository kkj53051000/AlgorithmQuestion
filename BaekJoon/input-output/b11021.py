# https://www.acmicpc.net/problem/11021

t = int(input())

for i in range(0, t):
    a, b = map(int, input().split())

    print("Case #" + str(i+1) + ":", a+b)