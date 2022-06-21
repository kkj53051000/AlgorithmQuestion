# https://programmers.co.kr/learn/courses/30/lessons/42746
from itertools import permutations

numbers = [12, 121]	
numbersLen = []

for n in numbers:
    numbersLen.append(len(str(n)))

maxNumLen = max(numbersLen)

newNumbers = []

for i in range(0, len(numbers)):
    nowLen = len(str(numbers[i]))
    now = numbers[i]
    if nowLen < maxNumLen:
        newNumbers.append([(10 ** (maxNumLen - nowLen)) * now, nowLen])
    else:
        newNumbers.append([now, nowLen])


newNumbers.sort(key=lambda x:x[0], reverse=True)

print(newNumbers)

answerList = []

for n in newNumbers:
    num, nowLen = n

    if nowLen < maxNumLen:
        answerList.append(int(num / 10 ** (maxNumLen - nowLen)))
    else:
        answerList.append(num)

print(answerList)

answer = ""

realAnswerList = []

for n in permutations(answerList):

    tempStr = ""
    for j in list(n):
        tempStr += str(j)
    realAnswerList.append(int(tempStr))

print(max(realAnswerList))