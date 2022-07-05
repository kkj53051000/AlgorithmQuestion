# https://school.programmers.co.kr/learn/courses/30/lessons/12909

s = "()()"
stack = []


for st in s:
    if st == '(':
        stack.append('(')
    elif st == ')' and len(stack) > 0:
        stack.pop()
    else:
        print("false")


if len(stack) > 0:
    print("false")