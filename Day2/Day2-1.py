import re

#Puzzle Input
puzzleinput = open('./Day2/input2.txt', 'r').read().split('\n')
countTrue = 0
for line in puzzleinput:
    policy = line.replace(':','').split(' ')
    numbers = [int(s) for s in re.findall(r'\b\d+\b', policy[0])]

    minL = numbers[0]
    maxL = numbers[1]
    password = policy[2]
    letter = policy[1]
    countL = len(re.findall(letter, password))
    
    if(countL >= minL and countL <= maxL):
        countTrue += 1

print(countTrue)



    # print(f'{countL} {minL} {maxL} {letter} {password} {countL >= minL and countL <= maxL}')







