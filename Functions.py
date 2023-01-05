
# def Add(a,b):
#     c = a+b
#     d=a-b
#     #print("Sum of " + str(a)+ " and "+ str(b)+ " is "+str(c))
#     return c,d
#
# resultx , resulty = Add(54,35)
# print(resultx,resulty)
#---------------------------------------------------------------------------------
# def update(lst1):
#     print(id(lst1))
#     lst1[1]=40
#     print(id(lst1))
#     print("lst1 = ", lst1)
#
# lst =[20,30,60]
# print(id(lst))
# update(lst)
# print("lst =", lst)
#-----------------------------------------------------------------------------------

#Types of Parameters: position,Keyword, default, Variable length

# def per_det (name,age=18):
#     print(name)
#     print(age)
#
# per_det(age=27,name='Neel')
#
# #Variable Length
#
# def sum(*b):
#     c=0
#     for i in b:
#         c=c+i
#     print(c)
#
# sum(5,22,34,53,43)
#---------------------------------------------------------------------------------------
#KeyWord variable length

def person(**b):
    for i,j in b.items():
        print(i,j)

person(Name="Neel",Age=32,HomeTown='Khammam',EmailId="saineelkiran@gmail.com", Phone_Num=9705386291)