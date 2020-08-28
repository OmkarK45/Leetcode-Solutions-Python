# Given an array nums of integers, return how many of them contain an even number of digits.

# My Solution using external fx \\ 
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        counter = 0
        converted = self.converter(nums)
        for i in converted:
            if len(i) % 2 == 0:
                counter += 1
        return counter
        
        
        
    def converter(self, nums):
        convert = []
        for i in nums:
            convert.append(str(i))
        return convert