import re

#Puzzle Input
puzzleinput = open('./Day2/input2.txt', 'r').read().split('\n')
countTrue = 0
for line in puzzleinput:
    policy = line.replace(':','').split(' ')
    numbers = [int(s) for s in re.findall(r'\b\d+\b', policy[0])]

    password = policy[2]
    letter = policy[1]

    if(sum(map(bool, [password[numbers[0] - 1] == letter, password[numbers[1] - 1] == letter])) == 1):
        countTrue += 1

print(countTrue)






