nums = [1,0,3,0,12]

def moveZeroes(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    if len(nums) > 1:
        p1, p0 = len(nums) - 1, len(nums) - 2
        for x in range(len(nums) - 1):
            if nums[p0] == 0:
                while p1 <= len(nums) - 1 and nums[p1] != 0:
                    nums[p1-1] = nums[p1]
                    nums[p1] = 0
                    p1 += 1
                p1 = p0 + 1
            p1 -= 1
            p0 -= 1
    print(nums)

moveZeroes(nums)