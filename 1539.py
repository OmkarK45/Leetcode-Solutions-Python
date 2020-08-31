nums = [2,3,4,7,11]
k=5
missing_set = set(range(0,1000)) - set(nums)
lst = list(missing_set)
print(len(lst))