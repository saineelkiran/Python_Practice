# f=open("Myfile",'r')
#
# f1=open("xyz",'w')
#
# for i in f:
#     f1.write(i)

f1=open("python.jpg","rb")

f2=open("copy_python.jpg","wb")

for i in f1:
    f2.write(i)



