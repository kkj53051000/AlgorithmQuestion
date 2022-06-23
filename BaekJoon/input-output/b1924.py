# https://www.acmicpc.net/problem/1924

from datetime import date

x, y = map(int, input().split())

dateDict = {0:'TUE', 1: 'WED', 2:'THU', 3: 'FRI', 4: 'SAT', 5:'SUN', 6: 'MON'}

print(dateDict[date(2017, x, y).weekday()])
