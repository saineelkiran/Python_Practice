name =("Sai Neel","Sravani","Vaishu","Lord Balaji","Sai Neel")
jobs=("Win Wire","Sel Employed","Kid","God","Win Wire")

print("\n For Loop output : \n")
zip_op=zip(name,jobs)
for i in zip_op:
    print (i)

print("\n List output :\n")

zip_op_list =list(zip(name,jobs))

print(zip_op_list)

print("\n SET output :\n")
zip_op_set=set(zip(name,jobs))

print(zip_op_set)
print("\n Dictionary output :\n")

zip_op_dic=dict(zip(name,jobs))
print(zip_op_dic)