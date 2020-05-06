'''
Given an array nums of n integers where n > 1,  return an array output such that 
output[i] is equal to the product of all the elements of nums except nums[i].
'''

class Solution:
    def productExceptSelf(self, nums):
        prodL = [1]
        prodR = [1]
        j = len(nums)-1

        for i in range(1, len(nums)):
            prodL.append(prodL[i - 1] * nums[i - 1])
            
        for i in range(1, len(nums)):
            prodR.insert(0, prodR[0] * nums[j])
            j -= 1

        for i in range(len(nums)):
            nums[i] = prodL[i] * prodR[i]

        return nums

    def productExceptSelf1(self, nums):
        ans = [1] * len(nums)
        l, r = 1, 1

        for i in range(len(nums)):
            ans[i] *= l
            ans[-1-i] *= r
            l *= nums[i]
            r *= nums[-1-i]

        return ans

s = Solution()
print(s.productExceptSelf1([1,2,3,4]))
