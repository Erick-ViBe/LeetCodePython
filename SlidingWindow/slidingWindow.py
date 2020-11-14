def maxSum(arr, k):
    """Return maximun sum of k consequtive elements of an array"""

    if len(arr) <= k:
        print("Invalid operation")
        return -1

    window_sum = sum(arr[0:k])
    max_sum = window_sum

    for i in range (len(arr)-k):
        window_sum = window_sum - arr[i] + arr[i+k]

        max_sum = max(max_sum, window_sum)

    return max_sum


if __name__ == '__main__':

    arr = [80, -50, 90, 100, -70]
    k = 3

    print (maxSum(arr, k))
