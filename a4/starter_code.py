# Import necessary libraries and CSP example
from cspExamples import csp1  # You can replace with crossword1 or another CSP
from cspSLS import SLSearcher, Runtime_distribution
import matplotlib.pyplot as plt


# Parameters to test
prob_best_values = [0.0,  0.3, 0.5, 0.7, 1.0] # Probabilities for selecting the best variable, how much greedy our search is
results = [] # Store results of each run for plotting
num_runs = 100 # Number of runs to perform for each probability setting
num_steps = 100 # Maximum number of steps to take in each run



# # TODO: Create a function to run the SLSearcher with varying probabilities
def run_stochastic_search(csp, prob_best, prob_anycon, max_steps=num_steps):
#     """
#     Runs the stochastic local search on a given CSP using the SLSearcher class.

#     Parameters:
#     - csp: The Constraint Satisfaction Problem (CSP) to solve.
#     - prob_best: The probability of selecting the best variable (one involved in the most constraints).
#     - prob_anycon: The probability of selecting any variable involved in a conflict.
#     - max_steps: The maximum number of steps for the search before giving up (default is 1000).

#     Returns:
#     - steps: The number of steps taken to find a solution, or None if no solution is found.
#     """

#     # TODO: Initialize the SLSearcher with the given CSP
    sl_searcher = SLSearcher(csp)

#     # TODO: Perform the search with the given probabilities and max steps
    steps = sl_searcher.search(max_steps, prob_best, prob_anycon)

    return steps, sl_searcher.current_assignment



# TODO: Run the search with different probabilities for multiple runs
for prob_best in prob_best_values:
        
    # TODO: Perform multiple runs to gather data
    for run in range(num_runs):

        # TODO: Call the stochastic search function with the current parameters
        steps, current_assignment = run_stochastic_search(csp1, prob_best, 1, num_steps)

        # TODO: Append the results, including the probabilities, run number, and steps taken
        result = [prob_best, run, steps]
        results.append(result)

        print(f"prob_best={prob_best}, run={run}, steps={steps}")
