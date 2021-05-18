# Input: digits = [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.

class Solution(object):
    def plusOne(self, digits):
        return [int(i) for i in str(int("".join([str(i) for i in digits])) + 1)]
