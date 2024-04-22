import random
import numpy as np

def find_optimal_stopping_point(mean, std_dev):
    len_candidates = 100
    solution_found_count = {}
    optimal_solution_found_count = {}
    for i in range(1, len_candidates):
        solution_found_count[str(i)] = 0
        optimal_solution_found_count[str(i)] = 0

    for experiment in range(1000):
        c = np.random.normal(mean, std_dev, len_candidates)
        candidates = c.tolist()
        optimal_candidate = max(candidates)
        for i in range(1, len_candidates):
            for candidate in candidates[i:-1]:
                if candidate > max(candidates[0:i]):
                    solution_found_count[str(i)] += 1
                    if candidate == optimal_candidate:
                        optimal_solution_found_count[str(i)] += 1

                    break
    return max(optimal_solution_found_count, key=optimal_solution_found_count.get)


def stopping_percentage(mean, std_dev):
    optimal_sp_string = find_optimal_stopping_point(mean, std_dev)
    optimal_sp_int = int(optimal_sp_string) / 100
    return optimal_sp_int