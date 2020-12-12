#puzzle Input
puzzleinput = list(map(int,open('input1-1.txt', 'r').read().split('\n')))

for number1 in puzzleinput:
    for number2 in puzzleinput:
        for number3 in puzzleinput:
            if number1+number2+number3 == 2020:    
                print(number1 * number2 * number3)


input('Press ENTER to exit')