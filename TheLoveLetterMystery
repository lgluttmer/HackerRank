import sys
import re
write = sys.stdout.write

# Constraints function
def constraints(num, low_bound, high_bound):
    return num < low_bound or num > high_bound

# Palindrome Function
def palindrome(case):
    count = 0
    l = len(case)
    for i in range(l/2):
        count += abs(ord(case[i]) - ord(case[l-1-i]))
    print count        
    
# Read in inputs
inputs = sys.stdin.readlines()

# Number of test cases constraints
T = int(inputs[0])
if constraints(T, 1, 10):
   sys.exit("Error. Number of testcases does not follow constraints.")

# Read in each test case
testcases = inputs[1:]
if constraints(len(testcases), T, T):
    sys.exit("Error. Incorrect number of strings provided.")
for case in testcases:
    case = str(case).rstrip()
    if constraints(len(case), 1, 10**4):
        sys.exit("Error. Length of string does not follow constraints.")
    if re.search(r"[^a-z]", case) is not None:
        sys.exit("Error. Strings may only contain 'a'-'z'.")
    palindrome(case)
