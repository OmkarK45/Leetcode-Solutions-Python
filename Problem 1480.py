# Running sum of 1d array
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        j=0
        new=[]
        for i in range(0, len(nums)):
            j+=nums[i]
            new.append(j)
        return new