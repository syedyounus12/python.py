# list is datatype and it is a object
# list is unsafe (muteabule) 
# in the list we can store different types of datatypes
# list will maintain the insertion order
# list will allow duplicates values

l1 = []
print(l1, type(l1))
# [] <class 'list'>
l2 = list
print(l2, type(l2))
#<class 'list'> <class 'type'>

l3 = list()
print(l3, type(l3))
# [] <class 'list'>

l4 = [10, 12, 13, 14, "talha", "Younus", "Khadri"]
print(l4, type(l4))
# [10, 12, 13, 14, 'talha', 'Younus', 'Khadri'] <class 'list'>
l5 = [10, 20, 30, 10, 20, 50, 60]

print(l5)
# [10, 20, 30, 10, 20, 50, 60]
l6 = []
l6.append(120)
l6.append(130)
l6.append(140)
print(l6)
# [120, 130, 140] #list we are adding one by one
l5.append(70)
print(l5)
# [10, 20, 30, 10, 20, 50, 60, 70]
l7 = [10, 12, 14, 16,]
l7.extend("Younus")
print(l7)
# [10, 12, 14, 16, 'Y', 'o', 'u', 'n', 'u', 's'] frist behavioiour

l7.extend(["Talha", "Younus", "Khadri" ])
print(l7)
# [10, 12, 14, 16, 'Y', 'o', 'u', 'n', 'u', 's', 'Younus']
print(l7)
print(l7)
# [10, 12, 14, 16, 'Y', 'o', 'u', 'n', 'u', 's', 'Talha', 'Younus', 'Khadri'] second behavioiour


l1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
#      0   1   2   3   4   5   6   7   8    9  #index values
l1.pop()   # eleminets the last element
print(l1)
# [10, 20, 30, 40, 50, 60, 70, 80, 90] frist behavioiour
print(l1.pop(5))  # eleminets the with index value
# 60 index no. 5 #second behavioiour


l1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
#      0   1   2   3   4   5   6   7   8    9 
l1.insert(5, "Younus")      #insert(index, "element")
print(l1)
# [10, 20, 30, 40, 50, 'Younus', 60, 70, 80, 90, 100]



l1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
#      0   1   2   3   4   5   6   7   8    9 

l1.remove(40)  # removeing with element
print(l1)
# [10, 20, 30, 50, 60, 70, 80, 90, 100]


l1 = [10, 20, 30, 40]
l1.clear() #clear all the elements
print(l1)

l1 = [10, 20, 30, 40]
print(l1.copy()) #[10, 20, 30, 40]
                  # [10, 20, 30, 40]
print(l1)



l1 = [10, 20, 30, 40, 10, 20, 10, 20, 30, ]
print(l1.count(10)) # 3
print(l1.count(20)) #3   # counting the no.of elements
print(l1.count(30))  #2
print(l1)     

l1 = [10, 20, 30, 40, 10, 20, 10, 20, 30,]
l1.reverse()   #[30, 20, 10, 20, 10, 40, 30, 20, 10]
print(l1)

l1 = [30, 40, 20, 10, 50, 70, 90, 80, 60,]
l1.sort()   #[10, 20, 30, 40, 50, 60, 70, 80, 90]
print(l1)




