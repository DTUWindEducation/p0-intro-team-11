# main.py

import functions

# Test greet function
functions.greet("Hannah")

# Test goldilocks function
functions.goldilocks(130)

# Test square_list function
print(functions.square_list([1, 2, 3, 4]))

# Test fibonacci_stop function
print(functions.fibonacci_stop(0))

# Test clean_pitch function
x = [-1, 2, 6, 95]
status = [1, 0, 0, 0]
print(functions.clean_pitch(x, status))
