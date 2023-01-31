#. Write a Python program to find the first duplicate element in a given array of integers
# . Return -1 if there are no such elements
def find_duplicate(nums):
    num_set =set()
    return_value = -1

    for i in range (len(nums)):
        if nums[i] in num_set:
            return nums[i]
        else:
            num_set.add(nums[i])

    return return_value

print(find_duplicate([2,3,4,7,9,3,6,0,11,4,5]))