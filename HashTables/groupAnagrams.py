"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.


Example:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
"""

def groupAnagrams(strs):
    m = {}

    for s in strs:
        hash = ''.join(sorted(s))

        if hash not in m:
            m[hash] = []

        m[hash].append(s)

    r = []

    for x in m.values():
        r.append(x)

    return r


if __name__ == '__main__':
    x = ["eat","tea","tan","ate","nat","bat"]

    print('*')
    print(groupAnagrams(x))
    print('*')
