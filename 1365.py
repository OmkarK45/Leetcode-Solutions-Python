# How many numbers smaller than current one Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].

Return the answer in an array.
# Brute force \\ not recommended \\ 296ms my worst ever

nums = [8,1,2,2,3]
a=[]
for i in nums:
    count=0
    for j in nums:
        if(j<i):
            count=count+1
    a.append(count)
print(a)