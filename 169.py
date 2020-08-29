# Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

# You may assume that the array is non-empty and the majority element always exist in the array.

nums = [3,2,3]
max=0
set_nums = set(nums)
for i in set_nums:
    count = nums.count(i)
    if(nums.count(i)>max):
        max=count
    if(max>len(nums)/2):
        print(i)
    