# https://school.programmers.co.kr/learn/courses/30/lessons/42883
import itertools

def solution(number, k):
    answer = ''
    answerInt = 0

    lenList = []

    for i in range(0, len(number)):
        lenList.append(i)

    combinationList = itertools.combinations(lenList, len(number)-k)

    for i in combinationList:
        
        cSum = ""

        for c in i:
            cSum += number[c]
        
        if answerInt < int(cSum) :
            answerInt = int(cSum)

        
    
    answer = str(answerInt)

    return answer

    

if __name__ == '__main__':
    print(solution("1231234", 3))