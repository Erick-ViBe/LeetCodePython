"""
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

    LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
    int get(int key) Return the value of the key if the key exists, otherwise return -1.
    void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.

Follow up:
Could you do get and put in O(1) time complexity?

Example:

Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4
"""
from collections import deque

class LRUCache:
    def __init__(self, capacity: int):
        self.c = capacity
        self.m = dict()
        self.deq = deque()

    def get(self, key: int) -> int:
        if key not in self.m:
            return -1
        else:
            self.deq.remove(key)
            self.deq.append(key)

            return self.m[key]

    def put(self, key: int, value: int) -> int:
        if key not in self.m:
            if self.c == len(self.deq):
                lastKey = self.deq.popleft()
                del self.m[lastKey]
        else:
            self.deq.remove(key)

        self.deq.append(key)
        self.m[key] = value

if __name__ == '__main__':
    s = LRUCache(3)

    s.put(1, 1000)
    s.put(2, 2000)
    s.put(3, 3000)

    #[ 1, 2, 3 ]

    print(s.get(1)) # 1000

    #[ 2, 3, 1 ]

    s.put(4, 4000)

    # least <= [ 3, 1, 4 ] => most

    print(s.get(2)) # -1

    print(s.get(3)) # 3000 

    #[ 1, 4, 3 ]

    print('*')
    print(s.m)
    print('*')
    print(s.deq)
    print('*')
