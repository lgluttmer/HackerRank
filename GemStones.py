import sys
import re
write = sys.stdout.write

# Constraints function
def constraints(num, low_bound, high_bound):
    return num < low_bound or num > high_bound

# Find gem_elements
# Recursive function that finds common letters in two elements of list
def gem_elements(rocks):
    A = set(str(rocks[0]).rstrip())
    B = set(str(rocks[1]).rstrip())
    # Find the set intersection
    gems = set.intersection(A, B)
    gems = ''.join(gems)
    # If list has length 2, you're done
        if len(rocks) == 2:
            print len(gems)
    # Otherwise add the intersection to the rest of the list and repeat
        else:
            rocks = [gems] + rocks[2:]
            gem_elements(rocks)

# Read in inputs
inputs = sys.stdin.readlines()

# Number of rocks constraints
N = int(inputs[0])
if constraints(N, 1, 100):
    sys.exit("Error. Number of rocks does not follow constraints.")

# Composition constraints
rocks = inputs[1:]
if constraints(len(rocks), N, N):
    sys.exit("Error. Incorrect number of rocks provided.")
for k in rocks:
    k = str(k).rstrip()
    if constraints(len(k), 1, 100):
        sys.exit("Error. Improper composition length.")
    if re.search(r"[^a-z]", k) is not None:
        sys.exit("Error. Compositions may only contain 'a'-'z'.")

gem_elements(rocks)
