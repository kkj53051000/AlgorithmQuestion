# https://www.acmicpc.net/problem/11720

t = int(input())

num = str(input())

sum = 0

for i in range(0, t):
    sum += int(num[i])

print(sum)