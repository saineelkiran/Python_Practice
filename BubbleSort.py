
def sort(list):
    for i in range(len(list)-1,0,-1):
        for j in range(i):
            if list[j]>list[j+1]:
                temp =list[j]
                list[j]=list[j+1]
                list[j+1]=temp

list=[8,7,20,34,21,67,29,37,22,29,2,3,89,34]
sort(list)

print(list)

print(sorted(list))
print(len(list))