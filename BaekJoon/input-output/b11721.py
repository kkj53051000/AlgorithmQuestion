# https://www.acmicpc.net/problem/11721

word = list(input())

tempWord = ""

for i in range(0, len(word)):
    tempWord += word[i]

    if (len(tempWord) % 10) == 0 or i == len(word) -1:
        print(tempWord)
        tempWord = ""