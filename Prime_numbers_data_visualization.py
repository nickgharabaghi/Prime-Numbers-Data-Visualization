# Visualizes the data relating to prime numbers less than an upper limit, specified by the user
from numpy import *
from matplotlib.pyplot import *


def user_input():
    """
    Allows the user to pick an upper limit on the number of primes that they
    want to examine
    """
    while True:
        upper_limit = input("Display data for all prime numbers up to: ")
        try:
            upper_limit = int(upper_limit)
        except BaseException:
            print("Please enter a positive number")
        # We need the user to enter a positive number
        if type(upper_limit) == int:
            if upper_limit < 0:
                print("Please enter a positive number")
                continue
            return upper_limit


def find_primes(upper_limit):
    """
    Return a list of all primes less than the upper limit selected by the user.
    Uses the Sieve of Eratosthenes.
    """
    q = upper_limit + 1
    boolean_list = [True] * q
    # Creates a list of Boolean values, with the first entry corresponding to
    # the number 0, the second to the number 1, and so on, with the final entry
    # corresponding to the upper limit provided by the user

    # We begin by assuming that every number is prime, and then "cross out" the
    # numbers that are composite, leaving only prime numbers.

    for x in range(2, int(upper_limit**0.5 + 1)):
        # Loop through each item in boolean_list, starting from 2, up to the
        # largest whole number less than the square root of the upper limit
        # --> since the largest prime factor of any number must be less than its
        # square root
        if boolean_list[x]:
            # This if statement is triggered if the value is True 
            # (i.e if the xth number is prime)
            for y in range(x**2, q, x):
                # We can begin at x^2 because any smaller numbers must be either
                # prime, or already determined to be composite with a smaller
                # factor

                # Increment by x; all multiples of x will be "crossed out"
                boolean_list[y] = False
                # "Crosses out" the multiples of x
    primes = [z for z in range(2, q) if boolean_list[z]]
    # Creates a list of the actual prime numbers
    return primes


def create_all_digits_array(primes):
    """
    Associated with the first graph.

    Creates an array with 10 entries, one each for the digits 0 through 9.
    Stores the number of occurences of each digit in the prime numbers less
    than the upper limit.

    e.g. If the upper limit is 12:
            > The resulting primes will be 2, 3, 5, 7, 11
            > digit_array will be: [0   2   1   1  0   1   0   1   0   0],
              since there are 0 zeros, 2 ones (in the 11), one 2 (in the 2), etc.
    """
    all_digits_array = zeros(10, dtype=int32)
    for x in primes:
        str_prime = str(x)
        # Converts to a string to take advantage of the .count() method
        for y in range(10):
            all_digits_array[y] += str_prime.count("{}".format(y))
            # Cycles through the digits 0 through 9, and adds the number of
            # occurences of each digit to the corresponding entry of digit_array
    return all_digits_array


def all_digits_graph(all_digits_array, upper_limit):    
    """
    Associated with the first graph.

    Graphs the distribution of the digits contained within prime numbers
    """
    subplot(3,1,1)
    # There will be three graphs in total, and this is the first.
    zero_to_nine = linspace(0, 9, 10, dtype=int32)
    graph = bar(zero_to_nine, all_digits_array, tick_label=zero_to_nine, color="pink")
    # Creates a bar graph with 10 bars, one for each digit 0-9
    # The values of each bar are the number of times that digit occurs, from 

    title("Occurences of the digits in prime numbers up to {}".format(upper_limit))
    ylabel("Occurences")
    xlabel("Digits")
    # Provides a title and axis labels
    i = 0
    for a_bar in graph:
        height = a_bar.get_height()
        width = a_bar.get_width()
        x_coord = a_bar.get_x()
        text(x_coord + 0.5 * width, 0.5 * height, all_digits_array[i], fontsize = 8, ha='center', va='bottom')
        i += 1
    # Adds labels to the graph, displaying the exact value associated with
    # each column


def create_leading_digit_array(primes):
    """
    Associated with the second graph.

    Creates an array containing the number of times that each digit 0-9 is the leading 
    digit of a prime number less than the upper limit
    """
    leading_digit_array = zeros(10, dtype = int32)
    for x in primes:
        first_digit = x // (10 ** (int(math.log(x, 10))))
        # the log base 10 of x gives a float y such that (digits in x) < y < (digits in x + 1)
        # Taking the integer conversion of this float gives the number of digits in x, since int() truncates towards 0
        # The integer division // of x by 10 ^ (digits in x) gives the leading digit of x
        # --> e.g. 2303 // 1000 is 2. 56678 // 10000 is 5
        for y in range(10):
            if first_digit == y:
                leading_digit_array[y] += 1
    return leading_digit_array
    

def leading_digit_graph(leading_digit_array, upper_limit):
    """
    Associated with the second graph.

    Graphs the number of times one of the prime numbers less than the upper limit begins 
    with each digit 0-9
    """
    subplot(3,1,2)
    # This is the second graph
    zero_to_nine = linspace(0, 9, 10, dtype = int32)
    graph = bar(zero_to_nine, leading_digit_array, tick_label=zero_to_nine, color="tan")
    # Creates a bar graph with 10 bars, one for each digit
    # The values of each bar are the number of times that digit is the leading digit of a prime number

    title("Distribution of leading digits in prime numbers up to {}".format(upper_limit))
    ylabel("Occurences")
    xlabel("Digits")
    # Provides a title and axis labels

    i = 0
    for a_bar in graph:
        height = a_bar.get_height()
        width = a_bar.get_width()
        x_coord = a_bar.get_x()
        text(x_coord + 0.5 * width, 0.5 * height, leading_digit_array[i], fontsize = 8, ha='center', va='bottom')
        i += 1
    # Adds labels to the graph, displaying the exact value associated with
    # each column


def create_ending_digit_array(primes):
    """
    Associated with the third graph.

    Creates an array containing the number of times that each digit 0-9 is the final digit of a prime 
    number less than the upper limit
    """
    ending_digit_array = zeros(10, dtype = int32)
    for x in primes:
        remainder = x % 10
        # The final digit of x can be found as the remainder when x is divided by 10
        for y in range(10):
            if remainder == y:
                ending_digit_array[y] += 1
    return ending_digit_array


def ending_digit_graph(ending_digit_array, upper_limit):
    """
    Associated with the third graph.

    Graphs the number of times one of the prime numbers less than the upper limit ends with 
    each digit 0-9.
    """
    subplot(3,1,3)
    # This is the third graph.
    zero_to_nine = linspace(0, 9, 10, dtype = int32)
    graph = bar(zero_to_nine, ending_digit_array, tick_label=zero_to_nine, color="orange")
    # Creates a bar graph with 10 bars, one for each digit
    # The values of each bar are the number of times that digit is the final digit of a prime number

    title("Distribution of final digits in prime numbers up to {}".format(upper_limit))
    ylabel("Occurences")
    xlabel("Digits")
    # Provides a title and axis labels

    i = 0
    for a_bar in graph:
        height = a_bar.get_height()
        width = a_bar.get_width()
        x_coord = a_bar.get_x()
        text(x_coord + 0.5 * width, 0.5 * height, ending_digit_array[i], fontsize = 8, ha='center', va='bottom')
        i += 1
    # Adds labels to the graph, displaying the exact value associated with
    # each column    


def create_all_graphs(primes, upper_limit):
    """
    Creates a figure with all three graphs.
    1) Occurences of the digits in prime numbers up to _____
    2) Distribution of leading digits in prime numbers up to ______
    3) Distribution of final digits in prime numbers up to _____
    """
    overall_figure = figure("Data For Prime Numbers Up To {}".format(upper_limit))
    overall_figure.subplots_adjust(hspace = 1.0)
    overall_figure.suptitle("Data For Prime Numbers Up To {}".format(upper_limit))

    # First Graph: Total occurences of all digits in all primes less than upper limit
    all_digits_array = create_all_digits_array(primes)
    all_digits_graph(all_digits_array, upper_limit)

    # Second Graph: Frequency of prime numbers starting with each digit
    leading_digit_array = create_leading_digit_array(primes)
    leading_digit_graph(leading_digit_array, upper_limit)

    # Third Graph: Frequency of prime numbers ending with each digit
    ending_digit_array = create_ending_digit_array(primes)
    ending_digit_graph(ending_digit_array, upper_limit)

    show()
    # Creates a window displaying the graph


def run_program():
    """
    Runs the program
    """
    upper_limit = user_input()
    primes = find_primes(upper_limit)
    create_all_graphs(primes, upper_limit)


# ---------------------------------------------
run_program()