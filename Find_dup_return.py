# Write a Python program to find out if a given array of integers contains any duplicate elements.
# Return true if any value appears at least twice in the array,
# and return false if every element is distinct.

def dup_element(array_lst):
    set_res = set(array_lst)
    return len(array_lst)!=len(set_res)

print(dup_element([1,2,3,4,5,2]))
