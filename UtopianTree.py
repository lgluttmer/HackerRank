import sys
write = sys.stdout.write

# Constraints function
def constraints(num, low_bound, high_bound):
    return num < low_bound or num > high_bound

# Function that determines if a number is even
def isEven(number):
    return number % 2 == 0

# Function that finds height of tree for one testcase
def test(element):
    height = 1
    for x in xrange(element):
        # Height of tree doubles during monsoon cycles
        if isEven(x):
            height = height * 2
        # Tree grows 1 m during summer cycles
        else:
            height = height + 1
    return height

# Create a list of integers out of the input lines
my_list = map(int, sys.stdin.readlines())

# Number of testcases
T = my_list[0] 

# Testcases
my_list = my_list[1:len(my_list)]
N = len(my_list) 

# Check constraints and find tree height
if constraints(T, 1, 10) or constraints(N, 0, 60):
    sys.exit("Error. Input variables don't follow constraints.")
elif constraints(T, N, N):
    sys.exit("Error. Incorrect number of testcases.")
else:
    for element in my_list[:]:
        print test(element)

