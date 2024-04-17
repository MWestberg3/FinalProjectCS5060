# This file contains the two optimal stopping algorithms
#
import math
import random

def optimal_stop(rand_set):
    solutions = 0
    sal = []
    opt_solutions = 0
    length = len(rand_set)
    iterations = 0

    for experiment in range(10000):
        iterations += 1
        random.shuffle(rand_set)
        #sets the optimal that we are looking for from rand_set
        optimal = 0
        for k in range(length):
            if rand_set[k] > optimal:
                optimal = rand_set[k]

        #read through first 37% and hold onto the highest value as 'max'
        threshold = int(0.37 * length)
        max = 0
        for i in range(threshold):
            if rand_set[i] > max:
                max = rand_set[i]

        #choices is what is left after the 37%
        choices = rand_set[threshold:]

        #loop through the choices for 'solution'
        for j in range(len(choices)):
            if choices[j] == optimal:
                opt_solutions += 1
                sal.append(optimal)
                break
            elif choices[j] > max:
                solutions += 1
                break

    #prints the percentage of times that the optimal solution was found
    total = 0
    for s in range(len(sal)):
        total += sal[s]
    found = opt_solutions / (iterations / 100)
    avg_opt_sol = total / opt_solutions
    print("Pt. 1")
    print("Optimal solution found {} times out of {} iterations.".format(opt_solutions, iterations))
    print("The optimal solution was found {}% of the time".format(found))
    print("The average optimal solution found was: {}\n".format(avg_opt_sol))



def optimal_stop_pt_2(dict):
    length = len(dict)
    iterations = 0
    net = [] # rewards

    for experiment in range(100000):
        iterations += 1
        keys = list(dict.keys())
        random.shuffle(keys)

        optimal = 0
        for k in range(len(keys)):
            key = keys[k]
            sal = key.split(".")[0]
            val = int(sal) + (21000 - (17.5 * int(dict[key])))
            if val > optimal:
                optimal = val


        threshold = math.ceil(0.1 * length)
        max = 0
        for i in range(threshold):
            key = keys[i]
            sal = key.split(".")[0]
            val = int(sal) + (21000 - (17.5 * int(dict[key])))
            if val > max:
                max = val
        choices = keys[threshold:]


        for j in range(len(choices)):
            key = choices[j]
            sal = key.split(".")[0]
            val = int(sal) + (21000 - (17.5 * int(dict[key])))
            if val == optimal:
                net.append(optimal)
                break
            elif val > max:
                net.append(val)
                break

    mean = 0
    for n in range(len(net)):
        mean += net[n]

    mean = mean / iterations
    print("Pt. 2")
    print("The first year net profit based on {} iterations is: {}".format(iterations, mean))

