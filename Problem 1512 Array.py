# Given an array of integers nums.

# A pair (i,j) is called good if nums[i] == nums[j] and i < j.

# Return the number of good pairs.

# My Solution || accepted 40ms || brute force
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        a=[]
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if(nums[i]==nums[j]):
                    a.append((i,j))
        return len(a)