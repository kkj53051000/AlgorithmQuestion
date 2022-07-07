# https://school.programmers.co.kr/learn/courses/30/lessons/42747

citations = [3, 0, 6, 1, 5]	

citations.sort()

answer = 0

for i in range(0, len(citations)):
    h = citations[i]

    # h번 이상 인용된 논문이 h편 이상
    if len(citations)-i >= h:
        answer = h
    
print(answer)