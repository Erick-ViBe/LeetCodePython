"""
Given a string s, find the length of the longest substring without repeating characters.

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""

def lengthOfLongestSubstring(s):
    n = len(s)

    left = 0
    rigth = 0

    r = 0
    m = {}

    while left<n and rigth<n:
        el = s[rigth]

        if el in m:
            left = max(left, m[el]+1)

        m[el] = rigth

        r = max(r, (rigth-left)+1)

        rigth += 1

    return r


if __name__ == '__main__':
    x = 'abaacad'

    r1 = lengthOfLongestSubstring(x)

    y = 'abcabcbb'

    r2 = lengthOfLongestSubstring(y)

    print(r1)
    print('**********************')
    print(r2)
