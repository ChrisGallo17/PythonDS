'''
Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.
Example: Input: [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
'''
def findMaxLength(nums):
    count = 0
    ht = {0:-1}
    length = 0
    for i in range(len(nums)):
        if nums[i] == 1:
            count += 1
        else:
            count -= 1
        if count in ht:
            length = max(length, i - ht[count])
        else:
            ht[count] = i
    return length
