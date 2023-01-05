
def sort(nums):
    for i in range(len(nums)-1):
        min_pos=i
        for j in range(i,len(nums)):
            if nums[j]<nums[min_pos]:
                min_pos=j

        temp=nums[i]
        nums[i]=nums[min_pos]
        nums[min_pos]=temp

        print(nums)
nums=[8,7,20,34,21,67,29,37,22,29,2,3,99]
sort(nums)

# print(nums)
#
# print(sorted(nums))
