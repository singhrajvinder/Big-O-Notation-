import random
import time

def generateClockList(total, size):
    clock = [1] * size
    remain = total - size
    while remain:
        addition = random.randint(1, min(remain,6))
        index = random.randint(0, size-1)

        clock[index] += addition
        remain -= addition

    return clock

def checkSequence(clock, power, start, end):
    goal = 2*10**power
    if start >= end:
        start, end = end+1, start-1
        goal = 10**power

    if sum(clock[start:end+1]) == goal:
        return True
    else:
        return False


def generalClockProblem(clock, power):
    total= 0
    start = 0
    end = 0
    count = 0
    max = 2*10**power
    min = 10**power
    while total != min and total != max:
        if count == len(clock)+1:
            count =0
        if count < len(clock) and total < max:
            total += clock[count]
        if total == min:
            end = start-1
            start = count+1
        elif total == max:
            end = count
        elif total > max:
            total -= clock[start]
            start +=1
            if total == max:
                end = count
        if total < max:
            count+=1
    return (start,end)

# This section creates a list like we went over in class
# if you would like to visualize
#print(3)
#clock = generateClockList(30, 12)
#print(clock)
#result = generalClockProblem(clock, 1)
#print(result)
#print(checkSequence(clock, 1, *result))
#################################################################################
##################### YOU DO NOT NEED TO TOUCH THIS #############################
#################################################################################

test_powers = 6
ind_test_cases = 100
test_cases = test_powers*ind_test_cases
correct = 0
total_time = 0

for power in range(1, test_powers+1):
    print("Now working on power of N={0}".format(power))
    for i in range(ind_test_cases):
        clock = generateClockList(3*10**power, 10**power + random.randint(1, 10**power))
        stime = time.time()
        result = generalClockProblem(clock, power)
        total_time += (time.time() - stime)
        correct += checkSequence(clock, power, *result)

print("You passed {0} out of {1} test cases for a score of {2:.2f}%".format(correct, test_cases, correct/test_cases*100))
print("It took your code {0:.5f} seconds to complete".format(total_time))
