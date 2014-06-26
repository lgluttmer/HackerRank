import sys
write = sys.stdout.write

# Constraints function
def constraints(num, low_bound, high_bound):
    return num < low_bound or num > high_bound

# Function that determines if a number is even
def isEven(number):
    return number % 2 == 0

# Cut Function
def cuts(case):
    if isEven(case):
        w = case / 2
        l = case / 2
    else:
        w = (case + 1) / 2
        l = (case - 1) / 2
    print w * l
    
# Read in inputs
inputs = sys.stdin.readlines()

# Number of test cases constraints
T = int(inputs[0])
if constraints(T, 1, 10):
   sys.exit("Error. Number of testcases does not follow constraints.")

# Read in each test case
testcases = inputs[1:]
if constraints(len(testcases), T, T):
    sys.exit("Error. Incorrect number of testcases provided.")
for case in testcases:
    case = int(case)
    if constraints(case, 2, 10**7):
        sys.exit("Error. Number of cuts does not follow constraints.")
    cuts(case)
