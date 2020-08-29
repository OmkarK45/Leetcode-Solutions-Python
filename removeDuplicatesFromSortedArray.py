# Remove duplicates from sorted array 
nums = [0,0,1,1,1,2,2,3,3,4]

i=0
for j in range(i+1, len(nums)):
    if(nums[i]!= nums[j]):
        i+=1
        nums[i] = nums[j]
return i+1