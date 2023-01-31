import array as ar
b= ar.array('i',[1,2,3,4,5,2,5,9,7,6])

arr_1 = b[4:7]
print ("Array with Boundaries \n"+ str (arr_1))

arr_2 =b[4:]
print ("Array with Left boundary \n"+ str (arr_2))

arr_3 =b[:4]
print ("Array with Right boundary \n"+ str (arr_3))

arr_4 =b[:]
print ("Array with no boundaries \n"+ str (arr_4))

