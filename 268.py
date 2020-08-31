nums = [0]
(element,) = set(range(0,len(nums)))-set(nums)
if(element==0):
    print(0)
else:
    print(element)