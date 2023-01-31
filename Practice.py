list_arr = [4,1,10,5,3,11,13,9]
sum = 0
target=14

for i in range(len(list_arr)-1):
    for j in range(i+1,len(list_arr)):
        #sum = list_arr[i] + list_arr[j]
        if list_arr[i] + list_arr[j] ==target:
           print(str(list_arr[i]) +","+ str(list_arr[j]))
