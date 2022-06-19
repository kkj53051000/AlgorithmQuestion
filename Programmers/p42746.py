# https://programmers.co.kr/learn/courses/30/lessons/42746

numbers = [3, 30, 34, 5, 9]	
numbersLen = []

for n in numbers:
    numbersLen.append(len(str(n)))

maxNumLen = 4

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
    num, len = n

    if len < maxNumLen:
        answerList.append(int(num / 10 ** (maxNumLen - len)))
    else:
        answerList.append(num)

print(answerList)

answer = ""

for n in answerList:
    answer += str(n)

print(answer)