n = int(input())

inputArr = []
arr = []

answer = []

for i in range(0, n):
    now = str(input())
    inputArr.append(now)

for now in inputArr:
    
    # 5글자 이상 즉, push일때 arr.append()
    if(len(now) > 5): 
        arr.append(int(now[5:len(now)]))

    
    if (now == "pop"):
        if (len(arr) > 0):
            print(arr.pop())
        else:
            print(-1)

    if now == "size":
        print(len(arr))
    
    if (now == "empty"):
        if (len(arr) == 0):
            print("1")
        else:
            print("0")
        
    
    if now == "top":
        if len(arr) > 0:
            print(arr[-1])
        else:
            print(-1)