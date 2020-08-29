nums = [12,14,13,19,19,19]
set_nums = set(nums)

if len(set_nums) == 1:
    print(nums[0]) 
elif len(set_nums) == 2:
    print(max(set_nums))
else:
    print(sorted(set_nums)[-3])