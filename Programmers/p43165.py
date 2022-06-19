from collections import deque

def solution(number, target):
    que = deque([])

    que.append([number[0], 0])
    que.append([-1 * number[0], 0])

    count = 1

    answer = 0

    while len(que) > 0:
        i, j = que.popleft()

        if j < len(number)-1:
            que.append([i+number[j+1], j + 1])
            que.append([i+(-1 * number[j+1]), j + 1])     

        if j == len(number)-1 and i == target:
            answer += 1


    return answer