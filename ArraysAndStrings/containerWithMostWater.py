"""
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.

Notice that you may not slant the container.

https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/17/question_11.jpg
"""

def maxArea(height):
    left = 0
    rigth = len(height)-1

    max_area = 0

    while left < rigth:
        max_area = max(max_area, min(height[left], height[rigth])*(rigth-left))

        if(height[left] < height[rigth]):
            left += 1
        else:
            rigth -= 1

    return max_area


if __name__ == '__main__':
    x = [1, 8, 6, 2, 5, 4, 8, 3, 7]

    result = maxArea(x)

    print(result)
