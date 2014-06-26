# Constraints function
def constraints(num, low_bound, high_bound):
    return num < low_bound or num > high_bound

# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(raw_input())
if constraints(T, 1, 1000):
    sys.exit("Error. Inputs do not follow constraints.")
for i in range (0,T):
    N,C,M = [int(x) for x in raw_input().split(' ')]
    if constraints(N, 2, 10**5) or constraints(C, 1, N) or constraints(M, 2, N):
        sys.exit("Error. Inputs do not follow constraints.")
    candy = N/C
    wrappers = N/C
    while wrappers >= M:
        candy += 1
        wrappers -= (M - 1)
    print candy
