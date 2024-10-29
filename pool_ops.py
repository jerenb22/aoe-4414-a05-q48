# pool_ops.py
#
# Usage: python3 pool_ops.py c_in h_in w_in h_pool w_pool s p
# This script calculates the output shape and operation count of an average pooling layer.
# Parameters:
# c_in: Input channel count
# h_in: Input height count
# w_in: Input width count
# h_pool: Average pooling kernel height count
# w_pool: Average pooling kernel width count
# s: Stride of average pooling kernel
# p: Amount of padding on each of the four input map sides
#
# Output:
# The output channel count, output height count, output width count,
# number of additions performed, number of multiplications performed,
# and number of divisions performed.
#
# Written by Jeren Browder
# Other contributors: None
#
# Optional license statement, e.g., See the LICENSE file for the license.

import sys  # For command-line arguments

# Calculate the output dimensions and operations for an average pooling layer
def calculate_average_pooling(c_in, h_in, w_in, h_pool, w_pool, s, p):
    c_out = c_in  # The number of channels remains the same in average pooling
    h_out = (h_in + 2 * p - h_pool) // s + 1
    w_out = (w_in + 2 * p - w_pool) // s + 1

    # Each pooling operation requires (h_pool * w_pool) additions and 1 division
    adds = h_out * w_out * c_out * (h_pool * w_pool - 1)
    muls = 0  # No multiplications in average pooling
    divs = h_out * w_out * c_out  # One division per pooling operation
    
    return c_out, h_out, w_out, adds, muls, divs

# Initialize script arguments
c_in = h_in = w_in = h_pool = w_pool = s = p = 0

# Parse script arguments
if len(sys.argv) == 8:
    c_in = int(sys.argv[1])
    h_in = int(sys.argv[2])
    w_in = int(sys.argv[3])
    h_pool = int(sys.argv[4])
    w_pool = int(sys.argv[5])
    s = int(sys.argv[6])
    p = int(sys.argv[7])
else:
    print('Usage: python3 pool_ops.py c_in h_in w_in h_pool w_pool s p')
    exit()

# Write script below this line
c_out, h_out, w_out, adds, muls, divs = calculate_average_pooling(c_in, h_in, w_in, h_pool, w_pool, s, p)

# Print the results
print(int(c_out))  # Output channel count
print(int(h_out))  # Output height count
print(int(w_out))  # Output width count
print(int(adds))   # Number of additions performed
print(int(muls))   # Number of multiplications performed
print(int(divs))   # Number of divisions performed
