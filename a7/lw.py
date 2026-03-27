# Likelihood Weighting

import matplotlib.pyplot as plt
import math

csv = open("lw_1.csv")

num_of_samples = 0
total_weight = 0
true_weight = 0
x_list = []
y_list = []
upper = []
lower = []

target_N = {12741, 44349, 84558, 100000}

for line in csv:
    num_of_samples += 1
    sample, weight = line.strip().split(',')
    sample = sample == "True"
    weight = float(weight)

    total_weight += weight

    if sample:
        true_weight += weight

    prob = true_weight / total_weight

    if num_of_samples in target_N:
        print(f"N={num_of_samples}: P(+r|+s,+w) ≈ {prob}")
    
    x_list.append(num_of_samples)
    y_list.append(prob)

    epsilon = math.sqrt(- math.log(0.025) / (2 * num_of_samples))
    upper.append(min(prob + epsilon, 1))
    lower.append(max(prob - epsilon, 0))
    
plt.figure()
plt.plot(x_list, y_list, label='Approximate')
plt.plot(x_list, upper, label='Upper Confidence Bound')
plt.plot(x_list, lower, label='Lower Confidence Bound')
plt.xscale('log')

plt.xlabel("Number of generated samples N")
plt.ylabel("P(+r|+s,+w)")

plt.title("Likelihood Weighting Graph")

print("Number of samples =", num_of_samples)
print("Total true weight =", true_weight)
print("Total weight =", total_weight)

plt.legend()
plt.show()