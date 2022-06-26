# https://programmers.co.kr/learn/courses/30/lessons/76502
from collections import deque

s = "[)(]"
s = deque(s)

open = ['(', '{', '[']

openDic = {
    ')':'(',
    '}':'{',
    ']':'['
}

answer = 0

for n in range(0, len(s)-1):


    stackList = deque([])

    count = 0

    check = True

    for i in range(0, len(s)):
        if s[i] in open:
            stackList.append(s[i])
        elif len(stackList) > 0 and openDic.get(s[i]) == stackList[len(stackList)-1]:
            stackList.pop()
        else:
            check = False
        
        print(stackList)

    if len(stackList) > 0:
        check = False

    if check:
        answer += 1

    temp = s.popleft()
    s.append(temp)

print(answer)