# https://school.programmers.co.kr/learn/courses/30/lessons/42584

prices = [1, 2, 3, 2, 3]
answer = []

for i in range(0, len(prices)):
    tempAnswer = 0
    for j in range(i+1, len(prices)):
        if prices[i] <= prices[j]:
            tempAnswer += 1
        else:
            continue
    answer.append(tempAnswer)

print(answer)