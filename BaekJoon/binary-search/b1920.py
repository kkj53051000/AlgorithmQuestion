n = int(input())

nList = list(map(int, input().split()))

m = int(input())

mList = list(map(int, input().split()))

nList.sort()

def binary_search(nList, targetNum):

    start = 0
    end = len(nList) -1

    while start <= end:
        mid = nList[(start + end) // 2]

        if mid == targetNum:
            return True
        elif mid > targetNum:
            end = mid - 1
        else:
            start = mid + 1

    return False
    
for m in mList:
    if(binary_search(nList, m)):
        print(1)
    else:
        print(0)




