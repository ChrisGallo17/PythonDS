'''
You are given a string s containing lowercase English letters, and a matrix shift, where shift[i] = [direction, amount]:

direction can be 0 (for left shift) or 1 (for right shift). 
amount is the amount by which string s is to be shifted.
A left shift by 1 means remove the first character of s and append it to the end.
Similarly, a right shift by 1 means remove the last character of s and add it to the beginning.
'''


class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        count = self.countShift(shift)
        if count < 0:
            s = list(s)
            while count != 0:
                s.append(s.pop(0))
                count += 1
            s = "".join(s)
        elif count > 0:
            s = list(s)
            while count != 0:
                s.insert(0, s.pop())
                count -= 1
            s = "".join(s)
        return s

    def countShift(self, shift: List[List[int]]) -> int:
        count = 0
        for i in shift:
            if i[0] == 0:
                count -= i[1]
            else:
                count += i[1]
        return count
