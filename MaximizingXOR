#!/bin/python

# Constraints function
def constraints(num, low_bound, high_bound):
    return num < low_bound or num > high_bound

# Brute force method
def  maxXor( l,  r):
    my_max = 0
    for i in range(l, r+1):
        for j in range(l, r+1):
            if i^j > my_max:
                my_max = i^j
    return my_max

_l = int(raw_input());
_r = int(raw_input());
if constraints(_l, 1, _r) or constraints(_r, _l, 10**3):
   sys.exit("Error. Integers do not follow constraints.")

res = maxXor(_l, _r);
print(res)
