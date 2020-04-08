def maxSubArray(nums):
    p1, p2, max = 0, 0, 0
    while p1 < len(nums):
        sub = 0
        p2 = p1
        while p2 < len(nums):
            sub += nums[p2]
            if sub > max:
                max = sub
            p2 += 1
        p1 += 1
    return(max)
    # runs in O(n^2), time exceeded

def maxSubArrayN(nums):
    for x in range(1, len(nums)):
        if nums[x] + nums[x-1] > nums[x]:
            nums[x] = nums[x] + nums[x-1]
    return max(nums)


ex = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

print(maxSubArray(ex))
