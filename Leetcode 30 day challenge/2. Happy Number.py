# A happy number is a number defined by the following process: 
#   Starting with any positive integer, replace the number by the sum 
#   of the squares of its digits, and repeat the process until the number 
#   equals 1 (where it will stay), or it loops endlessly in a cycle which 
#   does not include 1. Those numbers for which this process ends in 1 
#   are happy numbers.
 
# Input: 19
# Output: true
# Explanation:
# 1^2 + 9^2 = 82
# 8^2 + 2^2 = 68
# 6^2 + 8^2 = 100
# 1^2 + 0^2 + 0^2 = 1

class Solution:
    def isHappy(self, n: int) -> bool:
        s = set()
        num = n
        while num not in s:
            s.add(num)
            sum = 0
            while num != 0:
                sum += (num % 10) ** 2
                num //= 10
            num = sum
            if num == 1:
                return True
        return False
