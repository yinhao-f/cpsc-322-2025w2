import matplotlib.pyplot as plt
import math

csv = open("rs_1.csv")

num_of_samples = 0
num_of_accepted = 0
num_of_true = 0
x_list = []
y_list = []
upper = []
lower = []

target_N = {7587, 63197, 95735, 100000}

for line in csv:
    num_of_samples += 1
    sample = int(line.strip())

    if num_of_samples in target_N:
        if num_of_accepted > 0:
            prob = num_of_true / num_of_accepted
            print(f"N={num_of_samples}: P(+r|+s,+w) ≈ {prob}")
        else:
            print(f"N={num_of_samples}: undefined (no accepted samples yet)")

    # Rejected
    if sample == -1:
        continue

    # Accepted
    num_of_accepted += 1

    if sample == 1:
        num_of_true += 1

    prob = num_of_true / num_of_accepted
    
    x_list.append(num_of_samples)
    y_list.append(prob)


    epsilon = math.sqrt(- math.log(0.025) / (2 * num_of_accepted))
    upper.append(min(prob + epsilon, 1))
    lower.append(max(prob - epsilon, 0))
    
plt.figure()
plt.plot(x_list, y_list, label='Approximate')
plt.plot(x_list, upper, label='Upper Confidence Bound')
plt.plot(x_list, lower, label='Lower Confidence Bound')
plt.xscale('log')

plt.xlabel("Number of generated samples N")
plt.ylabel("P(+r|+s,+w)")

plt.title("Rejection Sample Graph")

print(num_of_samples)
print(num_of_accepted)
print(num_of_true)

plt.legend()
plt.show()