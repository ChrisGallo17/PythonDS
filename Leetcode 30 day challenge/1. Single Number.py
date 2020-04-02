class Solution:
    def singleNumber(self, nums):
        s = set()
        for n in nums:
            if n in s:
                s.remove(n)
            else:
                s.add(n)
        return s.pop()

x = Solution()

example = [2,2,1,5,1]

print(x.singleNumber(example))