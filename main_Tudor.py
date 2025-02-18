from functions_Tudor import *

greet("there")

goldilocks(130)

print(square_list([1, 2, 3, 4]))

print(fibonacci_stop(100))

x = [-1, 2, 6, 95]  # "raw" pitch angle at four time steps
status = [1, 0, 0, 0]  # status signal
print(clean_pitch(x, status))