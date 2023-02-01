from array import array
import binascii
array1 = array("i",[2,3,63,6,85,23,21,4,7,89])
print ("array 1: ", array1)
as_bytes = array1.tobytes()
print("as Bytes : " ,as_bytes)
print("Bytes :", binascii.hexlify(as_bytes))
array2 =array('i')
array2.frombytes(as_bytes)
print("array2 : ",array2)

