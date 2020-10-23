# Go Python -->  List Operations

P_List=[1,2,3,4,5]

print('#Print List \n',P_List)
P_List.append(14)

print('#After append \n',P_List)
P_List.extend([8,9,11,12,16])

print('#After extend \n',P_List)
P_List.insert(6,7)

print('#After insert \n',P_List)
P_List.remove(12)

print('#After remove \n',P_List)
print('#Finding index of 4\n',P_List.index(4))
print('#Finding count of 5 in List\n',P_List.count(5))

P_List.sort()
print('#Sorted list\n',P_List)

P_List.reverse()
print('#Reversed list\n',P_List)

P_Listcopy=P_List.copy()
print('#Copied list\n',P_Listcopy)

P_List.clear()
print('#After clear \n',P_List)

# END
