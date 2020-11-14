"""
The i-th person has weight people[i], and each boat can carry a maximum weight of limit.

Each boat carries at most 2 people at the same time, provided the sum of the weight of those people is at most limit.

Return the minimum number of boats to carry every given person.  (It is guaranteed each person can be carried by a boat.)
"""

def numRescueBoats(people, limit):
    left = 0
    rigth = len(people)-1

    people.sort()

    boats = 0

    while left <= rigth:
        if left == rigth:
            boats += 1
            break

        if(people[left]+people[rigth] <= limit):
            left += 1

        boats += 1
        rigth -= 1

    return boats

if __name__ == '__main__':
    people = [2, 1, 3, 4]
    limit = 4

    boats_number = numRescueBoats(people, limit)

    print(boats_number)
