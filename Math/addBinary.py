"""
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example:

Input: a = "11", b = "1"
Output: "100"
"""

def addBinary(a, b):
    i = len(a)-1
    j = len(b)-1

    r = []
    carry = 0

    while i>=0 or j>=0 or carry:
        total = carry

        if i>=0:
            total+=int(a[i])
            i-=1

        if j>=0:
            total+=int(b[j])
            j-=1

        r.append(str(total%2))

        carry = total//2

    return ''.join(reversed(r))


if __name__ == '__main__':
    x = "1010"
    y = "1011"

    print("*")
    print(addBinary(x, y))
    print("*")
