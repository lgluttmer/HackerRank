import sys
write = sys.stdout.write

# Constraints function
def constraints(num, low_bound, high_bound):
    return num < low_bound or num > high_bound

# Largest width allowed
def test(i, j, width):
    if width[i:j+1].count(1) > 0:
        return '1'
    elif width[i:j+1].count(2) > 0:
        return '2'
    else:
        return '3'

# Read in inputs
inputs = sys.stdin.readlines()

# Freeway length constraints
N = int(inputs[0].split()[0])
if constraints(N, 2, 100000):
    sys.exit("Error. Freeway length does not follow constraints.")

# Number of test cases constraints
T = int(inputs[0].split()[1])
if constraints(T, 1, 1000):
    sys.exit("Error. Number of testcases does not follow constraints.")
if constraints(T, len(inputs[2:]), len(inputs[2:])):
    sys,exit("Error. Incorrect number of testcases provided.")

# Define width array
width = map(int, inputs[1].split())
if constraints(N, len(width), len(width)):
    sys.exit("Error. Incorrect number of widths provided.")
    for k in width:
        if constraints(k, 1, 3):
            sys.exit("Error. Improper widths.")

# Analyze each testcase
for element in range(0, T):
    testcase = map(int, inputs[element+2].split())

    # Where Calvin enters service lane
    i = int(testcase[0])

    # Where Calvin exits service lane
    j = int(testcase[1])

    # Test enter and exit constraints
    if constraints(i, 0, N) or constraints(j, 0, N) or constraints(j - i + 1, 2, min(N, 1000)):
        sys.exit("Error. Testcase does not follow constraints.")

    print test(i, j, width)
