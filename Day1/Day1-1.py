#Puzzle Input
puzzleinput = list(map(int,open('input1-1.txt', 'r').read().split('\n')))
answer = 0
# print(puzzleinput)

for number in puzzleinput:
    # print(number)
    otherNumber = 2020 - number
    if otherNumber in puzzleinput:
        answer = number * otherNumber

print(answer)
input('Press ENTER to exit')