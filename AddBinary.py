# 67. Add Binary
# Given two binary strings a and b, return their sum as a binary string.

# Example 1:

# Input: a = "11", b = "1"
# Output: "100"
# Example 2:

# Input: a = "1010", b = "1011"
# Output: "10101"

import os

def AddBinary(a, b):
    dec_a = int(a, 2)
    dec_b = int(b, 2)

    res = str(dec_a + dec_b)

    bin_res = bin(int(res))
    return bin_res[2:]

print(AddBinary("1010", "1011"))
os._exit(0)