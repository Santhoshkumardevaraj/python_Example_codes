from array import *

print("---ARRAY OPERATIONS---")

newarray=array('i',[10,34,17,15,26,5])
print("DISPLAY ARRAY")
print(newarray)

print("INSERT OPERATION")

insertelement=int(input("Enter element to be inserted: "))
insertposition=int(input("Enter position to be inserted: "))

newarray.insert(insertposition,insertelement)
print(newarray)
               
print("UPDATE OPERATION")

insertelement=int(input("Enter element to be inserted: "))
insertposition=int(input("Enter position to be updated: "))

newarray[insertposition]=insertelement
print(newarray)

print("DELETE OPERATION")

element=int(input("Enter element to be deleted: "))


newarray.remove(element)
print(newarray)

print("SEARCH POSITION BY ELEMENT")

element=int(input("Enter element to be searched: "))


print("Element Found at ",newarray.index(element))
print(newarray)
