
import random
import csv
import sys
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

def find_optimal_stopping_point():
    len_candidates = 100
    solution_found_count = {}
    optimal_solution_found_count = {}
    for i in range(1, len_candidates):
        solution_found_count[str(i)] = 0
        optimal_solution_found_count[str(i)] = 0

    for experiment in range(10000):
        candidates = random.sample(range(0,1000), len_candidates)
        optimal_candidate = max(candidates)
        for i in range(1, len_candidates):
            for candidate in candidates[i:-1]:
                if candidate > max(candidates[0:i]):
                    solution_found_count[str(i)] += 1
                    if candidate == optimal_candidate:
                        optimal_solution_found_count[str(i)] += 1
                        
                    break
    return max(optimal_solution_found_count, key=optimal_solution_found_count.get)

def find_max_optimal_stopping_point(distribution):
    len_candidates = 100
    solution_found_count = {}
    optimal_found_count = {}
    for i in range(1, len_candidates):
        solution_found_count[str(i)] = 0
        optimal_found_count[str(i)] = 0
        

    if distribution == "NORMAL":
        for experiment in range(10000):
            candidates = np.random.normal(50, 10, len_candidates)
            candidates = np.clip(candidates, 1, 99)
            integer_values = np.round(candidates).astype(int)

            candidates_minus_cost = []
            for i in range(len_candidates):
                candidates_minus_cost.append(integer_values[i]-i)
            optimal_normal_candidate = max(candidates_minus_cost)

            for i in range(1, len_candidates):
                for candidate in candidates_minus_cost[i:-1]:
                    if candidate > max(candidates_minus_cost[0:i]):
                        solution_found_count[str(i)] += 1
                        if candidate == optimal_normal_candidate:
                            optimal_found_count[str(i)] += 1

    ### COMMENTED OUT - LEFT IN FOR TESTING TO SEE DATA UPON GRADING ###
        # sns.distplot(candidates, hist=False)
        # plt.show()
            
        # print("\nCandidates:")
        # print(integer_values)
        # print("\nReward Candidates:")
        # print(candidates_minus_cost)
        # print("\nOptimal Candidate:")
        # print(optimal_normal_candidate)
        
        # x, y = zip(*optimal_found_count.items())
        
        # print("\nX-Values:")
        # print(x)
        # print("\nY-Values:")
        # print(y)
        # print("\nOptimal Solutions Found Count:")
        # print(optimal_found_count)
        # plt.plot(x,y)
        # plt.show()
    
    elif distribution == "UNIFORM":
        for experiment in range(10000):
            candidates = np.random.uniform(1, 99, len_candidates)
            candidates = np.round(candidates).astype(int)
            candidates_minus_cost = []
            for i in range(len_candidates):
                candidates_minus_cost.append(candidates[i]-i)
            optimal_uniform_candidate = max(candidates_minus_cost)
            for i in range(1, len_candidates):
                for candidate in candidates_minus_cost[i:-1]:
                    if candidate > max(candidates_minus_cost[0:i]):
                        solution_found_count[str(i)] += 1
                        if candidate == optimal_uniform_candidate:
                            optimal_found_count[str(i)] += 1
                            
                        break
                    
    ### COMMENTED OUT - LEFT IN FOR TESTING TO SEE DATA UPON GRADING ###
        # sns.distplot(candidates, hist=False)
        # plt.show()
            
        # print("\nCandidates:")
        # print(candidates)
        # print("\nReward Candidates:")
        # print(candidates_minus_cost)
        # print("\nOptimal Candidate:")
        # print(optimal_uniform_candidate)
        
        # x, y = zip(*optimal_found_count.items())
        
        # print("\nX-Values:")
        # print(x)
        # print("\nY-Values:")
        # print(y)
        # print("\nOptimal Solutions Found Count:")
        # print(optimal_found_count)
        # plt.plot(x,y)
        # plt.show()
    return max(optimal_found_count, key=optimal_found_count.get)



def no_look_back(csv_list, optimal_stopping_point, max_value):
    stop = round(len(csv_list) * optimal_stopping_point)
    front_max = max(csv_list[0:stop])
    
    for value in csv_list[stop::]:
        if value == max_value:
            return value
        if value > front_max:
            return value

    return csv_list[len(csv_list) - 1]

def max_benefit_stopping(num_list, optimal_stopping_point, max_value):
    stop = round(len(num_list) * optimal_stopping_point)
    front_max = max(num_list[0:stop])

    for value in num_list[stop::]:
        if value == max_value:
            return value
        if value > front_max:
            return value
        
    return num_list[len(num_list) - 1]
    
if __name__=="__main__":
    filepath = sys.argv[1]
    distribution = sys.argv[2]
    
    optimal_sp_string = find_optimal_stopping_point()
    optimal_sp_int = int(optimal_sp_string) / 100
    print("(TASK1) Optimal Stopping Point is: " + optimal_sp_string + "%")
    
    with open(filepath, newline='') as csvfile:
        csv_contents = csv.reader(csvfile)
        data_list = list(csv_contents)
        candidates_list = []
        for row in data_list:
            if row != '' or row != '\n' or row != ' ':
                int_row = float(row[0])
                candidates_list.append(int_row)
    
    passes = 0
    failures = 0
    totals = 0
    max_value = max(candidates_list)
    print("Max Value in data set: " + str(max_value))
    
    for i in range(1000):
        random.shuffle(candidates_list)
    
        end_result = no_look_back(candidates_list, optimal_sp_int, max_value)
        
        if (end_result < max_value):
            failures += 1
        else:
            passes += 1
        
        totals += 1
    
    result = {'Pass': passes,
              'Fail': failures,
              'Total': totals}

    for key in result:
        print(key + ': ' + str(result[key]))
    print("Percent pass: " + str((result['Pass'] / result['Total']) * 100) + "%")
    
    
    if distribution == '-n' or distribution.lower() == 'normal':
        distribution = "NORMAL"
    elif distribution == '-u' or distribution.lower() == 'uniform':
        distribution = "UNIFORM"
    else:
        raise "ERROR: Distribution flag not recognized"

    optimal_max_benefit_str = find_max_optimal_stopping_point(distribution)
    print("(TASK2) Optimal Stopping Point for a Max Benefit Stopping Algorithm: " + optimal_max_benefit_str + "%")
    optimal_max_benefit_int = int(optimal_max_benefit_str) / 100

    result['Pass'] = 0
    result['Fail'] = 0
    result['Total'] = 0

    for i in range(1000):
        ## Generate a new list with a Normal Distribution ##
        if distribution == "NORMAL":
            random_list = np.random.normal(50, 10, 1000)
        
        ## Generate a new list with Uniform Distribution ##
        if distribution == "UNIFORM":
            random_list = np.random.uniform(1, 100, 1000)

        new_list = []
        for j in range(len(random_list)):
            new_list.append(random_list[j]-j)

        max_value = max(new_list)
        
        end_result = max_benefit_stopping(new_list, optimal_max_benefit_int, max_value)
        
        if (end_result < max_value):
            result['Fail'] += 1
        else:
            result['Pass'] += 1
        
        result['Total'] += 1
        
    for key in result:
        print(key + ': ' + str(result[key]))
    print("Percent pass: " + str((result['Pass'] / result['Total']) * 100) + "%")
        