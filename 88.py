nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
m=6
n=3
def merge_lists(arr1,m,n,arr2):
    for i in range(n):
        arr1.pop()
    for n in arr2:
        arr1.append(n)
    arr1.sort()
    print(arr1)
merge_lists(nums1, 6,3,nums2)