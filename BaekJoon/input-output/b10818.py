# https://www.acmicpc.net/problem/10818

t = int(input())

numList = map(int, input().split())

min = 1000000
max = -1000000

for n in numList:
    if n < min:
        min = n
    
    if n > max:
        max = n

print(min, max)