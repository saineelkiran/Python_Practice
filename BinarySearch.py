pos=-1
def search(list,n):
   low=0
   upp=len(list)-1

   while low<=upp:
       mid=(low+upp)//2

       if(list[mid]==n):
           global pos
           pos = mid
           return True
       else:
           if n<list[mid]:
               upp=mid-1
           else:
               low=mid+1

n=108
list =[5,12,24,37,48,53,69,71,88,91,108,113]
if search(list,n):
    print("Search Element - Found @ position : ", pos+1)
else:
    print("Search Element -  Not Found")