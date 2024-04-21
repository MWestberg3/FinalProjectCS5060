import numpy as np
import random
from optimalStop import *


#lines 8-20 are creating a random dataset based on
# Parameters
low = 56000
high = 100000
mean = (low + high) / 2
std_dev = (high - mean) / 3  # Adjust the factor (e.g., 3) to control spread

# Generate Gaussian distribution
data = np.random.normal(mean, std_dev, 1200)
list = []
data_list = []
data_list_2 = {}

# put in average jobs offers received out of the 1200 applications
# also include in part 2 at what job offer your most likely to land a job


for value in data:
    list.append(value)

for i in range(len(list)):
    if random.random() <= 0.0072:
        data_list.append(list[i])
        data_list_2[str(list[i])] = i


optimal_stop(data_list)
optimal_stop_pt_2(data_list_2)

