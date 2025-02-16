#functions.py

# 1. Write a simple function 
# Define a function called greet that takes a name as a string, then prints "Hello, <name>!" to the screen.
def greet(name):
    print(f"Hello, {name}!")
#greet("Hannah")

# 2. If/else statements
#Goldilocks is 135 cm tall, and she is very picky about the size of her bed. If the bed is shorter than 140 cm, 
# or larger than 150 cm, then she is unhappy. Write a function called goldilocks that takes the length of a bed 
# in cm and prints whether goldilocks is happy with it. Be sure to distinguish whether the bed is too small or too large!

def goldilocks(bed_length):
    if bed_length < 140:
        print("Too small!")
    elif bed_length > 150:
        print("Too large!")
    else:
        print("Just right!")
#goldilocks(130) 

# 3. For loops
# Write a function called square_list that takes a list of numbers and returns a list where each element has been squared.

def square_list(numbers):
    return [num ** 2 for num in numbers]
#print(square_list([1, 2, 3, 4]))

# 4. While loops
# Write a function called fibonacci_stop that returns a list of the Fibonacci numbers up to a specified maximum value.
# Recall that the Fibonacci sequence is a sequence in which the next number is the sum of the previous two numbers: 1, 1, 2, 3, 5, etc.

def fibonacci_stop(max_value):
    if max_value < 1:
        return []
    
    fib_sequence = [1, 1]

    while True:
        next_fib = fib_sequence[-1] + fib_sequence[-2]
        if next_fib > max_value:
            break
        fib_sequence.append(next_fib)
    
    return fib_sequence

#print(fibonacci_stop(0))

# 5. Logical operators
# Instruments sometimes malfunction, returning incorrect values that can corrupt our analyses. 
# Pretend we have an instrument that returns the pitch angle of a wind turbine blade, which usually ranges 
# from 0 to 90 degrees, but can report occasional values outside that range. The instrument also records a status signal, 
# where 0 indicates that it is functioning normally but a positive value indicates some sort of malfunction. If a pitch 
# angle is outside of [0, 90] degrees and the instrument is malfunctioning, we want to set the pitch angle to -999 to indicate 
# a bad value. We ignore non-zero status signals if the pitch angle is in the correct range.

# Define a function called clean_pitch that takes two lists, one representing measurements from the pitch instrument at 
# certain points in time and the other representing the corresponding status signal. The function should return a cleaned 
# list of the pitch angle, where “good” values are untouched and “bad” values are set to -999.

def clean_pitch(x, status):
    '''Clean pitch angle data by setting bad values to -999.
    Parameters:
    - x (list of float): Recorded pitch angles.
    - status (list of int): Corresponding status signals (0 = normal, >0 = malfunctioning).
    '''
    cleaned_data = [] #initializing to store cleaned pitch angles

    for angle, stat in zip(x, status): #angle represents the pitch angle. stat represents the corresponding status signal.

        if (angle < 0 or angle > 90) and stat > 0:
                cleaned_data.append(-999)
        else:
                cleaned_data.append(angle)

    return cleaned_data

#x = [-1, 2, 6, 95]  # "raw" pitch angle at four time steps
#status = [1, 0, 0, 0]  # status signal
#print(clean_pitch(x, status))
