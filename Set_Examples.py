a=[1,2,1,3,0,0,4,7,8,6]
b=[5,5,7,8,7,9,6,1,1,2]

s1 = set(a)
print("unique numbers in a \n",s1)
s2 = set(b)
print("unique numbers in b \n",s2)

print("\n numbers that are present in a and not present in b \n",s1-s2)
print("\n numbers that are present in b and not present in a \n",s2-s1)

print("\n numbers that are present in either a or b \n",s1|s2)

print("\n numbers that are present in both a and b \n",s1&s2)

print("\n numbers that are present in  a and b  but not in both \n",s1^s2)