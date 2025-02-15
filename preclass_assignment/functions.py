import numpy as np

def greet():
    """Return a greeting to the user."""
    return "Hello, world!\n"

def square(num):
    """Return the square of a number."""
    return num ** 2

def square_list(list):
    return np.square(list)

def sqrt(num):
    """Return the square root of a number."""
    return num ** 0.5

def cube(num):
    """Return the cube of a number."""
    return num ** 3

def evaluate_line(a, b, x):
    """Calculate y = a*x + b for a number x."""
    return a*x + b

def evaluate_parabola(x, a, b, c):
    """Calculate y = a*x^2 + b*x + c for a number x."""
    return a**2 + b*x + c

def evaluate_line_list(a, b, inputs):
    """Map a list of inputs to a line according to y = a*x + b."""
    outputs = [None] * len(inputs)  # initialize our output list
    for index, x in enumerate(inputs):  # loop over our list of inputs, and use enumerate to get both the index and element
        y = evaluate_line(a, b, x)  # call the evaluate_line function from above
        outputs[index] = y  # assing the output to our output list
    return outputs  # return the list

def evaluate_parabola_list(xs, a=1, b=1, c=1):
    """Map a list of inputs to a parabola according to y = a*x^2 + b*x + c."""
    res = list()
    for x in xs:
        res.append(a*x**2 + b*x + c)
    return res


# Place the plotting code into a function so we can re-use it in later cells without copy-pasting
def plot_lines(x, y1, y2, label1, label2):
    """Make a function to plot two lines."""
    fig, ax = plt.subplots(figsize=(5, 3.5))  # initalize a figure and axes, specifying the aspect ratio

    ax.plot(x, y1, label=label1)  # plot the line data, and give it a label for the legend
    ax.plot(x, y2, linestyle='--', label=label2)  # plot the parabola data, making it a dashed line and giving a label

    ax.set(xlabel='x', ylabel='y')  # add labels to the x and y axes
    ax.legend()  # add a legend to the plot using the labelled data

    fig.tight_layout()  # scale everything to look pretty

    return ax

def clip_list(x, x_min, x_max):
    """Clip the values in a list so that they fall within the given max and min values."""
    x_clip = x
    for i, val in enumerate(x_clip):
        if val < x_min:
            x_clip[i] = x_min
        elif val > x_max:
            x_clip[i] = x_max
    return x_clip

def evaluate_line_numpy(a, b, x):
    """Evaluate a line y = a*x + b using NumPy."""
    x = np.array(x)  # convert x to a numpy array in case a list was passed in
    y = a*x + b  # evaluate line. no need for a for loop anymore!
    return y

def evaluate_parabola_numpy(x, a=1, b=1, c=1):
    x = np.array(x)
    return a*x**2 + b*x + c

def fibonacci_stop(N_max):
    """Return the first 15 numbers in the Fibonacci sequence."""
    fibonacci = list()
    for n in range(N_max+1):
        if n == 0:
            fibonacci.append(0)
        if n == 1:
            fibonacci.append(1)
        elif n > 1:
            fibonacci.append(fibonacci[-1] + fibonacci[-2])
    return fibonacci