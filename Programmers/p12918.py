# https://programmers.co.kr/learn/courses/30/lessons/12918

s = "a234"

sLen = len(s)

if (not (sLen == 4 or sLen == 6)):
    print("False")

numCheck = True

for i in s:
    if not i.isdigit():
        numCheck = False
    
if numCheck:
    print("True")
else:
    print("False")